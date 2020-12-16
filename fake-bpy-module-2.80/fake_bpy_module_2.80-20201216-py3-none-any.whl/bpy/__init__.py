import sys
import typing
import bpy.types

from . import types
from . import ops
from . import path
from . import utils
from . import app
from . import props
from . import context

data: 'bpy.types.BlendData' = None
''' Access to Blender's internal data
'''
