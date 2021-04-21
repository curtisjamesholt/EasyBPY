#region INFO
'''
    == EasyBPY 0.1.2 ==
    Managed by Curtis Holt
    https://curtisholt.online/links
    ---
    This purpose of this module is to simplify the use of the Blender API
    (bpy) by creating an extra layer of abstraction that is more human-
    readable, memorizable and reduces the user's exposure to complex code 
    paths.
    EasyBPY can be added to Blender by installing it into the:
                ../scripts/modules
    folder in the user preferences. The file can also be re-packaged with
    any other addon, so long as the developer respects the limitations of
    the GPL license, outlined below.
'''
'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#endregion
#region IMPORTS
import bpy
import bpy.types
from mathutils import Vector, Matrix, Euler
import math
import random
from math import radians
#endregion
#region RENDER SETTINGS
def set_render_engine_to_cycles():
    get_scene().render.engine = 'CYCLES'

def set_render_engine_cycles():
    set_render_engine_to_cycles()

def set_render_engine_to_eevee():
    get_scene().render.engine = 'BLENDER_EEVEE'

def set_render_engine_eevee():
    set_render_engine_to_eevee()

def render_image(use_view = False):
    bpy.ops.render.render(use_viewport=use_view)
    return bpy.data.images['Render Result']

def render_animation(use_view = False):
    bpy.ops.render.render(animation=True, use_viewport=use_view)

def set_render_resolution(x, y):
    get_scene().render.resolution_x = x
    get_scene().render.resolution_y = y

def get_render_resolution():
    reslist = []
    reslist.append(get_scene().render.resolution_x)
    reslist.append(get_scene().render.resolution_y)
    return reslist

def render_resolution(x = None, y = None):
    if x is not None and y is not None:
        set_render_resolution(x,y)
    else:
        return get_render_resolution()

def set_render_resolution_percentage(percent):
    get_scene().render.resolution_percentage = percent

def set_render_percentage(percent = None):
    set_render_resolution_percentage(percent)

def set_render_percent(percent = None):
    set_render_resolution_percentage(percent)

def get_render_resolution_percentage():
    return get_scene().render.resolution_percentage

def render_resolution_percentage(percent = None):
    if percent is not None:
        set_render_resolution_percentage(percent)
    else:
        return get_render_resolution_percentage()

def set_render_pixel_aspect_ratio(x, y):
    get_scene().render.pixel_aspect_x = x
    get_scene().render.pixel_aspect_y = y

def get_render_pixel_aspect_ratio():
    aspectlist = []
    aspectlist.append(get_scene().render.pixel_aspect_x)
    aspectlist.append(get_scene().render.pixel_aspect_y)
    return aspectlist

def render_aspect_ratio(x = None, y = None):
    if x is not None and y is not None:
        set_render_pixel_aspect_ratio(x,y)
    else:
        return get_render_pixel_aspect_ratio()

def current_frame(val = None):
    if val is None:
        return get_scene().frame_current
    else:
        get_scene().frame_current = val

def set_frame(val = None):
    current_frame(val)

def frame_start(val = None):
    if val is None:
        return get_scene().frame_start
    else:
        get_scene().frame_start = val

def frame_end(val = None):
    if val is None:
        return get_scene().frame_end
    else:
        get_scene().frame_end = val

def set_current_frame(val = None):
    current_frame(val)

def set_frame_start(val = None):
    frame_start(val)

def set_frame_end(val = None):
    frame_end(val)

def set_start_frame(val = None):
    frame_start(val)

def set_end_frame(val = None):
    frame_end(val)

def set_frame_interval(start = None, end = None):
    frame_start(start)
    frame_end(end)

def set_frame_step(val):
    get_scene().frame_step = val

def set_render_fps(val, base = 1.0):
    get_scene().render.fps = val
    get_scene().render.fps_base = base
#endregion
#region OBJECTS
def create_object(name = None, col = None):
    if name is None:
        name = "New Object"
    m = bpy.data.meshes.new(name)
    o = bpy.data.objects.new(name, m)
    col_ref = None
    # Assess col
    if col == None:
        col_ref=bpy.context.view_layer.active_layer_collection.collection
    elif is_string(col):
        if col in bpy.data.collections:
            col_ref = bpy.data.collections[col]
        else:
            col_ref = create_collection(col)
    else:
        col_ref = col
    col_ref.objects.link(o)
    return o

def copy_object(tocopy, col = None):
    # Set up vars
    new_obj = None
    to_copy = get_object(tocopy)
    col_ref = None
    
    # Assess col
    if col == None:
        col_ref = get_active_collection()
    elif is_string(col):
        if collection_exists(col):
            col_ref = get_collection(col)
        else:
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

def ao():
    return get_active_object()

def so():
    return get_selected_objects()

def get_selected_objects():
    return bpy.context.selected_objects

def get_all_objects():
    return bpy.data.objects

def get_list_of_objects():
    get_all_objects()

def select_object(ref, make_active=True):
    objref = get_object(ref)
    objref.select_set(True)
    if make_active:
        bpy.context.view_layer.objects.active = objref

def selected_objects():
    return get_selected_objects()

def select_all_objects(col = None):
    if col == None:
        for co in bpy.context.scene.objects:
            co.select_set(True)
    else:
        col_ref = None
        if is_string(col):
            if collection_exists(col):
                col_ref = get_collection(col)
        else:
            col_ref = col
        for c in col_ref.objects:
            c.select_set(True)

def select_only(ref = None):
    objref = get_object(ref)
    deselect_all_objects()
    select_object(objref)

def deselect_object(ref):
    objref = get_object(ref)
    objref.select_set(False)

def deselect_all_objects():
    for ob in so():
        ob.select_set(False)

def delete_selected_objects():
    bpy.ops.object.delete()

def delete_object(ref = None):
    objref = get_object(ref)
    bpy.data.objects.remove(objref, do_unlink=True)

def delete_objects(objlist = None):
    objlist = get_objects()
    for obj in objlist:
        ref = get_object(obj)
        bpy.data.objects.remove(ref, do_unlink=True)

def duplicate_object(tocopy,col):
    return copy_object(tocopy,col)

def instance_object(ref, newname = None, col = None):
    deselect_all_objects()
    select_object(ref)
    bpy.ops.object.duplicate_move_linked()
    o = selected_object()
    if newname is not None:
        o.name = newname
    if col is not None:
        link_object_to_collection(o,col)
    return o

def get_object(ref):
    objref = None
    if ref is None:
        objref = ao()
    else:
        if is_string(ref):
            if object_exists(ref):
                objref = bpy.data.objects[ref]
        else:
            objref = ref
    return objref

def get_obj(ref):
    return get_object(ref)

def get_objects(ref = None):
    objref = []
    if ref is None:
        objref = so()
    else:
        if isinstance(ref, list):
            if len(ref) > 0:
                if isinstance(ref[0], bpy.types.Object):
                    objref = ref
                elif isinstance(ref[0], str):
                    for ob_name in ref:
                        if object_exists(ref):
                            objref.append(bpy.data.objects[ref])
        elif is_string(ref):
            if object_exists(ref):
                objref.append(bpy.data.objects[ref])
        elif isinstance(ref, bpy.types.Object) :
            objref.append(ref)
    return objref

def get_objs(ref = None):
    return get_objects(ref)

def get_median_point_of_objects(objs):
    point_loc = Vector()
    for obj in objs:
        point_loc += obj.location
    point_loc /= len(objs)
    return point_loc

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

def get_parent(ref = None):
    return get_object(ref).parent

def get_children(ref = None):
    return get_object(ref).children

def set_parent(child = None,parent = None):
    child = get_object(child)
    parent = get_object(parent)
    child.parent = parent 
    child.matrix_parent_inverse = parent.matrix_world.inverted()

def clear_parent(ref = None, keep_location = True):
    ref = get_object(ref)
    loc = ref.matrix_world.to_translation()
    print(loc)
    ref.parent = None
    if keep_location:
        ref.location = loc

def get_bounding_box(ref = None):
    return get_object(ref).bound_box

def get_bounding_box_corners(ref = None):
    return [ref.matrix_world @ Vector(corner) for corner in get_bounding_box(ref)]
#endregion
#region OBJECTS - CONVERSION
def convert_to_mesh(ref):
    objref = get_object(ref)
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.convert(target='MESH')

def convert_to_grease_pencil(ref):
    objref = get_object(ref)
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.convert(target='GPENCIL')

def convert_to_curve(ref):
    objref = get_object(ref)
    deselect_all_objects()
    select_object(objref)
    bpy.ops.object.convert(target='CURVE')
#endregion
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

def select_all_grease_pencils():
    bpy.ops.object.select_by_type(type='GPENCIL')

def select_all_cameras():
    bpy.ops.object.select_by_type(type='CAMERA')

def select_all_lights():
    bpy.ops.object.select_by_type(type='LIGHT')

def select_all_speakers():
    bpy.ops.object.select_by_type(type='SPEAKER')

def select_all_light_probes():
    bpy.ops.object.select_by_type(type='LIGHT_PROBE')

def invert_selection():
    bpy.ops.object.select_all(action='INVERT')

def get_objects_with_modifiers():
    objlist = []
    for obj in bpy.data.objects:
        if len(obj.modifiers) > 0:
            objlist.append(obj)
    return objlist

def select_objects_with_modifiers():
    deselect_all_objects()
    for obj in bpy.data.objects:
        if len(obj.modifiers) > 0:
            select_object(obj)

# Custom Selection
def get_objects_including(include, case_sensitive = True):
    objlist = []
    for o in bpy.data.objects:
        if case_sensitive is True:
            if include in o.name:
                objlist.append(o)
        else:
            if (include.lower() in o.name) or (include.upper() in o.name) or (include in o.name):
                objlist.append(o)
    return objlist

def select_objects_including(include, case_sensitive = True):
    for o in bpy.data.objects:
        if case_sensitive is True:
            if include in o.name:
                o.select_set(True)
        else:
            if (include.lower() in o.name) or (include.upper() in o.name) or (include in o.name):
                o.select_set(True)

def get_objects_by_vertex(count = 0, mode="EQUAL"):
    cmode = mode.upper()
    objlist = []
    for o in bpy.data.objects:
        if isinstance(o.data, bpy.types.Mesh):
            # o.data / len(o.data.vertices)
            if cmode == "EQUAL" or cmode == "SAME":
                if len(o.data.vertices) == count:
                    objlist.append(o)
            if cmode == "GREATER" or cmode == "MORE":
                if len(o.data.vertices) > count:
                    objlist.append(o)
            if cmode == "LESS" or cmode == "FEWER":
                if len(o.data.vertices) < count:
                    objlist.append(o)
    return objlist

def select_objects_by_vertex(count = 0, mode="EQUAL"):
    objs = get_objects_by_vertex(count, mode)
    for o in objs:
        o.select_set(True)

#endregion
#region OBJECTS - PRIMITIVES
# Mesh
def create_plane():
    bpy.ops.mesh.primitive_plane_add()
    return active_object()

def create_cube():
    bpy.ops.mesh.primitive_cube_add()
    return active_object()

def create_circle():
    bpy.ops.mesh.primitive_circle_add()
    return active_object()

def create_cylinder():
    bpy.ops.mesh.primitive_cylinder_add()
    return active_object()

def create_uv_sphere():
    bpy.ops.mesh.primitive_uv_sphere_add()
    return active_object()

def create_sphere():
    return create_uv_sphere()

def create_ico_sphere():
    bpy.ops.mesh.primitive_ico_sphere_add()
    return active_object()

def create_cone():
    bpy.ops.mesh.primitive_cone_add()
    return active_object()

def create_torus():
    bpy.ops.mesh.primitive_torus_add()
    return active_object()

def create_grid():
    bpy.ops.mesh.primitive_grid_add()
    return active_object()

def create_suzanne():
    bpy.ops.mesh.primitive_monkey_add()
    return active_object()

def create_monkey():
    return create_suzanne()

# Curve
def create_bezier_curve():
    bpy.ops.curve.primitive_bezier_curve_add()
    return active_object()

def create_bezier():
    return create_bezier_curve()

def create_circle_curve():
    bpy.ops.curve.primitive_circle_add()
    return active_object()

def create_nurbs_curve():
    bpy.ops.curve.primitive_nurbs_curve_add()
    return active_object()

def create_nurbs_circle():
    bpy.ops.curve.primitive_nurbs_circle_add()
    return active_object()

def create_nurbs_path():
    bpy.ops.curve.primitive_nurbs_path_add()
    return active_object()

def create_path():
    return create_nurbs_path()

# Surface
def create_nurbs_curve_surface():
    bpy.ops.surface.primitive_nurbs_surface_curve_add()
    return active_object()

def create_curve_surface():
    return create_nurbs_curve_surface()

def create_nurbs_circle_surface():
    bpy.ops.surface.primitive_nurbs_surface_circle_add()
    return active_object()

def create_circle_surface():
    return create_nurbs_circle_surface()

def create_nurbs_surface():
    bpy.ops.surface.primitive_nurbs_surface_surface_add()
    return active_object()

def create_nurbs_cylinder_surface():
    bpy.ops.surface.primitive_nurbs_surface_cylinder_add()
    return active_object()

def create_cylinder_surface():
    return create_nurbs_cylinder_surface()

def create_nurbs_sphere_surface():
    bpy.ops.surface.primitive_nurbs_surface_sphere_add()
    return active_object()

def create_sphere_surface():
    return create_nurbs_sphere_surface()

def create_nurbs_torus_surface():
    bpy.ops.surface.primitive_nurbs_surface_torus_add()
    return active_object()

def create_torus_surface():
    return create_nurbs_torus_surface()

# Metaball
def create_metaball():
    bpy.ops.object.metaball_add(type='BALL')
    active_object()

def create_metaball_capsule():
    bpy.ops.object.metaball_add(type='CAPSULE')
    active_object()

def create_metaball_plane():
    bpy.ops.object.metaball_add(type='PLANE')
    active_object()

def create_metaball_ellipsoid():
    bpy.ops.object.metaball_add(type='ELLIPSOID')
    active_object()

def create_metaball_cube():
    bpy.ops.object.metaball_add(type='CUBE')
    active_object()

# Text
def create_text_object():
    bpy.ops.object.text_add()
    return active_object()

def create_text():
    return create_text_object()

#endregion
#region OBJECTS - CONSTRAINTS
def add_constraint(type, ref = None, name = ""):
    objref = get_object(ref)
    new_con = objref.constraints.new(type)
    if name : 
        new_con.name = name
    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            area.tag_redraw()
    return new_con

def get_constraint(name, ref = None):
    objref = get_object(ref)

    # we assume name is string
    if name in objref.constraints:
        return objref.constraints[name]
    else:
        # Maybe return the 1st constraint on selected object?
        return None

def get_constraints_by_type(type,ref = None):
    objref = get_object(ref)
    constraints = [con for con in objref.constraints if con.type == type]
    return constraints

def remove_constraint(name = None, ref = None):
    objref = get_object(ref)

    if name is not None:
        if is_string(name):
            if name in objref.constraints:
                mod = get_constraint(name,objref)
                objref.constraints.remove(mod)
        else:
            objref.constraints.remove(name)
    else:
        remove_constraint(objref.constraints[0])
    
    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            area.tag_redraw()

def add_camera_solver_constraint(ref = None, name = ""):
    return add_constraint('CAMERA_SOLVER', ref, name)

def add_follow_track_constraint(ref = None, name = ""):
    return add_constraint('FOLLOW_TRACK', ref, name)

def add_object_solver_constraint(ref = None, name = ""):
    return add_constraint('OBJECT_SOLVER', ref, name)

def add_copy_location_constraint(ref = None, name = ""):
    return add_constraint('COPY_LOCATION', ref, name)

def add_copy_rotation_constraint(ref = None, name = ""):
    return add_constraint('COPY_ROTATION', ref, name)

def add_copy_scale_constraint(ref = None, name = ""):
    return add_constraint('COPY_SCALE', ref, name)

def add_copy_transforms_constraint(ref = None, name = ""):
    return add_constraint('COPY_TRANSFORMS', ref, name)

def add_limit_distance_constraint(ref = None, name = ""):
    return add_constraint('LIMIT_DISTANCE', ref, name)

def add_limit_location_constraint(ref = None, name = ""):
    return add_constraint('LIMIT_LOCATION', ref, name)

def add_limit_rotation_constraint(ref = None, name = ""):
    return add_constraint('LIMIT_ROTATION', ref, name)

def add_limit_scale_constraint(ref = None, name = ""):
    return add_constraint('LIMIT_SCALE', ref, name)

def add_maintain_volume_constraint(ref = None, name = ""):
    return add_constraint('MAINTAIN_VOLUME', ref, name)

def add_transform_constraint(ref = None, name = ""):
    return add_constraint('TRANSFORM', ref, name)

def add_transformation_constraint(ref = None, name = ""):
    return add_constraint('TRANSFORM', ref, name)

def add_transform_cache_constraint(ref = None, name = ""):
    return add_constraint('TRANSFORM_CACHE', ref, name)

def add_clamp_to_constraint(ref = None, name = ""):
    return add_constraint('CLAMP_TO', ref, name)

def add_damped_track_constraint(ref = None, name = ""):
    return add_constraint('DAMPED_TRACK', ref, name)

def add_locked_track_constraint(ref = None, name = ""):
    return add_constraint('LOCKED_TRACK', ref, name)

def add_stretch_to_constraint(ref = None, name = ""):
    return add_constraint('STRETCH_TO', ref, name)

def add_track_to_constraint(ref = None, name = ""):
    return add_constraint('TRACK_TO', ref, name)

def add_action_constraint(ref = None, name = ""):
    return add_constraint('ACTION', ref, name)

def add_armature_constraint(ref = None, name = ""):
    return add_constraint('ARMATURE', ref, name)

def add_child_of_constraint(ref = None, name = ""):
    return add_constraint('CHILD_OF', ref, name)

def add_floor_constraint(ref = None, name = ""):
    return add_constraint('FLOOR', ref, name)

def add_follow_path_constraint(ref = None, name = ""):
    return add_constraint('FOLLOW_PATH', ref, name)

def add_pivot_constraint(ref = None, name = ""):
    return add_constraint('PIVOT', ref, name)

def add_shrinkwrap_constraint(ref = None, name = ""):
    return add_constraint('SHRINKWRAP', ref, name)
#endregion
#region MODES
def set_mode(ref=None, newmode=None):
    if newmode is not None:
        objref = get_object(ref)
        bpy.context.view_layer.objects.active = objref
        bpy.ops.object.mode_set(mode=newmode)

def get_mode():
    return bpy.context.mode

def set_object_mode(ref=None):
    set_mode('OBJECT', ref)

def object_mode(ref=None):
    set_object_mode(ref)

def set_edit_mode(ref=None):
    set_mode('EDIT', ref)

def edit_mode(ref=None):
    set_edit_mode(ref)

def set_sculpt_mode(ref=None):
    set_mode('SCULPT', ref)

def sculpt_mode(ref=None):
    set_sculpt_mode(ref)

def set_vertex_paint_mode(ref=None):
    set_mode('VERTEX_PAINT', ref)

def vertex_paint_mode(ref=None):
    set_vertex_paint_mode(ref)

def set_weight_paint_mode(ref=None):
    set_mode('WEIGHT_PAINT', ref)

def weight_paint_mode(ref=None):
    set_weight_paint_mode(ref)

def set_texture_paint_mode(ref=None):
    set_mode('TEXTURE_PAINT', ref)

def texture_paint_mode(ref=None):
    set_texture_paint_mode(ref)
#endregion
#region SCENES
def get_scene():
    return bpy.context.scene
#endregion
#region VISIBILITY
def hide_object(ref=None):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_set(True)

def hide(ref = None):
    hide_object(ref)

def show_object(ref = None):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_set(False)

def show(ref = None):
    show_object(ref)

def unhide(ref = None):
    show_object(ref)

def unhide_object(ref = None):
    show_object(ref)

def hide_in_viewport(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_viewport = True

def show_in_viewport(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_viewport = False

def unhide_in_viewport(ref):
    show_in_viewport(ref)

def hide_in_render(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_render = True

def show_in_render(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.hide_render = False

def unhide_in_render(ref):
    show_in_render(ref)

def display_as_bounds(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.display_type = 'BOUNDS'

def display_as_textured(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.display_type = 'TEXTURED'

def display_as_solid(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.display_type = 'SOLID'

def display_as_wire(ref):
    objs = get_objects(ref)
    for obj in objs:
        obj.display_type = 'WIRE'
#endregion
#region TRANSFORMATIONS
def location(ref = None, loc = None):
    objref = get_object(ref)
    if loc is not None:
        objref.location = Vector((loc[0],loc[1],loc[2]))
    else:
        return objref.location

def rotation(ref = None, rot = None):
    objref = get_object(ref)
    if rot is not None:
        objref.rotation_euler = Vector((rot[0],rot[1],rot[2]))
    else:
        return objref.rotation_euler
            
def scale(ref = None, scale = None):
    objref = get_object(ref)
    if scale is not None:
        objref.scale = Vector((scale[0],scale[1],scale[2]))
    else:
        return objref.scale

# Applying Transformations:

def apply_location(ref = None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)

def apply_rotation(ref = None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

def apply_scale(ref = None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

def apply_all_transforms(ref = None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

def apply_rotation_and_scale(ref = None):
    if ref is not None:
        deselect_all_objects()
        select_object(ref)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

# Translations:

def translate_vector(vec = Vector(), ref = None):
    objs = make_obj_list(ref)
    for obj in objs:
        obj.location[0] += vec[0]
        obj.location[1] += vec[1]
        obj.location[2] += vec[2]

def translate_along_axis(val, axis, ref = None):
    objs = make_obj_list(ref)
    axis.normalize()
    for obj in objs:
        obj.location[0] += (val * axis[0])
        obj.location[1] += (val * axis[1])
        obj.location[2] += (val * axis[2])

def move_along_axis(val, axis, ref = None):
    translate_along_axis(val, axis, ref)

def translate_along_x(val, ref = None):
    translate_along_axis(val, Vector((1.0,0.0,0.0)), ref)

def move_along_x(val, ref = None):
    translate_along_x(val, ref)

def translate_along_y(val, ref = None):
    translate_along_axis(val, Vector((0.0,1.0,0.0)), ref)

def move_along_y(val, ref = None):
    translate_along_y(val, ref)

def translate_along_z(val, ref = None):
    translate_along_axis(val, Vector((0.0,0.0,1.0)), ref)

def move_along_z(val, ref = None):
    translate_along_z(val, ref)

def translate_along_global_x(val, ref = None):
    translate_along_x(val, ref)

def move_along_global_x(val, ref = None):
    translate_along_x(val, ref)

def translate_along_global_y(val, ref = None):
    translate_along_y(val, ref)

def move_along_global_y(val, ref = None):
    translate_along_y(val, ref)

def translate_along_global_z(val, ref = None):
    translate_along_z(val, ref)

def move_along_global_z(val, ref = None):
    translate_along_z(val, ref)

def translate_in_x(val, ref = None):
    translate_along_x(val, ref)

def move_in_x(val, ref = None):
    translate_along_x(val, ref)

def translate_in_y(val, ref = None):
    translate_along_y(val, ref)

def move_in_y(val, ref = None):
    translate_along_y(val, ref)

def translate_in_z(val, ref = None):
    translate_along_z(val, ref)

def move_in_z(val, ref = None):
    translate_along_z(val, ref)

def translate_along_local_axis(val, axis, ref = None):
    objs = make_obj_list(ref)
    axis.normalize()
    for obj in objs:
        tempaxis = axis.copy()
        tempaxis.rotate(obj.rotation_euler)
        obj.location[0] += (val * tempaxis[0])
        obj.location[1] += (val * tempaxis[1])
        obj.location[2] += (val * tempaxis[2])

def translate_along_local_x(val, ref = None):
    translate_along_local_axis(val, Vector((1.0,0.0,0.0)), ref)

def move_along_local_x(val, ref = None):
    translate_along_local_x(val, ref)

def translate_along_local_y(val, ref = None):
    translate_along_local_axis(val, Vector((0.0,1.0,0.0)), ref)

def move_along_local_y(val, ref = None):
    translate_along_local_y(val, ref)

def translate_along_local_z(val, ref = None):
    translate_along_local_axis(val, Vector((0.0,0.0,1.0)), ref)

def move_along_local_z(val, ref = None):
    translate_along_local_z(val, ref)

# Rotations:

def rotate_vector(vec = Vector(), ref = None):
    objs = make_obj_list(ref)
    for obj in objs:
        obj.rotation_euler[0] += vec[0]
        obj.rotation_euler[1] += vec[1]
        obj.rotation_euler[2] += vec[2]

def rotate_around_axis(deg, axis = Vector(), ref = None, point = None):
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pointref = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            pointref = get_cursor_location()
        else:
            pointref = get_median_point_of_objects(objs)
    else:
        pointref = point
    axis.normalize()
    for obj in objs:
        mat = (Matrix.Translation(pointref) @ Matrix.Rotation(math.radians(deg), 4, axis) @ Matrix.Translation(-pointref))
        obj.matrix_world = mat @ obj.matrix_world

def rotate_around_global_x(deg, ref = None, point = None):
    rotate_around_axis(deg, Vector((1.0,0.0,0.0)), ref, point)

def rotate_around_global_y(deg, ref = None, point = None):
    rotate_around_axis(deg, Vector((0.0,1.0,0.0)), ref, point)

def rotate_around_global_z(deg, ref = None, point = None):
    rotate_around_axis(deg, Vector((0.0,0.0,1.0)), ref, point)

def rotate_around_x(deg, ref = None,point = None):
    rotate_around_global_x(deg, ref, point)

def rotate_around_y(deg, ref = None,point = None):
    rotate_around_global_y(deg, ref, point)

def rotate_around_z(deg, ref = None,point = None):
    rotate_around_global_z(deg, ref, point)

def rotate_in_x(deg, ref = None,point = None):
    rotate_around_global_x(deg, ref, point)

def rotate_in_y(deg, ref = None,point = None):
    rotate_around_global_y(deg, ref, point)

def rotate_in_z(deg, ref = None,point = None):
    rotate_around_global_z(deg, ref, point)

def rotate_around_local_axis(deg, axis = Vector(), ref = None, point = None):
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pointref = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            pointref = get_cursor_location()
        else:
            pointref = get_median_point_of_objects(objs)
    else:
        pointref = point
    
    axis.normalize()
    for obj in objs:
        tempaxis = axis.copy()
        tempaxis.rotate(obj.rotation_euler)
        mat = (Matrix.Translation(pointref) @ Matrix.Rotation(math.radians(deg), 4, tempaxis) @ Matrix.Translation(-pointref))
        obj.matrix_world = mat @ obj.matrix_world

def rotate_around_local_x(deg, ref = None, point = None):
    rotate_around_local_axis(deg, Vector((1.0,0.0,0.0)), ref, point)

def rotate_around_local_y(deg, ref = None, point = None):
    rotate_around_local_axis(deg, Vector((0.0,1.0,0.0)), ref, point)

def rotate_around_local_z(deg, ref = None, point = None):
    rotate_around_local_axis(deg, Vector((0.0,0.0,1.0)), ref, point)

# Scaling:

def scale_vector(vec, ref = None):
    objs = make_obj_list(ref)
    for obj in objs:
        obj = get_object(ref)
        obj.scale[0] *= vec[0]
        obj.scale[1] *= vec[1]
        obj.scale[2] *= vec[2]

def scale_uniform(val, ref = None):
    scale_vector(Vector((val, val, val)), ref)

def scale_along_axis(val, axis, ref = None, point = None):
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pointref = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            pointref = get_cursor_location()
        else:
            pointref = get_median_point_of_objects(objs)
    else:
        pointref = point

    axis.normalize()
    temp = Vector()
    temp[0] = 1 + ((val - 1)/(1 - 0)) * (axis[0] - 0)
    temp[1] = 1 + ((val - 1)/(1 - 0)) * (axis[1] - 0)
    temp[2] = 1 + ((val - 1)/(1 - 0)) * (axis[2] - 0)
    for obj in objs:
        obj.scale[0] *= temp[0]
        obj.scale[1] *= temp[1]
        obj.scale[2] *= temp[2]
        
        tempaxis = axis.copy()
        tempaxis.rotate(obj.rotation_euler)
        fac = (obj.location - pointref).dot(tempaxis) * (val-1)
        translate_along_axis(fac, tempaxis, obj)

def scale_along_x(val, ref = None, point = None):
    scale_along_axis(val, Vector((1.0, 0.0, 0.0)), ref, point)

def scale_along_y(val, ref = None, point = None):
    scale_along_axis(val, Vector((0.0, 1.0, 0.0)), ref, point)

def scale_along_z(val, ref = None, point = None):
    scale_along_axis(val, Vector((0.0, 0.0, 1.0)), ref, point)

def scale_along_local_x(val, ref = None, point = None):
    scale_along_axis(val, Vector((1.0, 0.0, 0.0)), ref, point)

def scale_along_local_y(val, ref = None, point = None):
    scale_along_axis(val, Vector((0.0, 1.0, 0.0)), ref, point)

def scale_along_local_z(val, ref = None, point = None):
    scale_along_axis(val, Vector((0.0, 0.0, 1.0)), ref, point)

def scale_in_x(val, ref = None, point = None):
    scale_along_axis(val, Vector((1.0, 0.0, 0.0)), ref, point)

def scale_in_y(val, ref = None, point = None):
    scale_along_axis(val, Vector((0.0, 1.0, 0.0)), ref, point)

def scale_in_z(val, ref = None, point = None):
    scale_along_axis(val, Vector((0.0, 0.0, 1.0)), ref, point)

def scale_along_global_axis(val, axis, ref = None, point = None):
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            point = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            point = get_cursor_location()
        else:
            point = get_median_point_of_objects(objs)
    else:
        pointref = point
    for obj in objs:
        loc, rot, scale = obj.matrix_world.decompose()
        loc_mat = Matrix.Translation(loc)
        new_loc_mat = loc_mat.copy()
        new_loc_mat.invert()
        obj.matrix_world = new_loc_mat @ obj.matrix_world
        orig_rot = obj.rotation_euler.copy()
        orig_loc = obj.location
        obj.matrix_world = Matrix.Scale(val, 4, axis) @ obj.matrix_world
        obj.matrix_world = loc_mat @ obj.matrix_world
        obj.rotation_euler = orig_rot
        fac = (obj.location - point).dot(axis) * (val-1)
        translate_along_axis(fac, axis, obj)

def scale_along_global_x(val, ref = None, point = None):
    scale_along_global_axis(val, Vector((1.0, 0.0, 0.0)), ref, point)

def scale_along_global_y(val, ref = None, point = None):
    scale_along_global_axis(val, Vector((0.0, 1.0, 0.0)), ref, point)

def scale_along_global_z(val, ref = None, point = None):
    scale_along_global_axis(val, Vector((0.0, 0.0, 1.0)), ref, point)

#Need to be revised, not working as expected
def scale_perpendicular_to_x(val, ref = None, point = None):
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pointref = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            pointref = get_cursor_location()
        else:
            pointref = get_median_point_of_objects(objs)
    else:
        pointref = point
    
    for obj in objs:
        scale_vector(Vector((1.0, val, val)), obj)
        axis = (obj.location - pointref) * Vector((0.0, 1.0, 1.0))
        fac = axis.magnitude * (val-1)
        translate_along_axis(fac, axis, obj)

def scale_perpendicular_to_y(val, ref = None, point = None):
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pointref = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            pointref = get_cursor_location()
        else:
            pointref = get_median_point_of_objects(objs)
    else:
        pointref = point
    
    for obj in objs:
        scale_vector(Vector((val, 1.0, val)), obj)
        axis = (obj.location - pointref) * Vector((1.0, 0.0, 1.0))
        fac = axis.magnitude * (val-1)
        translate_along_axis(fac, axis, obj)

def scale_perpendicular_to_z(val, ref = None, point = None):
    objs = make_obj_list(ref)
    pointref = None
    if point is None:
        if get_scene().tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pointref = get_median_point_of_objects(objs)
        elif get_scene().tool_settings.transform_pivot_point == 'CURSOR':
            pointref = get_cursor_location()
        else:
            pointref = get_median_point_of_objects(objs)
    else:
        pointref = point
    
    for obj in objs:
        scale_vector(Vector((val, val, 1.0)), obj)
        axis = (obj.location - pointref) * Vector((1.0, 1.0, 0.0))
        fac = axis.magnitude * (val-1)
        translate_along_axis(fac, axis, obj)

#endregion
#region ANIMATION / KEYFRAMES
# Example: path is the object and property is 'location'
def add_keyframe(path, property, frame = None):
    if frame is None:
        frame = current_frame()
    path.keyframe_insert(data_path=property,frame=frame)
    keyframes = []
    for i in range(len(path.animation_data.action.fcurves)):
        fcurve = path.animation_data.action.fcurves.find(property,index=i)
        if fcurve is not None:
            for keyframe in fcurve.keyframe_points:
                if keyframe.co[0] == frame:
                    keyframes.append(keyframe)
    
    # Updating Interface:
    for area in bpy.context.screen.areas:
        area.tag_redraw()
        
    return keyframes if len(keyframes) > 1 else keyframes[0] 
    
def remove_keyframe(keyframes):
    if type(keyframes) is not list:
        keyframes = [keyframes]
    for keyframe in keyframes:
        fcurves = keyframe.id_data.fcurves
        for fcurve in fcurves:    
            for keyframe1 in fcurve.keyframe_points:
                if keyframe1 == keyframe:
                    fcurve.keyframe_points.remove(keyframe)
            if len(fcurve.keyframe_points) == 0:
                fcurves.remove(fcurve)

        # Updating Interface:
        for area in bpy.context.screen.areas:
            area.tag_redraw()
#endregion
#region DRIVERS

def add_driver(path,property,index=-1):
    fcurves = path.driver_add(property,index)
    for area in bpy.context.screen.areas:   #update interface
        area.tag_redraw()
    if type(fcurves) is list:
        return [fcurve.driver for fcurve in fcurves]
    return fcurves.driver

def remove_driver(driver):
    for fcurve in driver.id_data.animation_data.drivers: 
        if fcurve.driver == driver:
            driver.id_data.animation_data.drivers.remove(fcurve)

#endregion
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
    return bpy.context.scene.cursor.location

def set_cursor_location(newloc):
    bpy.context.scene.cursor.location = newloc

def get_cursor_rotation():
    return bpy.context.scene.cursor.rotation_euler

def get_cursor_rotation_mode():
    return bpy.context.scene.cursor.rotation_mode

#endregion
#region PIVOT POINT
def set_pivot_point_to_cursor():
    get_scene().tool_settings.transform_pivot_point = 'CURSOR'

def set_pivot_point_to_median():
    get_scene().tool_settings.transform_pivot_point = 'MEDIAN_POINT'

def set_pivot_point_to_individual_origins():
    get_scene().tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'

def set_pivot_point_to_active_element():
    get_scene().tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

def set_pivot_point_to_bounding_box_center():
    get_scene().tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'
#endregion
#region ORIGINS
def set_geometry_to_origin(ref = None):
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

def geometry_to_origin(ref = None):
    set_geometry_to_origin(ref)

def set_origin_to_geometry(ref = None):
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

def origin_to_geometry(ref = None):
    set_origin_to_geometry(ref)

def set_origin_to_cursor(ref = None):
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

def origin_to_cursor(ref = None):
    set_origin_to_cursor(ref)

def set_origin_to_centermass_surface(ref = None):
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

def origin_to_centermass_surface(ref = None):
    set_origin_to_centermass_surface(ref)

def set_origin_to_centermass_volume(ref = None):
    objref = get_object(ref)
    if objref is not None:
        select_object(objref)
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')

def origin_to_centermass_volume(ref = None):
    set_origin_to_centermass_volume(ref)
#endregion
#region SHADING
def shade_object_smooth(ref = None):
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

def shade_smooth(ref = None):
    shade_object_smooth(ref)

def shade_object_flat(ref = None):
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

def shade_flat(ref = None):
    shade_object_flat(ref)

def set_smooth_angle(ref, degrees = 60):
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    if objref.data.use_auto_smooth == False:
        objref.data.use_auto_smooth = True
    objref.data.auto_smooth_angle = radians(degrees)
#endregion
#region LIGHTING
def get_light(ref):
    obj = get_object(ref)
    return obj.data

def light_power(val = 0, ref = None):
    objlist = []
    if ref is None:
        objlist = so()
    else:
        objlist = [ref]
    for o in objlist:
        o.data.energy = val

def light_intensity(val = 0, ref = None):
    light_power(val,ref)

def light_power_add(val = 0, ref = None):
    objlist = []
    if ref is None:
        objlist = so()
    else:
        objlist = [ref]
    for o in objlist:
        o.data.energy += val

def light_intensity_add(val = 0, ref = None):
    light_power_add(val,ref)

def light_power_multiply(val = 0, ref = None):
    objlist = []
    if ref is None:
        objlist = so()
    else:
        objlist = [ref]
    for o in objlist:
        o.data.energy *= val

def light_intensity_multiply(val = 0, ref = None):
    light_power_multiply(val,ref)
#endregion
#region MESHES
# Creates a mesh - (string) name
def create_mesh(name):
    return bpy.data.meshes.new(name)

def get_all_meshes():
    return bpy.data.meshes

def get_vertices(ref):
    if is_string(ref):
        return get_object(ref).data.vertices
    else:
        return ref.data.vertices

def get_edges(ref):
    if is_string(ref):
        return get_object(ref).data.edges
    else:
        return ref.data.edges

def get_faces(ref):
    return get_polygons(ref)

def get_polygons(ref):
    if is_string(ref):
        return get_object(ref).data.polygons
    else:
        return ref.data.polygons

def get_mesh_from_object(ref):
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    return objref.data
#endregion
#region VERTEX GROUPS
''' FUTURE UPDATE
def create_vertex_group(ref, group_name):
    ref.vertex_groups.new(name=group_name)
    return ref.vertex_groups[group_name]

def delete_vertex_group(ref, group_name):
    pass
'''
#endregion
#region COLLECTIONS
def create_collection(name):
    if not collection_exists(name):
        bpy.data.collections.new(name)
        colref = bpy.data.collections[name]
        bpy.context.scene.collection.children.link(colref)
        return colref
    return False

def delete_collection(col, delete_objects = False):
    colref = None
    if is_string(col):
            colref = get_collection(col)
    else:
        colref = col

    if delete_objects:
        deselect_all_objects()
        if len(colref.objects) > 0:
            for co in colref.objects:
                co.select_set(True)
            delete_selected_objects()
    else:
        deselect_all_objects()
        if len(colref.objects) > 0:
            for co in colref.objects:
                bpy.context.scene.collection.objects.link(co)

    bpy.data.collections.remove(colref)

def delete_objects_in_collection(col):
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
    for co in colref.children:
        if isinstance(co, bpy.types.Collection):
            delete_hierarchy(co)
    deselect_all_objects()
    delete_objects_in_collection(colref)
    delete_collection(colref)

def duplicate_collection(col):
    colref = None
    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col
    new_name = "Copy of " + colref.name
    new_col = create_collection(new_name)
    to_copy = get_objects_from_collection(colref.name)
    for o in to_copy:
        copy_object(o,new_col)
    return get_collection(new_name)

def get_objects_from_collection(col):
    if is_string(col):
        return bpy.data.collections[col].objects
    else:
        return col.objects

def get_collection(ref = None):
    if ref is None:
        return bpy.context.view_layer.active_layer_collection.collection
    else:
        if is_string(ref):
            if ref in bpy.data.collections:
                return bpy.data.collections[ref]
            else:
                return False
        else:
            return ref

def get_col(ref = None):
    return get_collection(ref)

def get_active_collection():
    return bpy.context.view_layer.active_layer_collection.collection

def set_active_collection(ref):
    colref = None
    if is_string(ref):
        colref = get_collection(ref)
    else:
        colref = ref
    hir = bpy.context.view_layer.layer_collection
    search_layer_collection_in_hierarchy_and_set_active(colref, hir)

# Dev Function
def search_layer_collection_in_hierarchy_and_set_active(colref, hir) :
    if isinstance(hir, bpy.types.LayerCollection):
        if hir.collection == colref:
            bpy.context.view_layer.active_layer_collection = hir
        else:
            for child in hir.children:
                search_layer_collection_in_hierarchy_and_set_active(colref, child)

def get_all_collections():
    return bpy.data.collections

def get_list_of_collections():
    return get_all_collections()

def link_object_to_collection(ref, col):
    if is_string(col):
        objref = get_object(ref)
        bpy.data.collections[col].objects.link(objref)
    else:
        # Check for bad return argument
        if isinstance(col, bool)!=True:
            objref = get_object(ref)
            col.objects.link(objref)

def link_objects_to_collection(ref, col):
    objs = get_objects(ref)
    if is_string(col):
        for o in objs:
            bpy.data.collections[col].objects.link(o)
    else:
        for o in objs:
            col.objects.link(o)

def unlink_object_from_collection(ref, col):
    if is_string(col):
        objref = get_object(ref)
        bpy.data.collections[col].objects.unlink(objref)
    else:
        objref = get_object(ref)
        col.objects.unlink(objref)

def unlink_objects_from_collection(ref, col):
    objs = get_objects(ref)
    colref = None
    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col
    for o in objs:
        colref.objects.unlink(o)

def move_object_to_collection(ref, col):
    objref = get_object(ref)
    colref = None
    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col

    cols = objref.users_collection
    for c in cols:
        c.objects.unlink(objref)
    link_object_to_collection(objref, colref)

def move_objects_to_collection(ref, col):
    objs = get_objects(ref)
    colref = None
    if is_string(col):
        colref = get_collection(col)
    else:
        colref = col
    for o in objs:
        for c in o.users_collection:
            c.objects.unlink(o)
        link_object_to_collection(o, colref)

def get_object_collection(ref):
    objref = get_object(ref)
    return objref.users_collection[0]

def get_object_collections(ref):
    objref = get_object(ref)
    return objref.users_collection

def collection_exists(col):
    if is_string(col):
        return col in bpy.data.collections
    return col.name in bpy.data.collections

#endregion
#region MATERIALS
def create_material(name):
    return bpy.data.materials.new(name)

def material_exists(ref):
    if is_string(ref):
        return ref in bpy.data.materials
    # safety
    return ref.name in bpy.data.materials

def delete_material(ref):
    matref = None
    if is_string(ref):
        matref = get_material(ref)
    else:
        matref = ref
    bpy.data.materials.remove(matref)

def get_material(matname = None):
    if matname is None:
        active = ao()
        if len(active.material_slots) > 0:
            return active.material_slots[0].material
    else:
        for m in bpy.data.materials:
            if m.name == matname:
                return m

def add_material_to_object(ref, mat):
    objref = None
    matref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref
    
    if is_string(mat):
        matref = get_material(mat)
    else:
        matref = mat

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

def remove_materials(ref = None):
    objrefs = get_objects(ref)
    for o in objrefs:
        if len(o.material_slots) > 0:
            names = []
            for m in o.material_slots:
                names.append(m.name)
            for n in names:
                remove_material_from_object(o,n)
                
def remove_all_materials(ref = None):
    remove_materials(ref)

def remove_unused_material_slots(ref = None):
    objrefs = get_objects(ref)
    for o in objrefs:
        data = o.data
        tmp = data.materials.items()
        data.materials.clear()
        for item in tmp:
            data.materials.append(item[1])

def remove_unused_slots(ref = None):
    remove_unused_material_slots(ref)

def get_all_materials():
    return bpy.data.materials

def get_materials(ref = None):
    if ref is not None:
        get_materials_from_object(ref)
    else:
        return bpy.data.materials

def get_material_from_object(ref):
    objref = get_object(ref)
    return objref.material_slots[0].material

def get_materials_from_object(ref):
    objref = get_object(ref)
    mat_list = []
    mats = objref.material_slots
    for m in mats:
        mat_list.append(m.material)
    return mat_list

def get_material_names_from_object(ref):
    objref = get_object(ref)
    name_list = []
    mats = objref.material_slots
    for m in mats:
        name_list.append(m.name)
    return name_list
#endregion
#region NODES
def set_material_use_nodes(matref, value):
    matref.use_nodes = value

def set_material_to_use_nodes(matref=None, value=None):
    set_material_use_nodes(matref,value)

def get_material_nodes(ref):
    mat = get_material(ref)
    return mat.node_tree.nodes

def get_node(nodes,ref):
    if is_string(ref):
        for n in nodes:
            if n.name == ref:
                return n
    else:
        return ref

def get_nodes(mat):
    return mat.node_tree.nodes

def get_node_tree(matref):
    matref.use_nodes = True
    return matref.node_tree

def create_node(nodes, nodetype):
    return nodes.new(type=nodetype)

def delete_node(nodes, ref):
    noderef = get_node(nodes, ref)
    if noderef is not None:
        nodes.remove(noderef)

def get_node_links(matref):
    return matref.node_tree.links

def create_node_link(point1, point2):
    links = point1.id_data.links
    return links.new(point1,point2)

def create_link(point1 = None, point2 = None):
    return create_node_link(point1, point2)

def get_index_of_output(node, name):
    index = None
    i = 0
    while i < len(node.outputs):
        if node.outputs[i].name == name:
            index = i
        i += 1
    return index

def get_index_of_input(node, name):
    index = None
    i = 0
    while i < len(node.inputs):
        if node.inputs[i].name == name:
            index = i
        i += 1
    return index

# World Nodes
def get_world_nodes(index=None):
    if index is not None:
        return bpy.data.worlds[index].node_tree.nodes
    else:
        return bpy.data.worlds[0].node_tree.nodes

#endregion
#region TEXTURES AND IMAGES
def create_texture(name="Texture", type='CLOUDS'):
    if type is not None:
        return bpy.data.textures.new(name, type.upper())
    
def get_texture(ref):
    if is_string(ref):
        if ref in bpy.data.textures:
            return bpy.data.textures[ref]
    else:
        return ref

def get_all_textures():
    return bpy.data.textures

def get_list_of_textures():
    return get_all_textures()

def rename_texture(ref, name):
    texref = get_texture(ref)
    if name is not None:
        texref.name = name

def delete_texture(ref):
    if is_string(ref):
        bpy.data.textures.remove(get_texture(ref))
    else:
        bpy.data.textures.remove(ref)

def create_image(name = 'Image', width = 1024, height = 1024):
    return bpy.data.images.new(name = name, width = width, height = height)

def get_image(ref):
    if is_string(ref):
        if ref in bpy.data.images:
            return bpy.data.images[ref]
    else:
        return ref

def get_all_images():
    return bpy.data.images

def get_list_of_images():
    return get_all_images()

def rename_image(ref, name):
    imgref = get_image(ref)
    if name is not None:
        imgref.name = name

def delete_image(ref):
    if is_string(ref):
        bpy.data.images.remove(get_image(ref))
    else:
        bpy.data.images.remove(ref)

#endregion
#region MODIFIERS 
def add_modifier(ref = None, name = "Modifier", id="SUBSURF"):
    objrefs = get_objects(ref)
    new_mods = []
    for o in objrefs:
        new_mod = o.modifiers.new(name, id)
        new_mods.append(new_mod)

    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            area.tag_redraw()
    
    if len(new_mods)>1:
        return new_mods
    else:
        return new_mods[0]

def get_modifier(ref, name):
    objref = get_object(ref)

    # we assume name is string
    if name in objref.modifiers:
        return objref.modifiers[name]
    else:
        return False

def remove_modifier(ref = None, name = None):
    objref = get_object(ref)
    if name is not None:
        if is_string(name):
            if name in objref.modifiers:
                mod = get_modifier(objref,name)
                objref.modifiers.remove(mod)
        else:
            objref.modifiers.remove(name)
    else:
        objref.modifiers.remove(objref.modifiers[0])
    
    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            area.tag_redraw()

def remove_modifiers(ref = None):
    objref = get_objects(ref)
    for o in objref:
        for m in o.modifiers:
            o.modifiers.remove(m)

def remove_all_modifiers(ref = None):
    remove_modifiers(ref)

def apply_all_modifiers(ref = None):
    objref = get_object(ref)
    select_object(objref)
    for mod in objref.modifiers:
        bpy.ops.object.modifier_apply(modifier=mod.name)

def apply_modifiers(ref = None):
    apply_all_modifiers(ref)

# Specific Modifiers
def add_data_transfer(ref=None, modname = "DataTransfer"):
    return add_modifier(ref,modname,'DATA_TRANSFER')

def add_mesh_cache(ref=None, modname = "MeshCache"):
    return add_modifier(ref,modname,'MESH_CACHE')

def add_mesh_sequence_cache(ref=None, modname = "MeshSequenceCache"):
    return add_modifier(ref,modname,'MESH_SEQUENCE_CACHE')

def add_normal_edit(ref=None, modname = "NormalEdit"):
    return add_modifier(ref,modname,'NORMAL_EDIT')

def add_weighted_normal(ref=None, modname = "WeightedNormal"):
    return add_modifier(ref,modname,'WEIGHTED_NORMAL')

def add_uv_project(ref=None, modname = "UVProject"):
    return add_modifier(ref,modname,'UV_PROJECT')

def add_uv_warp(ref=None, modname = "Warp"):
    return add_modifier(ref,modname,'UV_WARP')

def add_vertex_weight_edit(ref=None, modname = "VertexWeightEdit"):
    return add_modifier(ref,modname,'VERTEX_WEIGHT_EDIT')

def add_vertex_weight_mix(ref=None, modname = "VertexWeightMix"):
    return add_modifier(ref,modname,'VERTEX_WEIGHT_MIX')

def add_vertex_weight_proximity(ref=None, modname = "VertexWeightProximity"):
    return add_modifier(ref,modname,'VERTEX_WEIGHT_PROXIMITY')

def add_array(ref=None, modname = "Array"):
    return add_modifier(ref,modname,'ARRAY')

def add_bevel(ref=None, modname = "Bevel"):
    return add_modifier(ref,modname,'BEVEL')

def add_boolean(ref=None, modname = "Boolean"):
    return add_modifier(ref,modname,'BOOLEAN')

def add_build(ref=None, modname = "Build"):
    return add_modifier(ref,modname,'BUILD')

def add_decimate(ref=None, modname = "Decimate"):
    return add_modifier(ref,modname,'DECIMATE')

def add_edge_split(ref=None, modname = "EdgeSplit"):
    return add_modifier(ref,modname,'EDGE_SPLIT')

def add_mask(ref=None, modname = "Mask"):
    return add_modifier(ref,modname,'MASK')

def add_mirror(ref=None, modname = "Mirror"):
    return add_modifier(ref,modname,'MIRROR')

def add_multires(ref=None, modname = "Multires"):
    return add_modifier(ref,modname,'MULTIRES')

def add_remesh(ref=None, modname = "Remesh"):
    return add_modifier(ref,modname,'REMESH')

def add_screw(ref=None, modname = "Screw"):
    return add_modifier(ref,modname,'SCREW')

def add_skin(ref=None, modname = "Skin"):
    return add_modifier(ref,modname,'SKIN')

def add_solidify(ref=None, modname = "Solidify"):
    return add_modifier(ref,modname,'SOLIDIFY')

def add_subsurf(ref=None, modname = "Subsurf"):
    return add_modifier(ref,modname,'SUBSURF')

def add_triangulate(ref=None, modname = "Triangulate"):
    return add_modifier(ref,modname,'TRIANGULATE')

def add_weld(ref=None, modname = "Weld"):
    return add_modifier(ref,modname,'WELD')

def add_wireframe(ref=None, modname = "Wireframe"):
    return add_modifier(ref,modname,'WIREFRAME')

def add_armature(ref=None, modname = "Armature"):
    return add_modifier(ref,modname,'ARMATURE')

def add_cast(ref=None, modname = "Cast"):
    return add_modifier(ref,modname,'CAST')

def add_curve(ref=None, modname = "Curve"):
    return add_modifier(ref,modname,'CURVE')

def add_displace(ref=None, modname = "Displace"):
    return add_modifier(ref,modname,'DISPLACE')

def add_hook(ref=None, modname = "Hook"):
    return add_modifier(ref,modname,'HOOK')

def add_laplacian_deform(ref=None, modname = "LaplacianDeform"):
    return add_modifier(ref,modname,'LAPLACIANDEFORM')

def add_lattice(ref=None, modname = "Lattice"):
    return add_modifier(ref,modname,'LATTICE')

def add_mesh_deform(ref=None, modname = "Deform"):
    return add_modifier(ref,modname,'MESH_DEFORM')

def add_shrinkwrap(ref=None, modname = "Shrinkwrap"):
    return add_modifier(ref,modname,'SHRINKWRAP')

def add_simple_deform(ref=None, modname = "SimpleDeform"):
    return add_modifier(ref,modname,'SIMPLE_DEFORM')

def add_smooth(ref=None, modname = "Smooth"):
    return add_modifier(ref,modname,'SMOOTH')

def add_corrective_smooth(ref=None, modname = "CorrectiveSmooth"):
    return add_modifier(ref,modname,'CORRECTIVE_SMOOTH')

def add_laplacian_smooth(ref=None, modname = "LaplacianSmooth"):
    return add_modifier(ref,modname,'LAPLACIANSMOOTH')

def add_surface_deform(ref=None, modname = "SurfaceDeform"):
    return add_modifier(ref,modname,'SURFACE_DEFORM')

def add_warp(ref=None, modname = "Warp"):
    return add_modifier(ref,modname,'WARP')

def add_wave(ref=None, modname = "Wave"):
    mod = add_modifier(ref,modname,'WAVE')
    mod.time_offset = random.random() * get_scene().render.fps
    return mod

def add_cloth(ref=None, modname = "Cloth"):
    return add_modifier(ref,modname,'CLOTH')

def add_collision(ref=None, modname = "Collision"):
    return add_modifier(ref,modname,'COLLISION')

def add_dynamic_paint(ref=None, modname = "DynamicPaint"):
    return add_modifier(ref,modname,'DYNAMIC_PAINT')

def add_explode(ref=None, modname = "Explode"):
    return add_modifier(ref,modname,'EXPLODE')

def add_fluid(ref=None, modname = "Fluid"):
    return add_modifier(ref,modname,'FLUID')

def add_ocean(ref=None, modname = "Ocean"):
    return add_modifier(ref,modname,'OCEAN')

def add_particle_instance(ref=None, modname = "ParticleInstance"):
    return add_modifier(ref,modname,'PARTICLE_INSTANCE')

def add_particle_system(ref=None, modname = "ParticleSystem"):
    return add_modifier(ref,modname,'PARTICLE_SYSTEM')

def add_soft_body(ref=None, modname = "SoftBody"):
    return add_modifier(ref,modname,'SOFT_BODY')

def add_surface(ref=None, modname = ""):
    return add_modifier(ref,modname,'SURFACE')

def add_simulation(ref=None, modname = ""):
    return add_modifier(ref,modname,'SIMULATION')
#endregion
#region PHYSICS
def add_force_field_physics(ref=None):
    objref = get_object(ref)
    bpy.context.view_layer.objects.active = objref
    if objref.field.type == 'NONE':
        bpy.ops.object.forcefield_toggle()

def add_collision_physics(ref=None):
    add_collision(ref)

def add_cloth_physics(ref=None):
    add_cloth(ref)

def add_dynamic_paint_physics(ref=None):
    add_dynamic_paint(ref)

def add_soft_body_physics(ref=None):
    add_soft_body(ref)

def add_fluid_physics(ref=None):
    add_fluid(ref)

def add_rigid_body_physics(ref=None):
    objref = get_object(ref)
    bpy.context.view_layer.objects.active = objref
    bpy.ops.rigidbody.object_add()

def add_rigid_body_constraint_physics(ref=None):
    objref = get_object(ref)
    bpy.context.view_layer.objects.active = objref
    bpy.ops.rigidbody.constraint_add()
#endregion
#region PHYSICS - FLUIDS

def set_fluid_type(fluidtype = None):
    ftype = bpy.context.object.modifiers["Fluid"].fluid_type
    if fluidtype is not None:
        if fluidtype == "NONE":
            ftype = "NONE"
        if fluidtype == "DOMAIN":
            ftype = "DOMAIN"
        if fluidtype == "FLOW":
            ftype = "FLOW"
        if fluidtype == "EFFECTOR":
            ftype = "EFFECTOR"
    else:
        ftype = "NONE"

# Effector Parameters 
def fluid_effector_type(type):
    bpy.context.object.modifiers["Fluid"].effector_settings.effector_type = type

def fluid_effector_subsample_value(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.subframes = intvalue

def fluid_effector_thickness_value(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.surface_distance = intvalue

# Use effector, 1 = on 0 = off
def fluid_effector_use_toggle(fbool):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].effector_settings.use_effector = h

# Is Planar, 1 = on 0 = off
def fluid_effector_is_planar(fbool):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].effector_settings.use_plane_init = h

def fluid_effector_velocity(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.velocity_factor = intvalue

def fluid_effector_guide_mode(value):
    if value == 'MAXIMUM' or value == 'MAX':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'MAXIMUM'
    if value == 'MINIMUM' or value == 'MIN':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'MINIMUM'
    if value == 'OVERRIDE' or value == 'OVER':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'OVERRIDE'
    if value == 'AVERAGED' or value == 'MEAN':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'AVERAGED'

# Type Flow Parameters
def fluid_set_flow_type(flowtype = None):
    ftype = bpy.context.object.modifiers["Fluid"].flow_settings.flow_type
    if flowtype is not None:
        if flowtype == "SMOKE":
            ftype = "SMOKE"
        if flowtype == "FIRE":
            ftype = "FIRE"
        if flowtype == "LIQUID" or flowtype == "FLUID":
            ftype = "LIQUID"
        if flowtype == "SMOKE_FIRE" or flowtype == "FIRE_SMOKE" or flowtype == "BOTH":
            ftype = "BOTH"
    else:
        ftype = "LIQUID"

def flow_set_behavior(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_behavior = value

def flow_use_flow_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_inflow = h

def flow_source(value):
    if value == 'PARTICLE SYSTEM':
        value = 'PARTICLES'
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_source = value

def flow_smoke_colour_rgb(r,g,b):
    print(r+g+b)
    rfloat = float(r)
    gfloat = float(g)
    bfloat = float(b)
    bpy.context.object.modifiers["Fluid"].flow_settings.smoke_color = (rfloat,gfloat,bfloat)

def flow_absolute_density(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_absolute = bool

def flow_initial_temp(value):
    temp = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.temperature = temp

def flow_density(value):
    density = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.density = density

def flow_vertexgroup(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.density_vertex_group = value

# Particle System
def flow_particle_system_select(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.particle_system = bpy.data.objects["Cube"].particle_systems[value]

def flow_particle_set_size_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_particle_size = h

def flow_set_particle_size(value):
    size = float(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.particle_size = size

# Intial Velocity
def flow_initial_velocity_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_initial_velocity = h

def flow_initial_velocity_value(value):
    velocity = float(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.velocity_factor = velocity

# Domains
def fluid_set_domain_type(domaintype = None):
    dtype = bpy.context.object.modifiers["Fluid"].domain_settings.domain_type
    if domaintype is not None:
        if domaintype == "GAS":
            dtype = "GAS"
        if domaintype == "LIQUID":
            dtype = "LIQUID"
    else:
        dtype = "LIQUID"

# Global Fluid Settings
def fluid_domain_set_resolution(value):
    res = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.resolution_max = res

def fluid_domain_time_scale(value):
    timespeed = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.time_scale = timespeed

def fluid_domain_set_cfl(value):
    CFL = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cfl_condition = CFL

def fluid_domain_set_timesteps_max(value):
    timestep = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.timesteps_max = timestep

def fluid_domain_set_timesteps_min(value):
    timestep = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.timesteps_min = timestep

# Border Collisions
def fluid_domain_border_colisions(side,toggle):
    bool = int(toggle)
    if side == 'top' or side == 'TOP':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_top = bool
    if side == 'back' or side == 'BACK':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_back = bool
    if side == 'front' or side == 'FRONT':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_front = bool
    if side == 'right' or side == 'RIGHT':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_right = bool
    if side == 'left' or side == 'LEFT':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_left = bool
    if side == 'bottom' or side == 'BOTTOM':
        bpy.context.object.modifiers["Fluid"].domain_settings.use_collision_border_bottom = bool

# Caches      
def fluid_domain_cache_folder(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_directory = value

def fluid_simulation_start(value):
    start = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_frame_start = start

def fluid_simulation_end(value):
    end = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_frame_end = end

def fluid_simulation_offset(value):
    end = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_frame_offset = end

def fluid_cache_type(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_type = value
    #use REPLAY, MODULAR, and ALL

def fluid_cache_continue_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.cache_resumable = h

def fluid_cache_format(value):
    if value.lower() == 'openvdb':
        bpy.context.object.modifiers["Fluid"].domain_settings.cache_data_format = 'OPENVDB'
    if value.lower() == 'uni cache':
        bpy.context.object.modifiers["Fluid"].domain_settings.cache_data_format = 'UNI'

def fluid_cache_compress_type(value):
    if value.lower() == 'zip':
        bpy.context.object.modifiers["Fluid"].domain_settings.openvdb_cache_compress_type = 'ZIP'
    if value.lower() == 'blosc':
        bpy.context.object.modifiers["Fluid"].domain_settings.openvdb_cache_compress_type = 'BLOSC'
    if value.lower() == 'none':
        bpy.context.object.modifiers["Fluid"].domain_settings.openvdb_cache_compress_type = 'NONE'

def fluid_cache_precision(value):
    print(value)
    if value.lower() == 'half':
        value = "16"
    if value.lower() == 'full':
        value = "32"
    bpy.context.object.modifiers["Fluid"].domain_settings.openvdb_data_depth = value

#Collections 
def fluid_flow_collection(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.fluid_group = bpy.data.collections[value]

def fluid_flow_effectorn(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_group = bpy.data.collections[value]

#Guides
def fluid_domain_guides_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_guide = h

def fluid_domain_guide_weight(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.guide_alpha = val

def fluid_domain_guides_size(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.guide_beta = val

def fluid_domain_guides_velocity(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.guide_vel_factor = val

def fluid_domain_guides_source(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.guide_source = value.upper()

# Field Weights
def fluid_field_weights_collection(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.collection = bpy.data.collections[value]

def fluid_field_weights_gravity(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.gravity = val

def fluid_field_weights_all(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.all = val

def fluid_field_weights_force(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.force = val

def fluid_field_weights_vortex(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.vortex = val

def fluid_field_weights_magnetic(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.magnetic = val

def fluid_field_weights_harmonic(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.harmonic = val

def fluid_field_weights_charge(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.charge = val

def fluid_field_weights_lennardjones(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.lennardjones = val

def fluid_field_weights_wind(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.wind = val

def fluid_field_weights_curve_guide(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.curve_guide = val

def fluid_field_weights_texture(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.texture = val

def fluid_field_weights_smoke_flow(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.smokeflow = val

def fluid_field_weights_turbulence(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.turbulence = val

def fluid_field_weights_drag(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.drag = val

def fluid_field_weights_boid(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.effector_weights.boid = val

# Viewport Display
def fluid_view_thickness(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.display_thickness = val

def fluid_view_interpolation(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.display_interpolation = value.upper()

def fluid_view_slices_voxel(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.slice_per_voxel = val

def fluid_view_slice_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_slice =h

def fluid_view_slice_axis(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.slice_axis = value.upper

def fluid_view_slice_position(value):
    boolean = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.slice_depth = boolean 

def fluid_view_grid_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_color_ramp = h

def fluid_view_grid_scale(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.color_ramp_field_scale = val

def fluid_view_grid_color_position(pos,stop):
    val = float(pos)
    position = int(stop)
    C.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements[position].position= val

def fluid_view_grid_color_hue_interpolation(value):
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.hue_interpolation = value.upper()

def fluid_view_grid_color(stop,encoding,r,g,b,al):
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.color_mode = encoding.upper()
    stopint = int(stop)
    red = float(r)
    green = float(b)
    blue = float(g)
    alpha = float(al)
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements[stopint].color = (red,green,blue,alpha)

def fluid_view_grid_stops_new(value):
    val = float(value)
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements.new(val)

def fluid_view_grid_stops_remove(value):
    val = int(value)
    bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements.remove( bpy.context.active_object.modifiers["Fluid"].domain_settings.color_ramp.elements[val] )

def fluid_view_vector_dis_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_slice = h

def fluid_view_vector_display_type(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.vector_display_type = value.upper()

def fluid_view_vector_magnitude(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.vector_scale_with_magnitude = val

def fluid_view_vector_field(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.vector_field = value.upper()

def fluid_view_vector_scale(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.vector_scale = val

# Gas Domain (not categorized)
def fluid_gas_buoyancy_density(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.alpha = val

def fluid_gas_buoyancy_heat(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.beta = val

def fluid_gas_buoyancy_vorticity(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.vorticity = val

# Dissolve
def fluid_gas_dissolve_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_dissolve_smoke = h

def fluid_gas_dissolve_time(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.dissolve_speed = val

def fluid_gas_dissolve_slow_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_dissolve_smoke_log = h

# Noise
def fluid_gas_noise_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_noise = h

def fluid_gas_noise_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_scale = h

def fluid_gas_noise_upres_factor(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_scale = val

def fluid_gas_noise_method(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_type = value.upper()

def fluid_gas_noise_strength(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_strength = val

def fluid_gas_noise_scale(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_pos_scale = val

def fluid_gas_noise_time(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.noise_time_anim = val

# Fire
def fluid_gas_fire_reaction_speed(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.burning_rate = val

def fluid_gas_fire_smoke(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_smoke = val

def fluid_gas_fire_vorticity(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_vorticity = val

def fluid_gas_fire_temp_max(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_max_temp = val

def fluid_gas_fire_temp_min(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_ignition = val

def fluid_gas_fire_color_rgb(red,green,blue):
    r = float(red)
    g = float(green)
    b = float(blue)
    bpy.context.object.modifiers["Fluid"].domain_settings.flame_smoke_color = (r, g, b)

# Fluid
def fluid_fluid_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_flip_particles = h

def fluid_fluid_flip_ratio(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.flip_ratio = val

def fluid_fluid_particle_max(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sys_particle_maximum = val

def fluid_fluid_particle_radius(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_radius = val

def fluid_fluid_particle_sampling(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_number = val

def fluid_fluid_particle_random(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_randomness = val

def fluid_fluid_cell_max(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_max = val

def fluid_fluid_cell_min(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_min = val

def fluid_fluid_narrow_bandwidth(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.particle_band_width = val

def fluid_fluid_frac_obs_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_fractions = h

def fluid_fluid_obs_distance(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.fractions_distance = val

def fluid_fluid_obs_threshold(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.fractions_threshold = val

def fluid_fluid_diffusion_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_diffusion = h

def fluid_fluid_diffusion_base(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.viscosity_base = val

def fluid_fluid_diffusion_exponent(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.viscosity_exponent = val

def fluid_fluid_diffusion_surface(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.surface_tension = val

def fluid_fluid_particles_bubbles_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_bubble_particles = h

def fluid_fluid_particles_foam_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_foam_particles = h

def fluid_fluid_particles_spray_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_spray_particles = h

def fluid_fluid_particles_combined_export(value):
    value = value.replace(" ", "_")
    value = value.upper()
    print(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_combined_export = value

def fluid_fluid_particles_wave_crest_potential_maximum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_max_wavecrest = val

def fluid_fluid_particles_wave_crest_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_wavecrest = val

def fluid_fluid_particles_traped_air_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_max_trappedair = val

def fluid_fluid_particles_traped_air_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_trappedair = val

def fluid_fluid_particles_kinetic_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_max_energy = val

def fluid_fluid_particles_kinetic_potential_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_energy = val

def fluid_fluid_particles_potential_radius(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_energy = val

def fluid_fluid_particles_particle_update_radius(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_potential_min_energy = val

def fluid_fluid_particles_wave_crest_particle_sampling(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_sampling_trappedair = val

def fluid_fluid_particles_traped_air_particle_sampling(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_sampling_wavecrest = val

def fluid_fluid_particles_particle_life_maximum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_life_max = val

def fluid_fluid_particles_particle_life_minimum(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_life_min = val

def fluid_fluid_particles_bubble_buoyancy(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_bubble_buoyancy = val

def fluid_fluid_particles_bubble_drag(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_bubble_drag = val

def fluid_fluid_particles_particles_in_boundary(value):
    bpy.context.object.modifiers["Fluid"].domain_settings.sndparticle_boundary = value.upper()

def fluid_fluid_mesh_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_mesh = h

def fluid_fluid_mesh_upres(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.mesh_scale = val

def fluid_fluid_mesh_particle_radius(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.mesh_particle_radius = val

def fluid_fluid_mesh_smooth_pos(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.mesh_smoothen_pos = val

def fluid_fluid_mesh_smooth_pos(value):
    val = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.mesh_smoothen_pos = val

def fluid_fluid_mesh_use_speed_vectors(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)    
    bpy.context.object.modifiers["Fluid"].domain_settings.use_speed_vectors = h

def fluid_fluid_mesh_generator(value):
    if value.upper() == 'FINAL':
        bpy.context.object.modifiers["Fluid"].domain_settings.mesh_generator = 'IMPROVED'
    elif value.upper() == 'PREVIEW':
        bpy.context.object.modifiers["Fluid"].domain_settings.mesh_generator = 'UNION'

def fluid_fluid_mesh_concavity_upper(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.mesh_concave_upper = val

def fluid_fluid_mesh_concavity_lower(value):
    val = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.mesh_concave_lower = val

# Adpative Domain
def fluid_domain_adapt_toggle(value):
    if value.upper() == 'FALSE':
        h =bool(False)
    elif value.upper() == 'TRUE':
        h =bool(True)
    bpy.context.object.modifiers["Fluid"].domain_settings.use_adaptive_domain = h

def fluid_domain_adapt_res(value):
    intval = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.additional_res = intval

def fluid_domain_adapt_margin(value):
    intval = int(value)
    if intval > 24:
        print("Too high")
    else:
        bpy.context.object.modifiers["Fluid"].domain_settings.adapt_margin = intval

def fluid_domain_adapt_threshold(value):
    floatval = float(value)
    if floatval > 1:
        print("Too high")
    else:
        bpy.context.object.modifiers["Fluid"].domain_settings.adapt_threshold = floatval
#endregion
#region TEXT OBJECTS
def create_text_file(textname):
    return bpy.data.texts.new(textname)

def delete_text_file(textname):
    if is_string(textname):
        t = bpy.data.texts[textname]
        bpy.data.texts.remove(t)
    else:
        bpy.data.texts.remove(textname)
    
def get_lines_in_text_object(textname):
    return bpy.data.texts[textname].lines
#endregion
#region DATA CHECKS
def is_string(ref):
    if isinstance(ref, str):
        return True
    else:
        return False
#endregion
#region DATA CONSTRUCTORS
def make_vector(data):
    return Vector((data[0],data[1],data[2]))
def make_obj_list(ref):
    if ref is None:
        return [get_object(ref)]
    return get_objects(ref)
#endregion
#region MISC
def clear_unwanted_data():
    delete_unused_data()
def clear_unused_data():
    #bpy.ops.outliner.orphans_purge()
    delete_unused_data()
def delete_unused_data():
    #bpy.data.orphans_purge() # is considered experimental
    for block in bpy.data.lights:
        if block.users == 0:
            bpy.data.lights.remove(block)
    
    for block in bpy.data.curves:
        if block.users == 0:
            bpy.data.curves.remove(block)
    
    for block in bpy.data.cameras:
        if block.users == 0:
            bpy.data.cameras.remove(block)
            
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)

    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)

    for block in bpy.data.textures:
        if block.users == 0:
            bpy.data.textures.remove(block)

    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)
def debug_test():
    print("EasyBPY debug output")
#endregion
#region COMMON WORKFLOW FUNCTIONS
def organize_outliner():
    d = deselect_all_objects
    c = create_collection
    m = move_objects_to_collection
    ce = collection_exists
    gc = get_collection

    if bpy.context.active_object != None:
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

    # Cameras
    d()
    select_all_cameras()
    colname = "Cameras"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Lights
    d()
    select_all_lights()
    colname = "Lights"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Empties
    d()
    select_all_empties()
    colname = "Empties"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Mesh Objects
    d()
    select_all_meshes()
    colname = "Objects"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Curves
    d()
    select_all_curves()
    colname = "Curves"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)
        
    # Surfaces
    d()
    select_all_surfaces()
    colname = "Surfaces"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)
        
    # Metas
    d()
    select_all_metas()
    colname = "Metas"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Text
    d()
    select_all_text()
    colname = "Text"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Volumes
    d()
    select_all_volumes()
    colname = "Volumes"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Armatures
    d()
    select_all_armatures()
    colname = "Armatures"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Lattices
    d()
    select_all_lattices()
    colname = "Lattices"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Grease Pencil
    d()
    select_all_grease_pencils()
    colname = "Grease Pencils"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)

    # Light Probes
    d()
    select_all_light_probes()
    colname = "Light Probes"
    if len(so())>0:
        col = None
        if ce(colname):
            col = gc(colname)
            pass
        else:
            col = c(colname)
        m(so(),col)
    
    # End
    d()

def suffix_convert_dataset(data):
    for d in data:
        nn = d.name
        if '_' in d.name:
            r = d.name.split('_')
            if '.' in r[-1]:
                r2 = r[-1].split('.')
                if r2[0].isdigit():
                    val = int(r2[0]) + int(r2[1])
                    nn = r[0] + '_' + str(val)
                    i = 1
                    while nn in data:
                        nn = r[0] + '_' + str(val + i)
                        i += 1
                else:
                    if r2[1].isdigit():
                        val = int(r2[1])
                        i = 0
                        nn = ""
                        while i < len(r)-1:
                            nn = nn + r[i] + "_"
                            i+=1
                        nn = nn + r2[0] + "_" + str(val)
        else:
            if '.' in d.name:
                r = d.name.split('.')
                if r[-1].isdigit():
                    val = int(r[-1])
                    nn = r[0] + '_' + str(val)
                    i = 1
                    while nn in data:
                        nn = r[0] + '_' + str(val + i)
                        i += 1
        d.name = nn

def convert_suffixes_underscore():
    suffix_convert_dataset(bpy.data.meshes)
    suffix_convert_dataset(bpy.data.objects)
    suffix_convert_dataset(bpy.data.textures)
    suffix_convert_dataset(bpy.data.images)
    suffix_convert_dataset(bpy.data.materials)

def convert_suffixes():
    convert_suffixes_underscore()

def add_prefix_to_name(ref, prefix, delim="_"):
    objlist = make_obj_list(ref)
    for o in objlist:
        o.name = prefix + delim + o.name

def add_suffix_to_name(ref, suffix, delim="_"):
    objlist = make_obj_list(ref)
    for o in objlist:
        o.name = o.name + delim + suffix
#endregion