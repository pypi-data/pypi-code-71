import sys
import typing
import bpy_types


class ShaderFxButtonsPanel:
    bl_context = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_space_type = None
    ''' '''


class DATA_PT_shader_fx(ShaderFxButtonsPanel, bpy_types.Panel,
                        bpy_types._GenericUI):
    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
    ''' '''

    def FX_BLUR(self, layout, fx):
        ''' 

        '''
        pass

    def FX_COLORIZE(self, layout, fx):
        ''' 

        '''
        pass

    def FX_FLIP(self, layout, fx):
        ''' 

        '''
        pass

    def FX_GLOW(self, layout, fx):
        ''' 

        '''
        pass

    def FX_PIXEL(self, layout, fx):
        ''' 

        '''
        pass

    def FX_RIM(self, layout, fx):
        ''' 

        '''
        pass

    def FX_SHADOW(self, layout, fx):
        ''' 

        '''
        pass

    def FX_SWIRL(self, layout, fx):
        ''' 

        '''
        pass

    def FX_WAVE(self, layout, fx):
        ''' 

        '''
        pass

    def append(self, draw_func):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass_py(self):
        ''' 

        '''
        pass

    def draw(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def is_extended(self):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_overridable_library(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def pop(self):
        ''' 

        '''
        pass

    def prepend(self, draw_func):
        ''' 

        '''
        pass

    def property_overridable_library_set(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def remove(self, draw_func):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass
