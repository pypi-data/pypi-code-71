from itertools import tee
from typing import Sequence

import numpy as np
from osgeo import gdal

from gdalos import util
from gdalos.util import make_points_list, make_xy_list, FillMode
from gdalos.viewshed.radio_params import RadioParams, RadioCalcType

st_seen = 5
st_seenbut = 4
st_hidbut = 3
st_hidden = 2
st_nodtm = 1
st_nodata = 0  # out of range value

viewshed_visible = st_seen
viewshed_thresh = st_hidbut
viewshed_invisible = st_hidden
viewshed_out_of_range = st_nodata
viewshed_ndv = st_nodata
viewshed_comb_ndv = 255
viewshed_comb_multi_val = 254

atmospheric_refraction_coeff = 1/7


class LOSParams(object):
    __slots__ = ['ox', 'oy', 'oz', 'tz', 'omsl', 'tmsl',
                 'refraction_coeff', 'mode', 'radio_parameters', 'fill_mode']

    def __init__(self):
        self.ox = None
        self.oy = None
        self.oz = None
        self.tz = None
        self.omsl = False  # observer MSL
        self.tmsl = False  # target MSL

        self.refraction_coeff = atmospheric_refraction_coeff
        self.mode = 2
        self.radio_parameters = None
        self.fill_mode = FillMode.zip_cycle

    def is_calc_oz(self):
        return self.oz is None

    def is_calc_tz(self):
        return self.tz is None

    @property
    def oxy(self):
        return make_points_list(self.ox, self.oy, self.fill_mode)

    @oxy.setter
    def oxy(self, oxy):
        self.ox, self.oy, *_ = make_xy_list(oxy)

    def update(self, d: dict):
        for k, v in d.items():
            setattr(self, k, v)

    def make_xy_lists(self):
        if not isinstance(self.ox, Sequence):
            self.ox = [self.ox]
        if not isinstance(self.oy, Sequence):
            self.oy = [self.oy]

    @classmethod
    def get_list_from_lists_dict(cls, d: dict, key_map=None) -> Sequence['LOSParams']:
        radio_d = d['radio_parameters']
        d['radio_parameters'] = None
        vp_array = util.get_list_from_lists_dict(d, cls(), key_map=key_map)
        if radio_d is not None:
            radio_array = util.get_list_from_lists_dict(radio_d, RadioParams(), key_map=key_map)
            r = None
            for i, v in enumerate(vp_array):
                if i < len(radio_array):
                    r = radio_array[i]
                v.radio_parameters = r
        return vp_array

    @classmethod
    def get_object_from_lists_dict(cls, d: dict, key_map=None) -> Sequence['LOSParams']:
        radio_d = d['radio_parameters']
        d['radio_parameters'] = None
        vp_obj = util.get_object_from_lists_dict(d, cls(), key_map=key_map)
        if radio_d is not None:
            radio_obj = util.get_object_from_lists_dict(radio_d, RadioParams(), key_map=key_map)
            radio_obj.unsequence()
            vp_obj.radio_parameters = radio_obj
        return vp_obj

    def get_calc_module(self):
        return -1 if not self.is_radio() else -2

    def is_radio(self):
        return self.radio_parameters is not None

    def get_radio_as_talos_params(self):
        return self.radio_parameters.get_dict()


class MultiPointParams(LOSParams):
    __slots__ = ('tx', 'ty', 'mode', 'results')

    def __init__(self):
        super(MultiPointParams, self).__init__()
        self.tx = None
        self.ty = None
        self.mode = None
        self.results = None

    def make_xy_lists(self):
        super(MultiPointParams, self).make_xy_lists()
        if not isinstance(self.tx, Sequence):
            self.tx = [self.tx]
        if not isinstance(self.ty, Sequence):
            self.ty = [self.ty]

    @property
    def txy(self):
        return make_points_list(self.tx, self.ty, self.fill_mode)

    @txy.setter
    def txy(self, txy):
        self.tx, self.ty = make_xy_list(txy)

    def get_as_talos_params(self):
        vp_params = \
            'omsl', 'tmsl', \
            'ox', 'oy', 'oz', 'tx', 'ty', 'tz', \
            'mode', 'results'

        mode_data_type = np.int32
        result_vector_name = 'AIO_res'
        mode_vector_name = 'A_mode'
        vector_names = {
            np.float64: ['A_ox', 'A_oy', 'A_oz', 'A_tx', 'A_ty', 'A_tz'],
            mode_data_type: [mode_vector_name],
            np.float32: [result_vector_name],
        }

        talos_params = \
            ['ObsMSL', 'TarMSL'] + \
            vector_names[np.float64] + \
            vector_names[mode_data_type] + vector_names[np.float32]

        d = {k1: getattr(self, k0) for k0, k1 in
             zip(vp_params, talos_params)}

        if d[mode_vector_name] is None:
            d[mode_vector_name] = np.array([RadioCalcType.PathLoss], dtype=mode_data_type)
        elif not isinstance(d[mode_vector_name], np.ndarray):
            if isinstance(d[mode_vector_name], (tuple, list)):
                d[mode_vector_name] = [RadioCalcType[x] for x in d[mode_vector_name]]

        for data_type, names in vector_names.items():
            for x in names:
                arr = d[x]
                if arr is not None and not isinstance(arr, np.ndarray):
                    d[x] = np.array(list(arr), dtype=data_type)

        input_coord_vectors = vector_names[np.float64]
        res_len = max(len(d[x]) for x in input_coord_vectors)
        mode_len = len(d[mode_vector_name])
        res_shape = None if d[result_vector_name] is None else d[result_vector_name].shape
        min_res_shape = (res_len, mode_len)
        if res_shape is None or res_shape[0] < min_res_shape[0] or res_shape[1] < min_res_shape[1]:
            d[result_vector_name] = np.zeros(min_res_shape, dtype=np.float32)
            assert min_res_shape == d[result_vector_name].shape
        return d


class ViewshedParams(LOSParams):
    __slots__ = ('max_r', 'min_r', 'min_r_shave', 'max_r_slant',
                 'azimuth', 'h_aperture', 'elevation', 'v_aperture',
                 'vv', 'iv', 'ov', 'ndv')

    def __init__(self):
        super().__init__()

        self.min_r = 0
        self.max_r = None

        self.min_r_shave = False
        self.max_r_slant = True

        self.azimuth = 0
        self.h_aperture = 360
        self.elevation = 0
        self.v_aperture = 180

        self.vv = viewshed_visible
        self.iv = viewshed_invisible
        self.ov = viewshed_out_of_range
        self.ndv = viewshed_ndv

    def is_omni_h(self):
        return not self.h_aperture or abs(self.h_aperture - 360) < 0.0001

    def get_as_gdal_params(self):
        vp_params = \
            'max_r', 'ox', 'oy', 'oz', 'tz', \
            'vv', 'iv', 'ov', 'ndv', 'mode'

        gdal_params = \
            'maxDistance', 'observerX', 'observerY', 'observerHeight', 'targetHeight', \
            'visibleVal', 'invisibleVal', 'outOfRangeVal', 'noDataVal', 'mode'
        d = {k1: getattr(self, k0) for k0, k1 in
             zip(vp_params, gdal_params)}
        d['dfCurvCoeff'] = 1 - self.refraction_coeff
        return d

    def get_result_dt(self):
        return gdal.GDT_Int16 if self.is_radio() or self.is_calc_oz() or self.is_calc_tz() else gdal.GDT_Byte

    def get_as_talos_params(self):
        vp_params = \
            'ox', 'oy', 'oz', 'max_r', 'min_r', 'min_r_shave', 'max_r_slant', 'tz', \
            'omsl', 'tmsl', 'azimuth', 'h_aperture', 'elevation', 'v_aperture'

        talos_params = \
            'ox', 'oy', 'oz', 'MaxRange', 'MinRange', 'MinRangeShave', 'SlantRange', 'tz', \
            'ObsMSL', 'TarMSL', 'Direction', 'Aperture', 'Elevation', 'ElevationAperture'
        d = {k1: getattr(self, k0) for k0, k1 in
             zip(vp_params, talos_params)}

        slack_dummy_height = -1000
        if d['oz'] is None or d['tz'] is None:
            if self.is_radio():
                raise Exception('You have to specify oz and tz for radio calc')
            if d['oz'] is None:
                d['oz'] = slack_dummy_height
                if d['tz'] is None:
                    raise Exception('You have to specify at least one of oz or tz')
            else:
                d['tz'] = slack_dummy_height

        d['result_dt'] = self.get_result_dt()
        return d


# gdal_viewshed_params_short = \
#     'max_r', 'ox', 'oy', 'oz', 'tz', \
#     'vv', 'iv', 'ov', 'ndv', 'mode',
#
# gdal_viewshed_params_full = \
#     'maxDistance', 'observerX', 'observerY', 'observerHeight', 'targetHeight', \
#     'visibleVal', 'invisibleVal', 'outOfRangeVal', 'noDataVal', 'mode'
# gdal_viewshed_keymap = dict(zip(gdal_viewshed_params_short, gdal_viewshed_params_full))

viewshed_defaults = dict(vv=viewshed_visible,
                         iv=viewshed_invisible,
                         ov=viewshed_out_of_range,
                         ndv=viewshed_ndv,
                         )

# gdal_viewshed_defaults = dict_util.replace_keys(viewshed_defaults,  gdal_viewshed_keymap)
