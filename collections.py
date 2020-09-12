import bpy
from .utils import is_string


#region COLLECTIONS
def create_collection(name):
    if collection_exists(name) is False:
        bpy.data.collections.new(name)
        colref = bpy.data.collections[name]
        bpy.context.scene.collection.children.link(colref)
        return colref
    else:
        return False


def delete_collection(name, delete_objects=True):
    from .objects import deselect_all_objects
    from .objects import delete_selected_objects
    # Make sure collection exists
    if collection_exists(name):
        # String or reference check
        if is_string(name):
            col = get_collection(name)
        else:
            col = name
        # See if deleting the children
        if delete_objects is not None:
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
    from .objects import deselect_all_objects
    from .objects import delete_selected_objects
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


def delete_hierarchy(col):
    colref = None
    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col
        pass
    from .objects import deselect_all_objects
    deselect_all_objects()
    delete_objects_in_collection(colref)
    delete_collection(colref)


def duplicate_collection(col):
    from .objects import copy_object
    colref = None
    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col
    new_name = "Copy of " + colref.name
    new_col = create_collection(new_name)
    to_copy = get_objects_from_collection(colref.name)
    for o in to_copy:
        copy_object(o, new_col)
    return get_collection(new_name)


def get_objects_from_collection(col):
    if is_string(col):
        return bpy.data.collections[col].objects
    else:
        return col.objects


def get_collection(ref):
    if ref in bpy.data.collections:
        return bpy.data.collections[ref]
    else:
        return False


def get_col(ref):
    return get_collection(ref)


def get_list_of_collections():
    return bpy.data.collections


def link_object_to_collection(ref, col):
    from .objects import get_object
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


def link_objects_to_collection(ref, col):
    if is_string(col):
        for o in ref:
            bpy.data.collections[col].objects.link(o)
    else:
        for o in ref:
            col.objects.link(o)
        pass


def unlink_object_from_collection(ref, col):
    from .objects import get_object
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


def unlink_objects_from_collection(ref, col):
    # we assume that ref is a list
    colref = None

    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col

    for o in ref:
        colref.objects.unlink(o)


def move_object_to_collection(ref, col):
    from .objects import get_object
    objref = None
    colref = None

    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref

    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col

    cols = objref.users_collection
    for c in cols:
        c.objects.unlink(objref)
    link_object_to_collection(objref, colref)


def move_objects_to_collection(ref, col):
    colref = None

    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col

    # we assume that ref is object list
    for o in ref:
        for c in o.users_collection:
            c.objects.unlink(o)
        link_object_to_collection(o, colref)


def get_object_collection(ref):
    from .objects import get_object
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    return objref.users_collection[0]


def get_object_collections(ref):
    from .objects import get_object
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    return objref.users_collection


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
