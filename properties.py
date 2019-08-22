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

    exampleEnumItems = [
        ("1", "Name1", "NAME1"),
        ("2", "Name2", "NAME2"),
    ]

    exampleEnum : EnumProperty(
        items=exampleEnumItems,
        description="Description (Default: 1)",
        default="1"
    )

    numSegments : IntProperty(
        name="Segment Number",
        description="Number of segments to add. (Default: 1)",
        default = 1,
        min = 1,
        soft_max = 16
    )

    numIterations : IntProperty(
        name="Number of Iterations",
        description="Number of iterations. (Default: 1)",
        default = 1,
        min = 1,
        soft_max = 128
    )

    tension : IntProperty(
        name="Tension",
        description="Tension (Default: 180)",
        default = 180,
        max = 500,
        min = -500
    )

    minAngle : IntProperty(
        name="Minimum Angle",
        description="Minimum Angle (Default: 0)",
        default = 0,
        max = 180,
        min = 0
    )

    advancedSettings : BoolProperty(
        name="Checkbox Name",
        description="Use advanced settings. (Default: False)",
        default = False
    )