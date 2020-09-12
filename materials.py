import bpy
from .objects import get_object
from .utils import is_string


#region MATERIALS
def create_material(name):
    return bpy.data.materials.new(name)


def material_exists(ref):
    if is_string(ref):
        if ref in bpy.data.materials:
            return True
        else:
            return False
    # redundant but for safety
    else:
        if ref.name in bpy.data.materials:
            return True
        else:
            return False


def delete_material(name):
    matref = None
    if is_string(name):
        matref = get_material(name)
    else:
        matref = name
    bpy.data.materials.remove(matref)


def get_material(name):
    if name in bpy.data.materials:
        return bpy.data.materials[name]


def add_material_to_object(ref, matname):
    objref = None
    matref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref

    if is_string(matname):
        matref = get_material(matname)
    else:
        matref = matname

    if matref is not None:
        objref.data.materials.append(matref)


def remove_material_from_object(ref, matname):
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref

    matindex = objref.data.materials.find(matname)
    if matname in objref.data.materials:
        objref.data.materials.pop(index=matindex)


def remove_material(ref, matname):
    return remove_material_from_object(ref, matname)


def get_materials_from_object(ref):
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    mat_list = []
    mats = objref.data.materials.items()
    for m in mats:
        mat_list.append(m[1])
    return mat_list


def get_material_names_from_object(ref):
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    name_list = []
    mats = objref.data.materials.items()
    for m in mats:
        name_list.append(m[0])
    return name_list
#endregion
