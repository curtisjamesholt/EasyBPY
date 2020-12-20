#Setting the type of fluid (domain,flow,effector, or none)

def set_fluid_type_none():
    bpy.context.object.modifiers["Fluid"].fluid_type = 'NONE'

def set_fluid_type_domain():
    bpy.context.object.modifiers["Fluid"].fluid_type = 'DOMAIN'

def set_fluid_type_flow():
    bpy.context.object.modifiers["Fluid"].fluid_type = 'FLOW'

def set_fluid_type_effector():
    bpy.context.object.modifiers["Fluid"].fluid_type = 'EFFECTOR'


#Effector parameters 

#Effector Type
def fluid_effector_type(type):
    bpy.context.object.modifiers["Fluid"].effector_settings.effector_type = type
      
#Sampling Substeps
def fluid_effector_subsample_value(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.subframes = intvalue

#surface thickness
def fluid_effector_thickness_value(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.surface_distance = intvalue

#Use effector, 1 = on 0 = off
def fluid_effector_use(fbool):
    bool = int(fbool)
    bpy.context.object.modifiers["Fluid"].effector_settings.use_effector = bool
    
#Is Planar, 1 = on 0 = off
def fluid_effector_isplanar(fbool):
    bool = int(fbool)
    bpy.context.object.modifiers["Fluid"].effector_settings.use_plane_init = bool

#enabling velocity
def fluid_effector_velocity(value):
    intvalue = int(value)
    bpy.context.object.modifiers["Fluid"].effector_settings.velocity_factor = intvalue

#Guide Mode 
def fluid_effector_guide_mode(value):
    if value == 'MAXIMUM' or value == 'MAX':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'MAXIMUM'
    if value == 'MINIMUM' or value == 'MIN':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'MINIMUM'
    if value == 'OVERRIDE' or value == 'OVER':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'OVERRIDE'
    if value == 'AVERAGED' or value == 'MEAN':
        bpy.context.object.modifiers["Fluid"].effector_settings.guide_mode = 'AVERAGED'
            
#Type Flow parameters

#setting the 'flow type'
def flow_type_set_smoke():
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_type = 'SMOKE'

def flow_type_set_fire():
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_type = 'FIRE'
    
def flow_type_set_fire_smoke():
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_type = 'BOTH'
    
def flow_type_set_fluid():
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_type = 'LIQUID'
    
#flow behavior
def flow_set_behavoir(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_behavior = value

#Use flow
def flow_use_flow(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_inflow = bool

#flow source, liquids
def flow_source(value):
    if value == 'PARTICLE SYSTEM':
        value = 'PARTICLES'
    bpy.context.object.modifiers["Fluid"].flow_settings.flow_source = value

#smoke colour
def flow_smoke_colour_rgb(r,g,b):
    print(r+g+b)
    rfloat = float(r)
    gfloat = float(g)
    bfloat = float(b)
    bpy.context.object.modifiers["Fluid"].flow_settings.smoke_color = (rfloat,gfloat,bfloat)
    
#Absloute density????? what ever it is??
def flow_absolute_density(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_absolute = bool

#Initial temprature
def flow_initial_temp(value):
    temp = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.temperature = temp
    
#Density,
def flow_density(value):
    density = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.density = density

#if they want to emit from a vertex group
def flow_vertexgroup(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.density_vertex_group = value


#Particle system
#setting the particle system
def flow_particle_system_select(value):
    bpy.context.object.modifiers["Fluid"].flow_settings.particle_system = bpy.data.objects["Cube"].particle_systems[value]

def flow_particle_set_size_toggle(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_particle_size = bool


#set size thing in particles
def flow_set_particle_size(value):
    size = float(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.particle_size = size


    
#intial Velocity
#toggle
def flow_initial_velocity_toggle(value):
    bool = int(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.use_initial_velocity = bool

#How much
def flow_initial_velocity_value(value):
    velocity = float(value)
    bpy.context.object.modifiers["Fluid"].flow_settings.velocity_factor = velocity






#Domains
def fluid_domain_set_gas():
    bpy.context.object.modifiers["Fluid"].domain_settings.domain_type = 'GAS'

def fluid_domain_set_liquid():
    bpy.context.object.modifiers["Fluid"].domain_settings.domain_type = 'LIQUID'

#Global Fluid Settings
#Resolution
def fluid_domain_set_resolution(value):
    res = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.resolution_max = res
    
#Time scale
def fluid_domain_time_scale(value):
    timespeed = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.time_scale = timespeed

#CFL number (Don't know what this is )
def fluid_domain_set_cfl(value):
    CFL = float(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.cfl_condition = CFL

#time steps
def fluid_domain_set_timesteps_max(value):
    timestep = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.timesteps_max = timestep
    
def fluid_domain_set_timesteps_min(value):
    timestep = int(value)
    bpy.context.object.modifiers["Fluid"].domain_settings.timesteps_min = timestep

#Scene gravity (Not sure if I'll add it)


#Border collisions

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

        
    
    
#Gas Domain

