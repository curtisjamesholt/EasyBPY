from mathutils import Vector
from .objects import so, get_object
from .utils import is_string


#region TRANSFORMATIONS
def location(obj=None, loc=None):
    # set up vars
    objref = None
    obj_provided = False
    loc_provided = False

    # obj checks
    if obj is not None:
        obj_provided = True
        # obj has been provided
        if is_string(obj):
            objref = get_object(obj)
        else:
            objref = obj

    # loc checks
    if loc is not None:
        # loc has been provided
        loc_provided = True

    if obj_provided:
        # obj has been provided
        if loc_provided:
            # case 1 - obj and loc provided
            objref.location = Vector((loc[0], loc[1], loc[2]))
        else:
            # case 2 - obj but no loc provided
            return objref.location
    else:
        # obj has not been provided
        if loc_provided:
            # case 3 - obj not provided but loc is
            objref = so()
            objref.location = Vector((loc[0], loc[1], loc[2]))
        else:
            # case 4 - no obj and no loc provided
            return so().location


def rotation(obj=None, rot=None):
    # set up vars
    objref = None
    obj_provided = False
    rot_provided = False

    # obj checks
    if obj is not None:
        obj_provided = True
        # obj has been provided
        if is_string(obj):
            objref = get_object(obj)
        else:
            objref = obj

    # newloc checks
    if rot is not None:
        # rot has been provided
        rot_provided = True

    if obj_provided:
        # obj has been provided
        if rot_provided:
            # case 1 - obj and rot provided
            objref.rotation_euler[0] = rot[0]
            objref.rotation_euler[1] = rot[1]
            objref.rotation_euler[2] = rot[2]
        else:
            # case 2 - obj but no rot provided
            return objref.rotation_euler
    else:
        # obj has not been provided
        if rot_provided:
            # case 3 - obj not provided but rot is
            objref = so()
            objref.rotation_euler[0] = rot[0]
            objref.rotation_euler[1] = rot[1]
            objref.rotation_euler[2] = rot[2]
        else:
            # case 4 - no obj and no rot provided
            return so().rotation_euler


def scale(obj=None, scale=None):
    # set up vars
    objref = None
    obj_provided = False
    scale_provided = False

    # obj checks
    if obj is not None:
        obj_provided = True
        # obj has been provided
        if is_string(obj):
            objref = get_object(obj)
        else:
            objref = obj

    # newloc checks
    if scale is not None:
        # rot has been provided
        scale_provided = True

    if obj_provided:
        # obj has been provided
        if scale_provided:
            # case 1 - obj and scale provided
            objref.scale[0] = scale[0]
            objref.scale[1] = scale[1]
            objref.scale[2] = scale[2]
        else:
            # case 2 - obj but no scale provided
            return objref.scale
    else:
        # obj has not been provided
        if scale_provided:
            # case 3 - obj not provided but scale is
            objref = so()
            objref.scale[0] = scale[0]
            objref.scale[1] = scale[1]
            objref.scale[2] = scale[2]
        else:
            # case 4 - no obj and no scale provided
            return so().scale
    pass
#endregion
