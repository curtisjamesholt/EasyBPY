import bpy


#region OBJECTS - SELECTION
def select_all_meshes():
    bpy.ops.object.select_by_type(type='MESH')


def select_all_curves():
    bpy.ops.object.select_by_type(type='CURVE')


def select_all_surfaces():
    bpy.ops.object.select_by_type(type='SURFACE')


def select_all_metas():
    bpy.ops.object.select_by_type(type='META')


def select_all_text():
    bpy.ops.object.select_by_type(type='FONT')


def select_all_hair():
    bpy.ops.object.select_by_type(type='HAIR')


def select_all_point_clouds():
    bpy.ops.object.select_by_type(type='POINTCLOUD')


def select_all_volumes():
    bpy.ops.object.select_by_type(type='VOLUME')


def select_all_armatures():
    bpy.ops.object.select_by_type(type='ARMATURE')


def select_all_lattices():
    bpy.ops.object.select_by_type(type='LATTICE')


def select_all_empties():
    bpy.ops.object.select_by_type(type='EMPTY')


def select_all_greace_pencils():
    bpy.ops.object.select_by_type(type='GPENCIL')


def select_all_cameras():
    bpy.ops.object.select_by_type(type='CAMERA')


def select_all_speakers():
    bpy.ops.object.select_by_type(type='SPEAKER')


def select_all_light_probes():
    bpy.ops.object.select_by_type(type='LIGHT_PROBE')


def invert_selection():
    bpy.ops.object.select_all(action='INVERT')
#endregion
