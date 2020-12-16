from plantcv import plantcv as pcv

import logging

logger = logging.getLogger(__name__)

from ipso_phen.ipapi.base.ipt_abstract import IptBase


class IptPcvToto(IptBase):
    def build_params(self):
        self.add_enabled_checkbox()

    def process_wrapper(self, **kwargs):
        # Copy here the docstring generated by IPSO Phen
        wrapper = self.init_wrapper(**kwargs)
        if wrapper is None:
            return False

        res = False
        try:
            if self.get_value_of("enabled") == 1:
                img = wrapper.current_image

                # Write your code here
                wrapper.store_image(img, "current_image")
                res = True
            else:
                wrapper.store_image(wrapper.current_image, "current_image")
                res = True
        except Exception as e:
            res = False
            wrapper.error_holder.add_error(
                new_error_text=f'Failed to process {self. name}: "{repr(e)}"',
                new_error_level=35,
                target_logger=logger,
            )
        else:
            pass
        finally:
            return res

    @property
    def name(self):
        return "PCV toto"

    @property
    def package(self):
        return "PlantCV"

    @property
    def real_time(self):
        return False

    @property
    def result_name(self):
        return "image"

    @property
    def output_kind(self):
        return "image"

    @property
    def use_case(self):
        return ["PlantCV"]

    @property
    def description(self):
        return "Write your tool s description here. it will be used to generate documentation files"
