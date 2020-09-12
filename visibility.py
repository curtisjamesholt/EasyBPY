from .utils import is_string
from .objects import get_object, object_exists


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
