import bpy


#Show hide section with arrow, optional checkbox, and text
def createShowHide(self, context, scn, properties, showHideBool, optionalCheckboxBool, text, layout):

    if scn is not None:
        data = eval( f"scn.{properties}" )
        boolThing = eval( f"scn.{properties}.{showHideBool}" )
    else:
        data = self
        boolThing = eval( f"self.{showHideBool}")

    if boolThing:
        showHideIcon = "TRIA_DOWN"
    else:
        showHideIcon = "TRIA_RIGHT"

    row = layout.row(align=True)

    downArrow = row.column(align=True)
    downArrow.alignment = "LEFT"
    downArrow.prop(data, showHideBool, text="", icon=showHideIcon, emboss=False )

    if optionalCheckboxBool is not None:
        checkbox = row.column(align=True)
        checkbox.alignment = "LEFT"
        checkbox.prop(data, optionalCheckboxBool, text="" )

    textRow = row.column(align=True)
    textRow.alignment = "LEFT"
    textRow.prop(data, showHideBool, text=text, emboss=False )

    emptySpace = row.column(align=True)
    emptySpace.alignment = "EXPAND"
    emptySpace.prop(data, showHideBool, text=" ", emboss=False)

def createProp(self, context, scn, bEnabled, labelText, data, propItem, scale_y, labelScale, propScale, labelAlign, propAlign, propText, bExpandProp, bUseSlider, layout):

    propRow = layout.row(align=True)

    if not bEnabled:
        propRow.enabled = False

    propRow.scale_y = scale_y

    propRowLabel = propRow.row(align=True)
    propRowLabel.alignment="EXPAND"
    propRowLabel.ui_units_x = labelScale

    propRowLabel1 = propRowLabel.row(align=True)
    propRowLabel1.alignment=labelAlign
    propRowLabel1.scale_x = 1

    propRowLabel1.label(text=labelText)

    propRowItem = propRow.row(align=True)
    propRowItem.alignment=propAlign

    propRowItem1 = propRowItem.row(align=True)
    propRowItem1.alignment=propAlign
    propRowItem1.ui_units_x = propScale
    propRowItem1.scale_x = 100

    propRowItem1.prop(data, propItem, text=propText, expand=bExpandProp, slider=bUseSlider)


def createPropWithHideButtonAlt(self, context, scn, properties, propName, customPropText, bUseSlider, embossResetBtn, layout):

    propRow = layout.row(align=True)

    data                       = eval( f"scn.{properties}" )


    propCol                    = propRow.column(align=True)
    propCol.prop               ( data, propName, text=customPropText, slider=bUseSlider)

    resetPropCol               = propRow.column(align=True)
    resetPropCol.active        = embossResetBtn
    resetPropOp                = resetPropCol.operator("ntzedgcrv.resetsettings", text="", icon="LOOP_BACK", emboss=embossResetBtn)
    resetPropOp.settingToReset = propName


def mainEdgCrvPanel(self, context, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel):
    layout = self.layout
    scn = context.scene

    #determine if panel is inside of a popop/pie menu
    panelInsidePopupOrPie = context.region.type == 'WINDOW'

    if panelInsidePopupOrPie:

        if bUseCompactPopupAndPiePanel:
            layout.ui_units_x = 8
            layout.label(text="Edge Curve+")

        else:
            layout.ui_units_x = 13
            layout.label(text="Neltulz - Edge Curve+")

    obj = context.object

    compactPanelConditions = (panelInsidePopupOrPie and bUseCompactPopupAndPiePanel) or (not panelInsidePopupOrPie and bUseCompactSidebarPanel)

    if compactPanelConditions:
        insertBtnScaleY = 1
    else:
        insertBtnScaleY = 1.5

    insertEdgesRow = layout.row(align=True)
    insertEdgesRow.scale_y = insertBtnScaleY
    
    op = insertEdgesRow.operator('ntzedgcrv.insertedges', text="Insert Edge(s)", icon="OUTLINER_OB_CURVE")

    if scn.ntzedgcrv.customEdgeCurveSettings == "USE":

        op.numSegments          = scn.ntzedgcrv.numSegmentsSlider
        op.useEdgeFlow          = scn.ntzedgcrv.useEdgeFlowCheckbox
        op.tension              = scn.ntzedgcrv.tensionSlider
        op.numIterations        = scn.ntzedgcrv.numIterationsSlider
        op.minAngle             = scn.ntzedgcrv.minAngleSlider

    popover = insertEdgesRow.popover(text="", panel="NTZEDGCRV_PT_options", icon="DOWNARROW_HLT")

    optionsSectionWrapper = layout.column(align=True)


def options_inner(self, context, scn, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel, layout):

    layout.label(text="Edge Curve Settings:")
    layout.prop(scn.ntzedgcrv, "customEdgeCurveSettings", text="")

    if scn.ntzedgcrv.customEdgeCurveSettings == "USE":

        edgeCurveSettings = layout.box().column(align=True)

        createPropWithHideButtonAlt(self, context, scn, "ntzedgcrv", "numSegmentsSlider", None, True, True, edgeCurveSettings)
        edgeCurveSettings.separator()

        createPropWithHideButtonAlt(self, context, scn, "ntzedgcrv", "useEdgeFlowCheckbox", None, False, False, edgeCurveSettings)
        edgeCurveSettings.separator()

        bEdgeFlowPropertiesEnabled = False #declare
        bUseSlider = False
        if scn.ntzedgcrv.useEdgeFlowCheckbox:
            bEdgeFlowPropertiesEnabled = True
            bUseSlider = True

        if bEdgeFlowPropertiesEnabled:
            edgeFlowProperties = edgeCurveSettings.column(align=True)

            createPropWithHideButtonAlt(self, context, scn, "ntzedgcrv", "tensionSlider",           None,      True, True, edgeFlowProperties)
            createPropWithHideButtonAlt(self, context, scn, "ntzedgcrv", "numIterationsSlider",     None,      True, True, edgeFlowProperties)
            createPropWithHideButtonAlt(self, context, scn, "ntzedgcrv", "minAngleSlider",          None,      True, True, edgeFlowProperties)

            edgeCurveSettings.separator()
    
        resetButton = edgeCurveSettings.row(align=True)
        resetButton.alignment="RIGHT"
        op = resetButton.operator('ntzedgcrv.resetsettings', text="Reset All Settings", icon="LOOP_BACK")
        op.settingToReset = "ALL"