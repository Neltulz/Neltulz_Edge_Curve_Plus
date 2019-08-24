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
#   Panel
# ----------------------------------------------------------------------------- 

class OBJECT_PT_NeltulzEdgeCurvePlus(Panel):

    bl_idname = "object.neltulz_edge_curve_plus_panel"
    bl_label = "Edge Curve Plus v1.0.0"
    bl_category = "Edge Curve+"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):

        layout = self.layout
        scene = context.scene
        obj = context.object

        col = layout.column(align=True)
        #col.label(text="Title:")
        row = col.row(align=True)

        #op = row.operator('object.neltulz_edge_curve_plus', text="BUTTON TEXT")
        #op.PROPERTYNAME=1

        #END Overlay Options (Wireframe, Edge colors, etc)

        # -----------------------------------------------------------------------------
        #   Use Advanced Settings Box
        # -----------------------------------------------------------------------------

        col = layout.column(align=True)
        row = col.row(align=True)

        col.prop(context.scene.neltulzEdgeCurvePlus, "numSegments", text="Number of segments" )
        col.prop(context.scene.neltulzEdgeCurvePlus, "tension", text="Tension" )
        col.prop(context.scene.neltulzEdgeCurvePlus, "numIterations", text="Number of iterations" )
        col.prop(context.scene.neltulzEdgeCurvePlus, "minAngle", text="Min Angle" )

        col = layout.column(align=True)
        row = col.row(align=True)

        op = row.operator('object.neltulz_edge_curve_plus', text="Insert Edge(s)")

        col.separator()

        col.prop(context.scene.neltulzEdgeCurvePlus, "advancedSettings", text="Use Advanced Settings" )
        

        if scene.neltulzEdgeCurvePlus.advancedSettings:

            boxAdvancedOptions = layout.box()
            boxAdvancedOptions.label(text="Advanced Settings:")

            box = boxAdvancedOptions.column(align=True)
            
            row = box.row(align=True)

            #op = row.operator('object.neltulz_edge_curve_plus', text="BUTTON TEXT")
            #op.PROPERTYNAME=1

        #END Use Advanced Settings Box