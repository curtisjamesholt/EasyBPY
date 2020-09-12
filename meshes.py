import bpy
from .objects import get_object
from .utils import is_string


#region MESHES
# Creates a mesh - (string) name
def create_mesh(name):
    return bpy.data.meshes.new(name)


def get_vertices(ref):
    if is_string(ref):
        return get_object(ref).data.vertices
    else:
        return ref.data.vertices


def get_edges(ref):
    if is_string(ref):
        return get_object(ref).data.edges
    else:
        return ref.data.edges


def get_faces(ref):
    return get_polygons(ref)


def get_polygons(ref):
    if is_string(ref):
        return get_object(ref).data.polygons
    else:
        return ref.data.polygons


def get_mesh_from_object(ref):
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    return objref.data
#endregion
