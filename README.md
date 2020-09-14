== EasyBPY 0.0.1 ==
Created by Curtis Holt.
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
the GPL license.

Documentation will become available over time as the project evolves.
In the meantime, a list of all available functions is provided below.

Extra Thanks:
- Charan from Just 3D Things for contributing some functions and motivational support.
---

OBJECTS
- create_object                     
- copy_object                       
- get_active_object                 
- active_object                     
- get_selected_object               
- selected_object                   
- so
- get_selected_objects              
- select_object                     
- select_all_objects                
- deselect_object                   
- deselect_all_objects              
- delete_selected_objects           
- delete_object                     
- delete_objects                    
- duplicate_object                  
- instance_object                   
- get_object                        
- get_obj                           
- object_exists                     
- rename_object                     

OBJECTS - SELECTION
- select_all_meshes                 
- select_all_curves                 
- select_all_surfaces               
- select_all_metas                  
- select_all_text                   
- select_all_hair                   
- select_all_point_clouds           
- select_all_volumes                
- select_all_armatures              
- select_all_lattices               
- select_all_empties                
- select_all_greace_pencils         
- select_all_cameras                
- select_all_speakers               
- select_all_light_probes    
- invert_selection       

PRIMITIVE OBJECTS
- create_cube                       
- create_cylinder                   
- create_ico_sphere                 
- create_suzanne                    
- create_monkey                     
- create_cone                       

VISIBILITY
- hide_in_viewport                  
- show_in_viewport                  
- hide_in_render                    
- show_in_render                    
- display_as_bounds                 
- display_as_textured               
- display_as_solid                  
- display_as_wire                   

TRANSFORMATIONS
- location                          
- rotation                          
- scale                             

3D CURSOR   
- selection_to_cursor_without_offset
- selection_to_cursor_with_offset   
- cursor_to_world_origin            
- cursor_to_selection
- cursor_to_active
- selection_to_grid
- selection_to_active
- cursor_to_grid
- get_cursor_location
- set_cursor_location

SHADING
- shade_object_smooth               
- shade_smooth
- shade_object_flat                 
- shade_flat
- set_smooth_angle

MESHES
- create_mesh                       
- get_vertices                       
- get_edges                          
- get_faces                          
- get_mesh_from_object              

VERTEX GROUPS
( coming soon )

COLLECTIONS
- create_collection                 
- delete_collection                 
- delete_objects_in_colletion       
- delete_hierarchy                  
- duplicate_collection              
- get_objects_from_collection       
- get_collection                    
- get_col                           
- get_list_of_collections           
- link_object_to_collection         
- link_objects_to_collection        
- unlink_object_from_collection     
- unlink_objects_from_collection    
- move_object_to_collection         
- move_objects_to_collection        
- get_object_collection             
- get_object_collections            
- collection_exists                 

MATERIALS
- create_material                   
- material_exists                   
- delete_material                   
- get_material                      
- add_material_to_object            
- remove_material_from_object       
- remove_material                   
- get_materials_from_object         
- get_material_names_from_object    

NODES
( more coming soon )
- set_material_use_nodes
- get_node_tree
- create_node
- get_node_links
- create_node_link

TEXTURES
( more coming soon )
- create_texture
- delete_texture

MODIFIERS
- add_modifier                      
- get_modifier                      
- remove_modifier                   
- add_data_transfer
- add_mesh_cache
- add_mesh_sequence_cache
- add_normal_edit
- add_weighted_normal
- add_uv_project
- add_uv_warp
- add_vertex_weight_edit
- add_vertex_weight_mix
- add_vertex_weight_proximity
- add_array
- add_bevel
- add_boolean
- add_build
- add_decimate
- add_edge_split
- add_mask
- add_mirror
- add_multires
- add_remesh
- add_screw
- add_skin
- add_solidify
- add_subsurf
- add_triangulate
- add_weld
- add_wireframe
- add_armature
- add_cast
- add_curve
- add_displacement
- add_hook
- add_laplacian_deform
- add_lattice
- add_mesh_deform
- add_shrinkwrap
- add_simple_deform
- add_smooth
- add_corrective_smooth
- add_laplacian_smooth
- add_surface_deform
- add_warp
- add_wave
- add_cloth
- add_collision
- add_dynamic_paint
- add_explode
- add_fluid
- add_ocean
- add_particle_instance
- add_particle_system
- add_soft_body
- add_surface
- add_simulation                       

TEXT OBJECTS
- create_text_object
- delete_text_object
- get_lines_in_text_object

DATA CHECKS
- is_string                         

DATA CONSTRUCTORS
- make_vector                       

MISC
- clear_unwanted_data               
- clear_unsaved_data                
