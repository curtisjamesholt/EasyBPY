import bpy


#region OBJECTS - PRIMITIVES
def create_cube():
    bpy.ops.mesh.primitive_cube_add()
    return bpy.data.objects["Cube"]


def create_cylinder():
    bpy.ops.mesh.primitive_cylinder_add()
    return bpy.data.objects["Cylinder"]


def create_ico_sphere():
    bpy.ops.mesh.primitive_ico_sphere_add()
    return bpy.data.objects["Icosphere"]


def create_suzanne():
    bpy.ops.mesh.primitive_monkey_add()
    return bpy.data.objects["Suzanne"]


def create_monkey():
    create_suzanne()


def create_cone():
    bpy.ops.mesh.primitive_cone_add()
    return bpy.data.objects["Cone"]
#endregion
