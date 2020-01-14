import bpy
from . properties import NTZEDGCRV_ignitproperties
from . import misc_functions

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

# -----------------------------------------------------------------------------
#   Reset Settings
# -----------------------------------------------------------------------------    

class NTZEDGCRV_OT_resetsettings(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "ntzedgcrv.resetsettings"
    bl_label = "Neltulz - Edge Curve : Reset Setting(s)"
    bl_description = "Resets setting(s)"

    settingToReset : StringProperty(
        name="Setting to Reset",
        description='Name of the setting to be reset',
        default = "NONE"
    )

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        scn = context.scene

        defaultSettingsDict = {
            "numSegmentsSlider"             : 1,
            "useEdgeFlowCheckbox"           : True,
            "tensionSlider"                 : 180,
            "numIterationsSlider"           : 4,
            "minAngleSlider"                : 0,
        }

        if self.settingToReset == "ALL":

            for key in defaultSettingsDict:
                setattr(scn.ntzedgcrv, key, defaultSettingsDict[key])

        elif self.settingToReset != "NONE":
            key = self.settingToReset
            setattr(scn.ntzedgcrv, key, defaultSettingsDict[key])

        return {'FINISHED'}
    # END execute()
# END Operator()
