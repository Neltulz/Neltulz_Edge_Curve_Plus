bl_info = {
    "name" : "Neltulz - Edge Curve Plus",
    "author" : "Neil V. Moore",
    "description" : "Allows you to quickly insert edge loops with flow (Requires edge flow addon)",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 2),
    "location" : "View3D",
    "warning" : "",
    "category" : "3D View",
    "tracker_url": "https://www.logichaos.com/neltulz_blender_addons/neltulz_contact_page/neltulz_contact_page",
    "wiki_url": "https://www.logichaos.com/neltulz_blender_addons/neltulz_edge_curve_plus/README_Neltulz_Edge_Curve_Plus"
}

# -----------------------------------------------------------------------------
#   Import Classes and/or functions
# -----------------------------------------------------------------------------  

import bpy

from . properties import NeltulzEdgeCurvePlus_IgnitProperties
from . main_ot import OBJECT_OT_NeltulzEdgeCurvePlus
from . misc_ot import OBJECT_OT_NeltulzEdgeCurvePlus_ResetAllSettings
from . addon_preferences import OBJECT_OT_NeltulzEdgeCurvePlus_Preferences
from . panels import OBJECT_PT_NeltulzEdgeCurvePlus

from . import keymaps

PendingDeprecationWarning


# -----------------------------------------------------------------------------
#    Store classes in List so that they can be easily registered/unregistered    
# -----------------------------------------------------------------------------  

classes = (
    NeltulzEdgeCurvePlus_IgnitProperties,
    OBJECT_OT_NeltulzEdgeCurvePlus,
    OBJECT_OT_NeltulzEdgeCurvePlus_ResetAllSettings,
    OBJECT_OT_NeltulzEdgeCurvePlus_Preferences,
    OBJECT_PT_NeltulzEdgeCurvePlus,
)

# -----------------------------------------------------------------------------
#    Register classes from the classes list
# -----------------------------------------------------------------------------    

addon_keymaps = []

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    # update panel name
    addon_preferences.update_panel(None, bpy.context)

    #add keymaps from keymaps.py
    keymaps.neltulz_edge_curve_plus_register_keymaps(addon_keymaps)

    #add property group to the scene
    bpy.types.Scene.neltulzEdgeCurvePlus = bpy.props.PointerProperty(type=NeltulzEdgeCurvePlus_IgnitProperties)

    


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    #remove keymaps
    keymaps.neltulz_edge_curve_plus_unregister_keymaps(addon_keymaps)



if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.neltulz_edge_curve_plus()