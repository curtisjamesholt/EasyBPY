import bpy


#region 3D CURSOR
def selection_to_cursor_without_offset():
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)


def selection_to_cursor_with_offset():
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)


def cursor_to_world_origin():
    bpy.ops.view3d.snap_cursor_to_center()


def cursor_to_selection():
    bpy.ops.view3d.snap_cursor_to_selected()


def cursor_to_active():
    bpy.ops.view3d.snap_cursor_to_selected()


def selection_to_grid():
    bpy.ops.view3d.snap_selected_to_grid()


def selection_to_active():
    bpy.ops.view3d.snap_selected_to_active()


def cursor_to_grid():
    bpy.ops.view3d.snap_cursor_to_grid()


def get_cursor_location():
    return bpy.contex.scene.cursor_location


def set_cursor_location(newloc):
    bpy.context.scene.cursor_location = newloc
#endregion
