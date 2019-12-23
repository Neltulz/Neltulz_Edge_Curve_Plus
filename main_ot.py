import bpy
from . properties import NeltulzEdgeCurvePlus_IgnitProperties
from . import misc_functions

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

# -----------------------------------------------------------------------------
#    Main Addon Operator
# -----------------------------------------------------------------------------    

class OBJECT_OT_NeltulzEdgeCurvePlus(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "ntz_edg_curv.insertedges"
    bl_label = "Neltulz - Edge Curve Plus"
    bl_description = "Allows you to quick insert edges with flow"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    numSegments : IntProperty(
        name="Segment Number",
        description="Number of segments to add. (Default: 1)",
        default = 1,
        min = 1,
        soft_max = 16
    )

    useEdgeFlow : BoolProperty(
        name="Use Edge Flow",
        description='Allows you to use the EdgeFlow options (Tension, Num of iterations, Min Angle).  If this is disabled, then edges will be added without edge flow adjustments. (Default: True)',
        default = True
    )

    tension : IntProperty(
        name="Tension",
        description="Tension (Default: 180)",
        default = 180,
        max = 500,
        min = -500
    )

    numIterations : IntProperty(
        name="Number of Iterations",
        description="Number of iterations. (Default: 1)",
        default = 1,
        min = 1,
        soft_max = 128
    )


    minAngle : IntProperty(
        name="Minimum Angle",
        description="Minimum Angle (Default: 0)",
        default = 0,
        max = 180,
        min = 0
    )

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

                bpy.ops.mesh.loopcut(number_cuts=self.numSegments, object_index=0, edge_index=edgeIndex, mesh_select_mode_init=(False, True, False))

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
            
            
            #detect if EdgeFlow addon is installed and enabled
            if self.useEdgeFlow:
                try:
                    bpy.ops.mesh.set_edge_flow(tension=self.tension, iterations=self.numIterations, min_angle=self.minAngle)
                except:
                    self.report({'ERROR'}, 'The "EdgeFlow" add-on could not be found.  Please check to see if the Edge Flow addon is installed and enabled.' )
        
        else:
            self.report({'ERROR'}, 'Please select something before running the script.' )

        return {'FINISHED'}
    # END execute()
# END Operator()







