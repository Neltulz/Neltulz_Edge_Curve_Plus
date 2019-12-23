import bpy
from . properties import NeltulzEdgeCurvePlus_IgnitProperties
from . import misc_functions
from . import misc_layout

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

# -----------------------------------------------------------------------------
#   Panel
# ----------------------------------------------------------------------------- 

class OBJECT_PT_NeltulzEdgeCurvePlus(Panel):

    bl_idname = "ntz_edg_curv.panel"
    bl_label = "Edge Curve Plus v1.0.5"
    bl_category = "Neltulz"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):

        layout = self.layout
        scene = context.scene
        obj = context.object

        insertEdgesRow = layout.row(align=True)
        insertEdgesRow.scale_y = 1.5
        
        op = insertEdgesRow.operator('ntz_edg_curv.insertedges', text="Insert Edge(s)", icon="OUTLINER_OB_CURVE")
        
        if scene.neltulzEdgeCurvePlus.numSegmentsSlider_Enable:      op.numSegments          = scene.neltulzEdgeCurvePlus.numSegmentsSlider
        if scene.neltulzEdgeCurvePlus.useEdgeFlowCheckbox_Enable:    op.useEdgeFlow          = scene.neltulzEdgeCurvePlus.useEdgeFlowCheckbox
        if scene.neltulzEdgeCurvePlus.tensionSlider_Enable:          op.tension              = scene.neltulzEdgeCurvePlus.tensionSlider
        if scene.neltulzEdgeCurvePlus.numIterationsSlider_Enable:    op.numIterations        = scene.neltulzEdgeCurvePlus.numIterationsSlider
        if scene.neltulzEdgeCurvePlus.minAngleSlider_Enable:         op.minAngle             = scene.neltulzEdgeCurvePlus.minAngleSlider

        optionsSectionWrapper = layout.column(align=True)

        #create show/hide toggle for options section
        misc_layout.createShowHide(self, context, scene, "neltulzEdgeCurvePlus", "bShowOptions", None, "Options", optionsSectionWrapper)

        if scene.neltulzEdgeCurvePlus.bShowOptions:

            optionsSectionRow = optionsSectionWrapper.row(align=True)

            spacer = optionsSectionRow.column(align=True)
            spacer.label(text="", icon="BLANK1")

            optionsSection = optionsSectionRow.column(align=True)

            optionsSection.separator()

            misc_layout.createPropWithHideButton(self, context, scene, "neltulzEdgeCurvePlus", "numSegmentsSlider", "numSegmentsSlider_Enable", None, optionsSection)
            optionsSection.separator()

            misc_layout.createPropWithHideButton(self, context, scene, "neltulzEdgeCurvePlus", "useEdgeFlowCheckbox", "useEdgeFlowCheckbox_Enable", None, optionsSection)
            optionsSection.separator()

            if scene.neltulzEdgeCurvePlus.useEdgeFlowCheckbox:

                edgeFlowProperties = optionsSection.column(align=True)

                misc_layout.createPropWithHideButton(self, context, scene, "neltulzEdgeCurvePlus", "tensionSlider",       "tensionSlider_Enable",       None,      edgeFlowProperties)
                misc_layout.createPropWithHideButton(self, context, scene, "neltulzEdgeCurvePlus", "numIterationsSlider", "numIterationsSlider_Enable", None,      edgeFlowProperties)
                misc_layout.createPropWithHideButton(self, context, scene, "neltulzEdgeCurvePlus", "minAngleSlider",      "minAngleSlider_Enable",      None,      edgeFlowProperties)

            optionsSection.separator()
            
            resetButton = optionsSection.column(align=True)
            op = resetButton.operator('ntz_edg_curv.resetallsettings', text="Reset All Settings")
