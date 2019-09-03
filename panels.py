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
    bl_label = "Edge Curve Plus v1.0.4"
    bl_category = "Edge Curve+"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):

        layout = self.layout
        scene = context.scene
        obj = context.object

        col = layout.column(align=True)

        col.prop(context.scene.neltulzEdgeCurvePlus, "numSegmentsSlider", text="Number of segments" )

        col.separator()

        col = layout.column(align=True)

        col.prop(context.scene.neltulzEdgeCurvePlus, "useEdgeFlowCheckbox", text="Use Edge Flow" )

        if scene.neltulzEdgeCurvePlus.useEdgeFlowCheckbox:

            col = layout.column(align=True)

            col.prop(context.scene.neltulzEdgeCurvePlus, "tensionSlider", text="Tension" )
            col.prop(context.scene.neltulzEdgeCurvePlus, "numIterationsSlider", text="Number of iterations" )
            col.prop(context.scene.neltulzEdgeCurvePlus, "minAngleSlider", text="Min Angle" )

        col = layout.column(align=True)
        row = col.row(align=True)

        op = row.operator('object.neltulz_edge_curve_plus', text="Insert Edge(s)")
        op.numSegments = scene.neltulzEdgeCurvePlus.numSegmentsSlider
        op.useEdgeFlow = scene.neltulzEdgeCurvePlus.useEdgeFlowCheckbox
        op.tension = scene.neltulzEdgeCurvePlus.tensionSlider
        op.numIterations = scene.neltulzEdgeCurvePlus.numIterationsSlider
        op.minAngle = scene.neltulzEdgeCurvePlus.minAngleSlider

        op = row.operator('object.neltulz_edge_curve_plus_reset_all', text="Reset All Settings")
