import bpy
from . properties import NeltulzEdgeCurvePlus_IgnitProperties
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

# -----------------------------------------------------------------------------
#    Main Addon Operator
# -----------------------------------------------------------------------------    

class OBJECT_OT_NeltulzEdgeCurvePlus_ResetAllSettings(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.neltulz_edge_curve_plus_reset_all"
    bl_label = "Neltulz - Edge Curve Plus - Reset All Settings"
    bl_description = "Resets all settings"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        scene = context.scene

        scene.neltulzEdgeCurvePlus.numSegmentsSlider = 1
        scene.neltulzEdgeCurvePlus.useEdgeFlowCheckbox = True
        scene.neltulzEdgeCurvePlus.tensionSlider = 180
        scene.neltulzEdgeCurvePlus.numIterationsSlider = 1
        scene.neltulzEdgeCurvePlus.minAngleSlider = 0

        return {'FINISHED'}
    # END execute()
# END Operator()
