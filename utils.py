import bpy
from mathutils import Vector


#region DATA CHECKS
def is_string(ref):
    if isinstance(ref, str):
        return True
    else:
        return False
#endregion


#region DATA CONSTRUCTORS
def make_vector(data):
    return Vector((data[0], data[1], data[2]))
#endregion


#region MISC
def clear_unwanted_data():
    clear_unused_data()


def clear_unused_data():
    bpy.ops.outliner.orphans_purge()
#endregion
