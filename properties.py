import bpy
from . import misc_functions

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )




class NeltulzEdgeCurvePlus_IgnitProperties(bpy.types.PropertyGroup):

    useEdgeFlowCheckbox : BoolProperty(
        name="Use Edge Flow",
        description="Applies edge flow to the newly created edge loops. (Default: True)",
        default = True
    )

    numSegmentsSlider : IntProperty(
        name="Segment Number",
        description="Number of segments to add. (Default: 1)",
        default = 1,
        min = 1,
        soft_max = 16
    )

    numIterationsSlider : IntProperty(
        name="Number of Iterations",
        description="Number of iterations. (Default: 1)",
        default = 1,
        min = 1,
        soft_max = 128
    )

    tensionSlider : IntProperty(
        name="Tension",
        description="Tension (Default: 180)",
        default = 180,
        max = 500,
        min = -500
    )

    minAngleSlider : IntProperty(
        name="Minimum Angle",
        description="Minimum Angle (Default: 0)",
        default = 0,
        max = 180,
        min = 0
    )
