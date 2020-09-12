import bpy
from .utils import is_string


#region OBJECTS
def create_object(name, col):
    from .collections import create_collection
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
        from .collections import collection_exists
        if collection_exists(col):
            from .collections import get_collection
            col_ref = get_collection(col)
        else:
            from .collections import create_collection
            col_ref = create_collection(col)
    else:
        col_ref = col
    # Perform action
    new_obj = to_copy.copy()
    if new_obj.data is not None:
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


def duplicate_object(tocopy, col):
    return copy_object(tocopy, col)


def instance_object(ref, newname=None, col=None):
    from .collections import link_object_to_collection
    deselect_all_objects()
    select_object(ref)
    bpy.ops.object.duplicate_move_linked()
    o = selected_object()
    if newname is not None:
        o.name = newname
    if col is not None:
        link_object_to_collection(o, col)
    return o


def get_object(ref):
    # Expecting string
    if ref in bpy.data.objects:
        return bpy.data.objects[ref]
    else:
        return False


def get_obj(ref):
    return get_object(ref)


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


def rename_object(obj, newname):
    objref = None
    # obj is string
    if is_string(obj):
        objref = get_object(obj)
    else:
        objref = obj
    # set name - only if string
    if is_string(newname):
        objref.name = newname
        return True
    else:
        return False
#endregion
