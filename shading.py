import bpy
from math import radians

from .objects import (
    get_object, selected_object, deselect_all_objects,
    select_object
)
from .utils import is_string


#region SHADING
def shade_object_smooth(ref=None):
    objref = None
    if ref is not None:
        if is_string(ref):
            objref = get_object(ref)
        else:
            objref = ref
    else:
        # nothing supplied, use so
        objref = selected_object()
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.shade_smooth()


def shade_smooth(ref=None):
    shade_object_smooth(ref)


def shade_object_flat(ref=None):
    objref = None
    if ref is not None:
        if is_string(ref):
            objref = get_object(ref)
        else:
            objref = ref
    else:
        # nothing supplied, use so
        objref = selected_object()
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.shade_flat()


def shade_flat(ref=None):
    shade_object_flat(ref)


def set_smooth_angle(ref, degrees=60):
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    if objref.data.use_auto_smooth is False:
        objref.data.use_auto_smooth = True
    objref.data.auto_smooth_angle = radians(degrees)
#endregion
