import bpy
from . properties import NeltulzEdgeCurvePlus_IgnitProperties
from . import misc_functions
from . import addon_utils

# -----------------------------------------------------------------------------
#    Main Addon Operator
# -----------------------------------------------------------------------------    

class OBJECT_OT_NeltulzEdgeCurvePlus(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.neltulz_edge_curve_plus"
    bl_label = "Neltulz - Edge Curve Plus"
    bl_description = "Allows you to quick insert edges with flow"



    @classmethod
    def poll(cls, context):
        return (context.object.type == 'MESH' and bpy.context.object.mode == "EDIT")

    def execute(self, context):

        obj = context.object
        scene = context.scene

        selectedVerts = misc_functions.getSelectedVerts(self, context, obj)
        if len(selectedVerts) > 0:
            
            selectedEdges = misc_functions.getSelectedEdges(self, context, obj)
            selectedEdgeIndices = list()

            for edge in selectedEdges:
                selectedEdgeIndices.append(edge.index)


            

            totalNewEdgeLoopIndices = list()


            for edgeIndex in set(selectedEdgeIndices):

                bpy.ops.mesh.loopcut(number_cuts=scene.neltulzEdgeCurvePlus.numSegments, object_index=0, edge_index=edgeIndex, mesh_select_mode_init=(False, True, False))

                newEdges = misc_functions.getSelectedEdges(self, context, obj)
                newEdgeIndices = list()
                for edge in newEdges:
                    newEdgeIndices.append(edge.index)

                totalNewEdgeLoopIndices = list( set(totalNewEdgeLoopIndices).union(newEdgeIndices) )

            bpy.ops.mesh.select_all(action='DESELECT')
            
            totalEdges = misc_functions.getAllEdges(self, context, obj)
            
            #switch to object mode
            bpy.ops.object.mode_set(mode='OBJECT')

            for i in range( len(totalNewEdgeLoopIndices) ):
                obj.data.edges[ totalNewEdgeLoopIndices[i] ].select = True

            #switch to edit mode
            bpy.ops.object.mode_set(mode='EDIT')
            
            if addon_utils.check("EdgeFlow")[1]:
                print(scene.neltulzEdgeCurvePlus.tension)
                print(scene.neltulzEdgeCurvePlus.numIterations)
                print(scene.neltulzEdgeCurvePlus.minAngle)
                
                bpy.ops.mesh.set_edge_flow(tension=scene.neltulzEdgeCurvePlus.tension, iterations=scene.neltulzEdgeCurvePlus.numIterations, min_angle=scene.neltulzEdgeCurvePlus.minAngle)
            else:
                self.report({'ERROR'}, 'The "EdgeFlow" add-on could not be found.  Please check to see if the Edge Flow addon is installed and enabled.' )
        
        else:
            self.report({'ERROR'}, 'Please select something before running the script.' )
        
      


            

        return {'FINISHED'}
    # END execute()
# END Operator()







