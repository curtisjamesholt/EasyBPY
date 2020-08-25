import bpy

# Objects

# Creates object - (string) name, (string) col
def create_object(name, col):
    m = bpy.data.meshes.new(name)
    o = bpy.data.objects.new(name, m)
    colref = bpy.data.collections[col]
    colref.objects.link(o)

def delete_object(ref):
    pass

def duplicate_object(ref):
    pass

def instance_object(ref):
    pass

def get_object(ref):
    pass

def object_exists(ref):
    pass

# Collections

# Materials

# Textures