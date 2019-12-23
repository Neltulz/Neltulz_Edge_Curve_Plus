import bpy

#Show hide section with arrow, optional checkbox, and text
def createShowHide(self, context, scene, properties, showHideBool, optionalCheckboxBool, text, layout):

    if scene is not None:
        data = eval( f"scene.{properties}" )
        boolThing = eval( f"scene.{properties}.{showHideBool}" )
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

def createPropWithHideButton(self, context, scene, properties, propName, propNameVisibilityBool, customPropText, layout):

    propRow = layout.row(align=True)
    propVisible = eval(f"scene.{properties}.{propNameVisibilityBool}")

    if propVisible:
         propXButtonIcon = "X"
         propEditButtonIcon = "BLANK1"
         propEnabled = True

    else:
        propXButtonIcon = "BLANK1"
        propEditButtonIcon = "GREASEPENCIL"
        propEnabled = False

    data                    = eval( f"scene.{properties}" )

    propEditButton          = propRow.column(align=True)
    propEditButton.prop     ( data, propNameVisibilityBool, text="", icon=propEditButtonIcon, emboss=False )
    propEditButton.enabled  = not(propEnabled)
    propEditButton.active   = False

    propRow.separator()

    propCol                 = propRow.column(align=True)
    propCol.prop            ( data, propName, text=customPropText)
    propCol.enabled         = propEnabled
    propRow.separator()
    
    propXButton             = propRow.column(align=True)
    propXButton.prop        ( data, propNameVisibilityBool, text="", icon=propXButtonIcon,    emboss=False )
    propXButton.enabled     = propEnabled