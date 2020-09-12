import bpy
from .utils import is_string


#region TEXT OBJECTS
def create_text_object(textname):
    return bpy.data.texts.new(textname)


def delete_text_object(textname):
    if is_string(textname):
        t = bpy.data.texts[textname]
        bpy.data.texts.remove(t)
    else:
        bpy.data.texts.remove(textname)


def get_lines_in_text_object(textname):
    return bpy.data.texts[textname].lines
#endregion
