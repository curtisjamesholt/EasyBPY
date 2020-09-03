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

def get_active_object():
    return bpy.context.active_object

def active_object():
    return get_active_object()

def get_selected_object():
    return get_active_object()

def selected_object():
    return get_selected_object()

def so():
    return get_selected_object()

def get_selected_objects():
    return bpy.context.selected_objects

def select_object(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            bpy.data.objects[ref].select_set(True)
        else:
            return False
    # ref is object reference
    else:
        ref.select_set(True)

def select_all_objects():
    for co in bpy.context.scene.objects:
        co.select_set(True)

def deselect_object(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            bpy.data.objects[ref].select_set(False)
        else:
            return False
    # ref is object reference
    else:
        ref.select_set(False)
    pass

def deselect_all_objects():
    for ob in bpy.context.selected_objects:
        ob.select_set(False)

def delete_selected_objects():
    bpy.ops.object.delete()

def delete_object(ref):
    deselect_all_objects()
    # ref is string
    if is_string(ref):
        obj = get_object(ref)
        obj.select_set(True)
    # ref is object reference
    else:
        ref.select_set(True)
    delete_selected_objects()

def delete_objects(objlist):
    deselect_all_objects()
    for ob in objlist:
        ob.select_set(True)
    bpy.ops.object.delete()

def duplicate_object(tocopy,col):
    return copy_object(tocopy,col)

def instance_object(ref, newname = None, col = None):
    deselect_all_objects()
    select_object(ref)
    bpy.ops.object.duplicate_move_linked()
    o = selected_object()
    if newname != None:
        o.name = newname
    if col != None:
        link_object_to_collection(o,col)
    return o

def get_object(ref):
    #Expecting string
    if ref in bpy.data.objects:
        return bpy.data.objects[ref]
    else:
        return False

def object_exists(ref):
    if is_string(ref):
        if ref in bpy.data.objects:
            return True
        else:
            return False
    # redundant but for safety
    else:
        if ref.name in bpy.data.objects:
            return True
        else:
            return False
#endregion
#region OBJECTS - PRIMITIVES
def create_cube():
    bpy.ops.mesh.primitive_cube_add()
    return bpy.data.objects["Cube"]

def create_cylinder():
    bpy.ops.mesh.primitive_cylinder_add()
    return bpy.data.objects["Cylinder"]

def create_ico_sphere():
    bpy.ops.mesh.primitive_ico_sphere_add()
    return bpy.data.objects["Icosphere"]

def create_suzanne():
    bpy.ops.mesh.primitive_monkey_add()
    return bpy.data.objects["Suzanne"]

def create_monkey():
    create_suzanne()

def create_cone():
    bpy.ops.mesh.primitive_cone_add()
    return bpy.data.objects["Cone"]
#endregion
#region VISIBILITY
def hide_in_viewport(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            obj = get_object(ref)
            obj.hide_viewport = True
    # ref is an object reference
    else:
        if object_exists(ref):
            ref.hide_viewport = True
        else:
            return False

def show_in_viewport(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            obj = get_object(ref)
            obj.hide_viewport = False
    # ref is an object reference
    else:
        if object_exists(ref):
            ref.hide_viewport = False
        else:
            return False

def hide_in_render(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            obj = get_object(ref)
            obj.hide_render = True
    # ref is an object reference
    else:
        if object_exists(ref):
            ref.hide_render = True
        else:
            return False

def show_in_render(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            obj = get_object(ref)
            obj.hide_render = False
    # ref is an object reference
    else:
        if object_exists(ref):
            ref.hide_render = False
        else:
            return False

def display_as_bounds(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            obj = get_object(ref)
            obj.display_type = 'BOUNDS'
    # ref is an object reference
    else:
        if object_exists(ref):
            ref.display_type = 'BOUNDS'
        else:
            return False

def display_as_textured(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            obj = get_object(ref)
            obj.display_type = 'TEXTURED'
    # ref is an object reference
    else:
        if object_exists(ref):
            ref.display_type = 'TEXTURED'
        else:
            return False

def display_as_solid(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            obj = get_object(ref)
            obj.display_type = 'SOLID'
    # ref is an object reference
    else:
        if object_exists(ref):
            ref.display_type = 'SOLID'
        else:
            return False

def display_as_wire(ref):
    # ref is string
    if is_string(ref):
        if object_exists(ref):
            obj = get_object(ref)
            obj.display_type = 'WIRE'
    # ref is an object reference
    else:
        if object_exists(ref):
            ref.display_type = 'WIRE'
        else:
            return False
#endregion
#region TRANSFORMATIONS
def location(obj = None, newloc = None):
    pass
def rotation(obj = None, newrot = None):
    pass
def scale(obj = None, newscale = None):
    pass
#endregion
#region 3D CURSOR
def selection_to_cursor_without_offset():
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

def selection_to_cursor_with_offset():
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)

def cursor_to_world_origin():
    bpy.ops.view3d.snap_cursor_to_center()

def cursor_to_selection():
    bpy.ops.view3d.snap_cursor_to_selected()

def cursor_to_active():
    bpy.ops.view3d.snap_cursor_to_selected()

def selection_to_grid():
    bpy.ops.view3d.snap_selected_to_grid()

def selection_to_active():
    bpy.ops.view3d.snap_selected_to_active()

def cursor_to_grid():
    bpy.ops.view3d.snap_cursor_to_grid()
    
def get_cursor_location():
    return bpy.contex.scene.cursor_location

def set_cursor_location(newloc):
    bpy.context.scene.cursor_location = newloc
#endregion
#region SHADING
def shade_object_smooth(ref):
    bpy.ops.object.shade_smooth()
    pass
def shade_object_flat(ref):
    bpy.ops.object.shade_flat()
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

def delete_collection(name, delete_objects = True):
    # Make sure collection exists
    if collection_exists(name):
        # String or reference check
        if is_string(name):
            col = get_collection(name)
        else:
            col = name
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

def delete_objects_in_collection(col):
    # setting up colref
    colref = None
    # col is a string
    if collection_exists(col):
        if is_string(col):
            colref = get_collection(col)
        else:
            colref = col
    # delete all objects in colref
    deselect_all_objects()
    for co in colref.objects:
        co.select_set(True)
    delete_selected_objects()

def delete_hierarchy(name):

    pass

def duplicate_collection(colname):
    pass

def get_objects_from_collection(colname):
    pass

def get_collection(ref):
    if ref in bpy.data.collections:
        return bpy.data.collections[ref]
    else:
        return False

def get_list_of_collections():
    return bpy.data.collections

def link_object_to_collection(ref, col):
    if is_string(col):
        if is_string(ref):
            objref = get_object(ref)
            bpy.data.collections[col].objects.link(objref)
        else:
            bpy.data.collections[col].objects.link(ref)
    else:
        if is_string(ref):
            objref = get_object(ref)
            col.objects.link(objref)
        else:
            col.objects.link(ref)

def unlink_object_from_collection(ref, col):
    #ref.users_collection[0].unlink(ref)
    if is_string(col):
        if is_string(ref):
            objref = get_object(ref)
            bpy.data.collections[col].objects.unlink(objref)
        else:
            bpy.data.collections[col].objects.unlink(ref)
    else:
        if is_string(ref):
            objref = get_object(ref)
            col.objects.unlink(objref)
        else:
            col.objects.unlink(ref)

def get_object_collection(ref):
    return ref.users_collection

def collection_exists(col):
    if is_string(col):
        if col in bpy.data.collections:
            return True
        else:
            return False
    else:
        if col.name in bpy.data.collections:
            return True
        else:
            return False
#endregion
#region MATERIALS
def create_material(name):
    return bpy.data.materials.new(name)
def delete_material(name):
    bpy.data.materials.remove(name)
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
def add_displace_modifier(ref, modname):
    mod_displace = ref.modifiers.new(modname, "DISPLACE")
    return mod_displace
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
def clear_unwanted_data():
    clear_unused_data()
def clear_unused_data():
    bpy.ops.outliner.orphans_purge()
#endregion