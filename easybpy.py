import bpy

# == OBJECTS ==
# Creates object - (string) name, (string) col
def create_object(name, col):
    m = bpy.data.meshes.new(name)
    o = bpy.data.objects.new(name, m)
    colref = bpy.data.collections[col]
    colref.objects.link(o)
    return o

# Returns the active selected object
def get_active_object():
    return bpy.context.active_object
def get_selected_objects():
    return bpy.context.selected_objects
def select_all_objects():
    pass
def deselect_all_objects():
    pass
def delete_object(ref):
    pass

def duplicate_object(ref):
    pass

def instance_object(ref):
    pass

def get_object(ref):
    pass

def object_exists(ref):
    pass

# Primitive Objects
def create_cube():
    pass
# etc...

# == SHADING ==
def shade_object_smooth(ref):
    pass
def shade_object_flat(ref):
    pass

# == MESHES ==
# Creates a mesh - (string) name
def create_mesh(name):
    return bpy.data.meshes.new(name)
def get_vertices(ref):
    return ref.data.vertices

# == VERTEX GROUPS ==

# Creates a vertex group for the given object
# (object) ref, (string) group_name
def create_vertex_group(ref, group_name):
    ref.vertex_groups.new(name=group_name)
    return ref.vertex_groups[group_name]

# == COLLECTIONS ==
def create_collection(name):
    pass
def delete_collection(name):
    pass
def duplicate_collection(name):
    pass
def get_object_from_collection(name, collection):
    pass

# == MATERIALS ==
def create_material(name):
    pass
def delete_material(name):
    pass
def add_material_to_object(objname, matname):
    pass
def remove_material_from_object(objname, matname):
    pass

# == TEXTURES ==
def create_texture(name, type):
    pass
def delete_texture(name):
    pass

# == MODIFIERS ==
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