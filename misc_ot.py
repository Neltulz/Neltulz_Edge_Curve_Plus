import bpy
from . properties import NeltulzEdgeCurvePlus_IgnitProperties
from . import misc_functions

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

# -----------------------------------------------------------------------------
#   Reset All Settings
# -----------------------------------------------------------------------------    

class OBJECT_OT_NeltulzEdgeCurvePlus_ResetAllSettings(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "ntz_edg_curv.resetallsettings"
    bl_label = "Neltulz - Edge Curve Plus : Reset All Settings"
    bl_description = "Resets all settings"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        scene = context.scene

        scene.neltulzEdgeCurvePlus.numSegmentsSlider_Enable     = True
        scene.neltulzEdgeCurvePlus.numSegmentsSlider            = 1

        scene.neltulzEdgeCurvePlus.useEdgeFlowCheckbox_Enable   = True
        scene.neltulzEdgeCurvePlus.useEdgeFlowCheckbox          = True
        
        scene.neltulzEdgeCurvePlus.tensionSlider_Enable         = True
        scene.neltulzEdgeCurvePlus.tensionSlider                = 180
        
        scene.neltulzEdgeCurvePlus.numIterationsSlider_Enable   = True
        scene.neltulzEdgeCurvePlus.numIterationsSlider          = 4
        
        scene.neltulzEdgeCurvePlus.minAngleSlider_Enable        = True
        scene.neltulzEdgeCurvePlus.minAngleSlider               = 0

        return {'FINISHED'}
    # END execute()
# END Operator()