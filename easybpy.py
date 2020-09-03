#region INFO
'''
    == EasyBPY ==
    Created by Curtis Holt
    ---
    https://YouTube.com/CurtisHolt
    https://curtisholt.online
    https://twitter.com/curtisjamesholt
    https://instagram.com/curtisjamesholt
    ---
    This purpose of this module is to simplify the use of the Blender API
    (bpy) by creating an extra layer of abstraction that is more human-
    readable, memorizable and reduces the user's exposure to complex code 
    paths.
    EasyBPY can be added to Blender by installing it into the:
                ../scripts/modules
    folder in the user preferences. The file can also be re-packaged with
    any other addon, so long as the developer respects the limitations of
    the GPL license, outlined below.
'''
'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#endregion
#region IMPORTS
import bpy
from mathutils import Vector
#endregion
#region OBJECTS
# Creates object - (string) name, (string) col
def create_object(name, col):
    m = bpy.data.meshes.new(name)
    o = bpy.data.objects.new(name, m)
    col_ref = None
    # Assess col
    if is_string(col):
        if col in bpy.data.collections:
            col_ref = bpy.data.collections[col]
        else:
            col_ref = create_collection(col)
    else:
        col_ref = col
        pass
    col_ref.objects.link(o)
    return o

def copy_object(tocopy, col):
    # Set up vars
    new_obj = None
    to_copy = None
    col_ref = None
    # Assess tocopy
    if is_string(tocopy):
        to_copy = get_object(tocopy)
    else:
        to_copy = tocopy
    # Assess col
    if is_string(col):
        if collection_exists(col):
            col_ref = get_collection(col)
        else:
            col_ref = create_collection(col)
    else:
        col_ref = col
    # Perform action
    new_obj = to_copy.copy()
    new_obj.data = to_copy.data.copy()
    new_obj.animation_data_clear()
    col_ref.objects.link(new_obj)
    return new_obj

# Returns the active selected object
def get_active_object():
    return bpy.context.active_object

def get_selected_objects():
    return bpy.context.selected_objects

def select_all_objects():
    pass

def deselect_all_objects():
    for ob in bpy.context.selected_objects:
        ob.select_set(False)

def delete_selected_objects():
    bpy.ops.object.delete()

def delete_object(ref):
    pass

def delete_objects_in_list(objlist):
    deselect_all_objects()
    for ob in objlist:
        ob.select_set(True)
    bpy.ops.object.delete()

def duplicate_object(tocopy,col):
    return copy_object(tocopy,col)

def instance_object(ref, newname):
    return bpy.data.new(name=newname, object_data=ref.data)

def get_object(ref):
    #Expecting string
    if ref in bpy.data.objects:
        return bpy.data.objects[ref]
    else:
        return False

def object_exists(ref):
    pass

# Primitive Objects
def create_cube():
    bpy.ops.mesh.primitive_cube_add()
    return bpy.data.objects["Cube"]
# etc...
#endregion
#region SHADING
def shade_object_smooth(ref):
    pass
def shade_object_flat(ref):
    pass
#endregion
#region MESHES
# Creates a mesh - (string) name
def create_mesh(name):
    return bpy.data.meshes.new(name)

def get_vertices(ref):
    return ref.data.vertices

def get_edges(ref):
    return ref.data.edges

def get_faces(ref):
    return ref.data.faces
#endregion
#region VERTEX GROUPS

# Creates a vertex group for the given object
# (object) ref, (string) group_name
def create_vertex_group(ref, group_name):
    ref.vertex_groups.new(name=group_name)
    return ref.vertex_groups[group_name]
#endregion
#region COLLECTIONS
def create_collection(name):
    if collection_exists(name) is False:
        bpy.data.collections.new(name)
        colref = bpy.data.collections[name]
        bpy.context.scene.collection.children.link(colref)
        return colref
    else:
        return False

def collection_exists(name):
    if name in bpy.data.collections:
        return True
    else:
        return False

def delete_collection(name, delete_objects = True):
    # Make sure collection exists
    if collection_exists(name):
        col = get_collection(name)
        # See if deleting the children
        if delete_objects != None:
            if delete_objects:
                deselect_all_objects()
                if len(col.objects) > 0:
                    for co in col.objects:
                        co.select_set(True)
                    delete_selected_objects()
        # Now remove collection
        bpy.data.collections.remove(col)
    else:
        return False

def delete_hierarchy(name):
    
    pass

def duplicate_collection(colname):
    pass

def get_object_from_collection(objname, collection):
    pass

def get_collection(ref):
    if ref in bpy.data.collections:
        return bpy.data.collections[ref]
    else:
        return False

def get_collections():
    return bpy.data.collections

def link_object_to_collection(ref, col):
    bpy.data.collections[col].objects.link(ref)

def unlink_object_from_collection(ref):
    ref.users_collection[0].unlink(ref)

def get_object_collection(ref):
    return ref.users_collection
#endregion
#region MATERIALS
def create_material(name):
    pass
def delete_material(name):
    pass
def add_material_to_object(objname, matname):
    pass
def remove_material_from_object(objref, matname):
    matindex = objref.data.materials.find(matname)
    objref.data.materials.pop(index=matindex)
#endregion
#region NODES
def set_material_use_nodes(matref, value):
    if value is True:
        matref.use_nodes = True
    else:
        matref.use_nodes = False

def get_node_tree(matref):
    matref.use_nodes = True
    return matref.node_tree.nodes

def create_node(nodes, nodetype):
    return nodes.new(type=nodetype)

def get_node_links(matref):
    return matref.node_tree.links

def create_node_link(matref, point1, point2):
    links = matref.node_tree.links
    return links.new(point1,point2)
#endregion
#region TEXTURES 
def create_texture(name, type):
    pass
def delete_texture(name):
    pass
#endregion
#region MODIFIERS
def add_modifier(object, name, id):
    pass
def get_modifier(object, name):
    pass
def remove_modifier(object, name):
    pass
# Specific Modiiers
def add_subsurf_modifier(ref, modname, level):
    mod_subsurf = ref.modifiers.new(modname, "SUBSURF")
    mod_subsurf.levels = level
    mod_subsurf.render = level
    return mod_subsurf
def add_displacement_modifier(ref, modname):
    mod_displace = ref.modifiers.new(modname, "DISPLACE")
    return mod_displace
#endregion
#region 3D VIEW
def get_cursor_location():
    return bpy.contex.scene.cursor_location

def set_cursor_location(newloc):
    bpy.context.scene.cursor_location = newloc
#endregion
#region TEXT OBJECTS
def create_text_object(textname):
    return bpy.data.texts.new(textname)
def delete_text_object(textname):
    t = bpy.data.texts[textname]
    bpy.data.texts.remove(t)
def get_lines_in_text_object(textname):
    return bpy.data.texts[textname].lines
#endregion
#region DATA CHECKS
def is_string(ref):
    if isinstance(ref, str):
        return True
    else:
        return False
#endregion
#region DATA CONSTRUCTORS
def make_vector(data):
    return Vector((data[0],data[1],data[2]))
#endregion
#region MISC
def run_python_from_string(pycode):
    exec(pycode)
#endregion