import sys
import typing
import bpy.types


def brush_stroke(stroke: typing.Union[
        typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.
        List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection'] = None,
                 mode: typing.Union[str, int] = 'NORMAL',
                 ignore_background_click: bool = False):
    ''' Sculpt a stroke into the geometry

    :param stroke: Stroke
    :type stroke: typing.Union[typing.Dict[str, 'bpy.types.OperatorStrokeElement'], typing.List['bpy.types.OperatorStrokeElement'], 'bpy_prop_collection']
    :param mode: Stroke Mode, Action taken when a paint stroke is made * NORMAL Normal, Apply brush normally. * INVERT Invert, Invert action of brush for duration of stroke. * SMOOTH Smooth, Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Union[str, int]
    :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
    :type ignore_background_click: bool
    '''

    pass


def detail_flood_fill():
    ''' Flood fill the mesh with the selected detail setting

    '''

    pass


def dynamic_topology_toggle():
    ''' Dynamic topology alters the mesh topology while sculpting

    '''

    pass


def optimize():
    ''' Recalculate the sculpt BVH to improve performance

    '''

    pass


def sample_detail_size(location: typing.List[int] = (0, 0)):
    ''' Sample the mesh detail on clicked point

    :param location: Location, Screen Coordinates of sampling
    :type location: typing.List[int]
    '''

    pass


def sculptmode_toggle():
    ''' Toggle sculpt mode in 3D view

    '''

    pass


def set_detail_size():
    ''' Set the mesh detail (either relative or constant one, depending on current dyntopo mode)

    '''

    pass


def set_persistent_base():
    ''' Reset the copy of the mesh that is being sculpted on

    '''

    pass


def symmetrize():
    ''' Symmetrize the topology modifications

    '''

    pass


def uv_sculpt_stroke(mode: typing.Union[str, int] = 'NORMAL'):
    ''' Sculpt UVs using a brush

    :param mode: Mode, Stroke Mode * NORMAL Normal, Apply brush normally. * INVERT Invert, Invert action of brush for duration of stroke. * RELAX Relax, Switch brush to relax mode for duration of stroke.
    :type mode: typing.Union[str, int]
    '''

    pass
