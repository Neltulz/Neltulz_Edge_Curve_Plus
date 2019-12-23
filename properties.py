import bpy
from . import misc_functions

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

class NeltulzEdgeCurvePlus_IgnitProperties(bpy.types.PropertyGroup):

    bShowOptions : BoolProperty (
        name="Show Options",
        description="Reveals options.",
        default = False,
    )

    useEdgeFlowCheckbox_Enable : BoolProperty(
        name="Enable Use Edge Flow",
        description='Enables the "Use Edge Flow Checkbox" (Default: True)',
        default = True
    )

    useEdgeFlowCheckbox : BoolProperty(
        name="Use Edge Flow",
        description="Applies edge flow to the newly created edge loops. (Default: True)",
        default = True
    )

    numSegmentsSlider_Enable : BoolProperty (
        name="Enable Num Segments Slider",
        description="Enables the Num Segments Slider (Default: True)",
        default = True
    )

    numSegmentsSlider : IntProperty(
        name="Segment Num",
        description="Number of segments to add. (Default: 1)",
        default = 1,
        min = 1,
        soft_max = 16
    )

    numIterationsSlider_Enable : BoolProperty (
        name="Enable numIterationsSlider",
        description="Enables the numIterationsSlider (Default: True)",
        default = True
    )

    numIterationsSlider : IntProperty(
        name="Num Iterations",
        description="Number of iterations. (Default: 1)",
        default = 4,
        min = 1,
        soft_max = 128
    )

    tensionSlider_Enable : BoolProperty (
        name="Enable Tension",
        description="Enables the Tension slider",
        default = True
    )

    tensionSlider : IntProperty(
        name="Tension",
        description="Tension (Default: 180)",
        default = 180,
        max = 500,
        min = -500
    )

    minAngleSlider_Enable : BoolProperty (
        name="Enable minAngleSlider",
        description="Enables the minAngleSlider",
        default = True
    )

    minAngleSlider : IntProperty(
        name="Minimum Angle",
        description="Minimum Angle (Default: 0)",
        default = 0,
        max = 180,
        min = 0
    )