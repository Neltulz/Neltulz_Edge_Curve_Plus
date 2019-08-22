import bpy
        

# -----------------------------------------------------------------------------
#   Determine which mode is currently Selected (Vert, Edge, Face, etc)
#   Returned: (0=Multiple modes, 1=Vertice Mode, 2=Edge Mode, 3=Face Mode)
# -----------------------------------------------------------------------------

def getCurrentSelectMode(self, context):
    #Create empty list
    tempList = []

    #check current mesh select mode
    for bool in bpy.context.tool_settings.mesh_select_mode:
        tempList.append(bool)
    
    #convert list into a tuple
    tempTuple = tuple(tempList)

    currentSelectMode = int()

    
    if tempTuple == (True, False, False):       
        currentSelectMode = 1
    elif tempTuple == (False, True, False):
        currentSelectMode = 2
    elif tempTuple == (False, False, True):
        currentSelectMode = 3
    else:
        pass #(defaults currentSelectMode to 0)

    return currentSelectMode
# END getCurrentSelectMode(self, context)


def getSelectedVerts(self, context, obj):
    mesh = obj.data

    #switch to object mode before getting edgeList
    bpy.ops.object.mode_set(mode='OBJECT')

    vertList = [v for v in mesh.vertices if v.select]

    #switch back to edit mode
    bpy.ops.object.mode_set(mode='EDIT')
        
    return vertList

def getSelectedEdges(self, context, obj):
    mesh = obj.data

    #switch to object mode before getting edgeList
    bpy.ops.object.mode_set(mode='OBJECT')

    edgeList = [e for e in mesh.edges if e.select]

    #switch back to edit mode
    bpy.ops.object.mode_set(mode='EDIT')
        
    return edgeList

def getAllEdges(self, context, obj):
    mesh = obj.data

    #switch to object mode before getting edgeList
    bpy.ops.object.mode_set(mode='OBJECT')

    edgeList = [e for e in mesh.edges]
    #edgeList = list(filter(lambda e: e, mesh.edges))

    #switch back to edit mode
    bpy.ops.object.mode_set(mode='EDIT')
        
    return edgeList