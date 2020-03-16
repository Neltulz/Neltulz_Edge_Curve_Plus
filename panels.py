import bpy
from . properties import NTZEDGCRV_ignitproperties
from . import misc_functions
from . import misc_layout

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

# -----------------------------------------------------------------------------
#   Panel
# ----------------------------------------------------------------------------- 

class NTZEDGCRV_PT_options(Panel):
    bl_label = "Neltulz - Edge Curve - Options"
    bl_idname = "NTZEDGCRV_PT_options"
    bl_category = ""
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"

    def draw(self, context):
        scn = context.scene
        layout = self.layout
        layout.ui_units_x = 15

        optionsSection = layout.column(align=True)

        misc_layout.options_inner(self, context, scn, True, True, optionsSection)

    #END draw()

class NTZEDGCRV_PT_sidebarpanel(Panel):
    bl_label = "Edge Curve Plus v1.0.7"
    bl_category = "Neltulz"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bUseCompactSidebarPanel = BoolProperty(
        name="Use Compact Panel",
        description="Use Compact Panel",
        default = False
    )

    bUseCompactPopupAndPiePanel = BoolProperty(
        name="Use Compact Popup & Pie Panel",
        description="Use Compact Popup & Pie Panel",
        default = True
    )

    def draw(self, context):
        misc_layout.mainEdgCrvPanel(self, context, self.bUseCompactSidebarPanel, self.bUseCompactPopupAndPiePanel)