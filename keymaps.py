import bpy
from . properties import NTZEDGCRV_ignitproperties

# -----------------------------------------------------------------------------
#    Keymaps (For Register)
# -----------------------------------------------------------------------------    

def neltulz_edge_curve_plus_register_keymaps(addon_keymaps):

    wm = bpy.context.window_manager

    def createEdgeCurvePlusKeymap():
        #create shortcuts for keymap
        kmi = km.keymap_items.new("ntzedgcrv.insertedges", type = "E", ctrl=False, shift=True, alt=True, value = "PRESS")
        kmi.properties.numSegments = 1
        kmi.properties.useEdgeFlow = True
        kmi.properties.tension = 180
        kmi.properties.numIterations = 4
        kmi.properties.minAngle = 0

    #------------------------------Mesh Mode----------------------------------------------------------------------------

    #create new keymap
    km = wm.keyconfigs.addon.keymaps.new(name = "Mesh", space_type="EMPTY")

    createEdgeCurvePlusKeymap()

    #add list of keymaps
    addon_keymaps.append(km)

def neltulz_edge_curve_plus_unregister_keymaps(addon_keymaps):
    # handle the keymap
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    addon_keymaps.clear()