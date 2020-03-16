bl_info = {
    "name" : "Neltulz - Edge Curve",
    "author" : "Neil V. Moore",
    "description" : "Allows you to quickly insert edge loops with flow (Requires edge flow addon)",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 7),
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

from . properties        import NTZEDGCRV_ignitproperties
from . main_ot           import NTZEDGCRV_OT_insertedges
from . misc_ot           import NTZEDGCRV_OT_resetsettings
from . addon_preferences import NTZEDGCRV_OT_addonprefs
from . panels            import NTZEDGCRV_PT_options
from . panels            import NTZEDGCRV_PT_sidebarpanel

from . import keymaps

PendingDeprecationWarning

bDebugModeActive = False
if bDebugModeActive:
    print("##################################################################################################################################################################")
    print("REMINDER: DEBUG MODE ACTIVE")
    print("##################################################################################################################################################################")

# -----------------------------------------------------------------------------
#    Store classes in List so that they can be easily registered/unregistered    
# -----------------------------------------------------------------------------  

classes = (
    NTZEDGCRV_ignitproperties,
    NTZEDGCRV_OT_insertedges,
    NTZEDGCRV_OT_resetsettings,
    NTZEDGCRV_OT_addonprefs,
    NTZEDGCRV_PT_options,
    NTZEDGCRV_PT_sidebarpanel,
)

# -----------------------------------------------------------------------------
#    Register classes from the classes list
# -----------------------------------------------------------------------------    

addon_keymaps = []

#vscode pme workaround from iceythe (part 2 of 2)
def _reg():
    pme = bpy.utils._preferences.addons['pie_menu_editor'].preferences
    for pm in pme.pie_menus:
        if pm.key != 'NONE':
            pm.register_hotkey()
#END vscode pme workaround (part 2 of 2)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    # update panel name
    prefs = bpy.context.preferences.addons[__name__].preferences
    addon_preferences.update_panel(prefs, bpy.context)

    #add keymaps from keymaps.py
    keymaps.neltulz_edge_curve_plus_register_keymaps(addon_keymaps)

    #add property group to the scene
    bpy.types.Scene.ntzedgcrv = bpy.props.PointerProperty(type=NTZEDGCRV_ignitproperties)

    


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    #remove keymaps
    keymaps.neltulz_edge_curve_plus_unregister_keymaps(addon_keymaps)



if __name__ == "__main__":
    register()

    # test call
    bpy.ops.ntzedgcrv.insertedges()