from .objects import get_object
from .utils import is_string


#region MODIFIERS
def add_modifier(obj, name, id):
    objref = None
    if is_string(obj):
        objref = get_object(obj)
    else:
        objref = obj
    new_mod = objref.modifiers.new(name, id)
    return new_mod


def get_modifier(obj, name):
    objref = None
    if is_string(obj):
        objref = get_object(obj)
    else:
        objref = obj

    # we assume name is string
    if name in objref.modifiers:
        return objref.modifiers[name]
    else:
        return False


def remove_modifier(ref, name):
    objref = None
    if is_string(ref):
        objref = get_object(ref)
    else:
        objref = ref

    if is_string(name):
        if name in objref.modifiers:
            mod = get_modifier(objref, name)
            objref.modifiers.remove(mod)
    else:
        objref.modifiers.remove(name)


# Specific Modifiers
def add_data_transfer(ref, modname):
    return add_modifier(ref, modname, 'DATA_TRANSFER')


def add_mesh_cache(ref, modname):
    return add_modifier(ref, modname, 'MESH_CACHE')


def add_mesh_sequence_cache(ref, modname):
    return add_modifier(ref, modname, 'MESH_SEQUENCE_CACHE')


def add_normal_edit(ref, modname):
    return add_modifier(ref, modname, 'NORMAL_EDIT')


def add_weighted_normal(ref, modname):
    return add_modifier(ref, modname, 'WEIGHTED_NORMAL')


def add_uv_project(ref, modname):
    return add_modifier(ref, modname, 'UV_PROJECT')


def add_uv_warp(ref, modname):
    return add_modifier(ref, modname, 'UV_WARP')


def add_vertex_weight_edit(ref, modname):
    return add_modifier(ref, modname, 'VERTEX_WEIGHT_EDIT')


def add_vertex_weight_mix(ref, modname):
    return add_modifier(ref, modname, 'VERTEX_WEIGHT_MIX')


def add_vertex_weight_proximity(ref, modname):
    return add_modifier(ref, modname, 'VERTEX_WEIGHT_PROXIMITY')


def add_array(ref, modname):
    return add_modifier(ref, modname, 'ARRAY')


def add_bevel(ref, modname):
    return add_modifier(ref, modname, 'BEVEL')


def add_boolean(ref, modname):
    return add_modifier(ref, modname, 'BOOLEAN')


def add_build(ref, modname):
    return add_modifier(ref, modname, 'BUILD')


def add_decimate(ref, modname):
    return add_decimate(ref, modname, 'DECIMATE')


def add_edge_split(ref, modname):
    return add_modifier(ref, modname, 'EDGE_SPLIT')


def add_mask(ref, modname):
    return add_modifier(ref, modname, 'MASK')


def add_mirror(ref, modname):
    return add_modifier(ref, modname, 'MIRROR')


def add_multires(ref, modname):
    return add_modifier(ref, modname, 'MULTIRES')


def add_remesh(ref, modname):
    return add_modifier(ref, modname, 'REMESH')


def add_screw(ref, modname):
    return add_modifier(ref, modname, 'SCREW')


def add_skin(ref, modname):
    return add_modifier(ref, modname, 'SKIN')


def add_solidify(ref, modname):
    return add_modifier(ref, modname, 'SOLIDIFY')


def add_subsurf(ref, modname):
    return add_modifier(ref, modname, 'SUBSURF')


def add_triangulate(ref, modname):
    return add_modifier(ref, modname, 'TRIANGULATE')


def add_weld(ref, modname):
    return add_modifier(ref, modname, 'WELD')


def add_wireframe(ref, modname):
    return add_modifier(ref, modname, 'WIREFRAME')


def add_armature(ref, modname):
    return add_modifier(ref, modname, 'ARMATURE')


def add_cast(ref, modname):
    return add_modifier(ref, modname, 'CAST')


def add_curve(ref, modname):
    return add_modifier(ref, modname, 'CURVE')


def add_displace(ref, modname):
    return add_modifier(ref, modname, 'DISPLACE')


def add_hook(ref, modname):
    return add_modifier(ref, modname, 'HOOK')


def add_laplacian_deform(ref, modname):
    return add_modifier(ref, modname, 'LAPLACIANDEFORM')


def add_lattice(ref, modname):
    return add_modifier(ref, modname, 'LATTICE')


def add_mesh_deform(ref, modname):
    return add_modifier(ref, modname, 'MESH_DEFORM')


def add_shrinkwrap(ref, modname):
    return add_modifier(ref, modname, 'SHRINKWRAP')


def add_simple_deform(ref, modname):
    return add_modifier(ref, modname, 'SIMPLE_DEFORM')


def add_smooth(ref, modname):
    return add_modifier(ref, modname, 'SMOOTH')


def add_corrective_smooth(ref, modname):
    return add_modifier(ref, modname, 'CORRECTIVE_SMOOTH')


def add_laplacian_smooth(ref, modname):
    return add_modifier(ref, modname, 'LAPLACIANSMOOTH')


def add_surface_deform(ref, modname):
    return add_modifier(ref, modname, 'SURFACE_DEFORM')


def add_warp(ref, modname):
    return add_modifier(ref, modname, 'WARP')


def add_wave(ref, modname):
    return add_modifier(ref, modname, 'WAVE')


def add_cloth(ref, modname):
    return add_modifier(ref, modname, 'CLOTH')


def add_collision(ref, modname):
    return add_modifier(ref, modname, 'COLLISION')


def add_dynamic_paint(ref, modname):
    return add_modifier(ref, modname, 'DYNAMIC_PAINT')


def add_explode(ref, modname):
    return add_modifier(ref, modname, 'EXPLODE')


def add_fluid(ref, modname):
    return add_modifier(ref, modname, 'FLUID')


def add_ocean(ref, modname):
    return add_modifier(ref, modname, 'OCEAN')


def add_particle_instance(ref, modname):
    return add_modifier(ref, modname, 'PARTICLE_INSTANCE')


def add_particle_system(ref, modname):
    return add_modifier(ref, modname, 'PARTICLE_SYSTEM')


def add_soft_body(ref, modname):
    return add_modifier(ref, modname, 'SOFT_BODY')


def add_surface(ref, modname):
    return add_modifier(ref, modname, 'SURFACE')


def add_simulation(ref, modname):
    return add_modifier(ref, modname, 'SIMULATION')
#endregion
