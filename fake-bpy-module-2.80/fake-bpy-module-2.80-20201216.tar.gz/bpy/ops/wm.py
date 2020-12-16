import sys
import typing
import bpy.types


def alembic_export(filepath: str = "",
                   check_existing: bool = True,
                   filter_blender: bool = False,
                   filter_backup: bool = False,
                   filter_image: bool = False,
                   filter_movie: bool = False,
                   filter_python: bool = False,
                   filter_font: bool = False,
                   filter_sound: bool = False,
                   filter_text: bool = False,
                   filter_btx: bool = False,
                   filter_collada: bool = False,
                   filter_alembic: bool = True,
                   filter_folder: bool = True,
                   filter_blenlib: bool = False,
                   filemode: int = 8,
                   display_type: typing.Union[str, int] = 'DEFAULT',
                   sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
                   start: int = -2147483648,
                   end: int = -2147483648,
                   xsamples: int = 1,
                   gsamples: int = 1,
                   sh_open: float = 0.0,
                   sh_close: float = 1.0,
                   selected: bool = False,
                   renderable_only: bool = True,
                   visible_layers_only: bool = False,
                   flatten: bool = False,
                   uvs: bool = True,
                   packuv: bool = True,
                   normals: bool = True,
                   vcolors: bool = False,
                   face_sets: bool = False,
                   subdiv_schema: bool = False,
                   apply_subdiv: bool = False,
                   curves_as_mesh: bool = False,
                   compression_type: typing.Union[str, int] = 'OGAWA',
                   global_scale: float = 1.0,
                   triangulate: bool = False,
                   quad_method: typing.Union[str, int] = 'SHORTEST_DIAGONAL',
                   ngon_method: typing.Union[str, int] = 'BEAUTY',
                   export_hair: bool = True,
                   export_particles: bool = True,
                   as_background_job: bool = False,
                   init_scene_frame_range: bool = False):
    ''' Export current scene in an Alembic archive

    :param filepath: File Path, Path to file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene
    :type start: int
    :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene
    :type end: int
    :param xsamples: Transform Samples, Number of times per frame transformations are sampled
    :type xsamples: int
    :param gsamples: Geometry Samples, Number of times per frame object data are sampled
    :type gsamples: int
    :param sh_open: Shutter Open, Time at which the shutter is open
    :type sh_open: float
    :param sh_close: Shutter Close, Time at which the shutter is closed
    :type sh_close: float
    :param selected: Selected Objects Only, Export only selected objects
    :type selected: bool
    :param renderable_only: Renderable Objects Only, Export only objects marked renderable in the outliner
    :type renderable_only: bool
    :param visible_layers_only: Visible Layers Only, Export only objects in visible layers
    :type visible_layers_only: bool
    :param flatten: Flatten Hierarchy, Do not preserve objects' parent/children relationship
    :type flatten: bool
    :param uvs: UVs, Export UVs
    :type uvs: bool
    :param packuv: Pack UV Islands, Export UVs with packed island
    :type packuv: bool
    :param normals: Normals, Export normals
    :type normals: bool
    :param vcolors: Vertex Colors, Export vertex colors
    :type vcolors: bool
    :param face_sets: Face Sets, Export per face shading group assignments
    :type face_sets: bool
    :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembic's subdivision schema
    :type subdiv_schema: bool
    :param apply_subdiv: Apply Subsurf, Export subdivision surfaces as meshes
    :type apply_subdiv: bool
    :param curves_as_mesh: Curves as Mesh, Export curves and NURBS surfaces as meshes
    :type curves_as_mesh: bool
    :param compression_type: Compression
    :type compression_type: typing.Union[str, int]
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type global_scale: float
    :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles
    :type triangulate: bool
    :param quad_method: Quad Method, Method for splitting the quads into triangles * BEAUTY Beauty , Split the quads in nice triangles, slower method. * FIXED Fixed, Split the quads on the first and third vertices. * FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices. * SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices.
    :type quad_method: typing.Union[str, int]
    :param ngon_method: Polygon Method, Method for splitting the polygons into triangles * BEAUTY Beauty , Split the quads in nice triangles, slower method. * FIXED Fixed, Split the quads on the first and third vertices. * FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices. * SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices.
    :type ngon_method: typing.Union[str, int]
    :param export_hair: Export Hair, Exports hair particle systems as animated curves
    :type export_hair: bool
    :param export_particles: Export Particles, Exports non-hair particle systems
    :type export_particles: bool
    :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
    :type as_background_job: bool
    :type init_scene_frame_range: bool
    '''

    pass


def alembic_import(filepath: str = "",
                   check_existing: bool = True,
                   filter_blender: bool = False,
                   filter_backup: bool = False,
                   filter_image: bool = False,
                   filter_movie: bool = False,
                   filter_python: bool = False,
                   filter_font: bool = False,
                   filter_sound: bool = False,
                   filter_text: bool = False,
                   filter_btx: bool = False,
                   filter_collada: bool = False,
                   filter_alembic: bool = True,
                   filter_folder: bool = True,
                   filter_blenlib: bool = False,
                   filemode: int = 8,
                   display_type: typing.Union[str, int] = 'DEFAULT',
                   sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
                   scale: float = 1.0,
                   set_frame_range: bool = True,
                   validate_meshes: bool = False,
                   is_sequence: bool = False,
                   as_background_job: bool = False):
    ''' Load an Alembic archive

    :param filepath: File Path, Path to file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type scale: float
    :param set_frame_range: Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive
    :type set_frame_range: bool
    :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
    :type validate_meshes: bool
    :param is_sequence: Is Sequence, Set to true if the cache is split into separate files
    :type is_sequence: bool
    :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
    :type as_background_job: bool
    '''

    pass


def append(filepath: str = "",
           directory: str = "",
           filename: str = "",
           files: typing.
           Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
                 List['bpy.types.OperatorFileListElement'],
                 'bpy_prop_collection'] = None,
           filter_blender: bool = True,
           filter_backup: bool = False,
           filter_image: bool = False,
           filter_movie: bool = False,
           filter_python: bool = False,
           filter_font: bool = False,
           filter_sound: bool = False,
           filter_text: bool = False,
           filter_btx: bool = False,
           filter_collada: bool = False,
           filter_alembic: bool = False,
           filter_folder: bool = True,
           filter_blenlib: bool = True,
           filemode: int = 1,
           display_type: typing.Union[str, int] = 'DEFAULT',
           sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
           link: bool = False,
           autoselect: bool = True,
           active_collection: bool = True,
           instance_collections: bool = False,
           set_fake: bool = False,
           use_recursive: bool = True):
    ''' Append from a Library .blend file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param filename: File Name, Name of the file
    :type filename: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param link: Link, Link the objects or data-blocks rather than appending
    :type link: bool
    :param autoselect: Select, Select new objects
    :type autoselect: bool
    :param active_collection: Active Collection, Put new objects on the active collection
    :type active_collection: bool
    :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
    :type instance_collections: bool
    :param set_fake: Fake User, Set Fake User for appended items (except Objects and Groups)
    :type set_fake: bool
    :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
    :type use_recursive: bool
    '''

    pass


def blend_strings_utf8_validate():
    ''' Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files) :file: startup/bl_operators/file.py\:294 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/file.py$294> _

    '''

    pass


def call_menu(name: str = ""):
    ''' Call (draw) a pre-defined menu

    :param name: Name, Name of the menu
    :type name: str
    '''

    pass


def call_menu_pie(name: str = ""):
    ''' Call (draw) a pre-defined pie menu

    :param name: Name, Name of the pie menu
    :type name: str
    '''

    pass


def call_panel(name: str = "", keep_open: bool = True):
    ''' Call (draw) a pre-defined panel

    :param name: Name, Name of the menu
    :type name: str
    :param keep_open: Keep Open
    :type keep_open: bool
    '''

    pass


def collada_export(
        filepath: str = "",
        check_existing: bool = True,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = True,
        filter_alembic: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 8,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
        prop_bc_export_ui_section: typing.Union[str, int] = 'main',
        apply_modifiers: bool = False,
        export_mesh_type: int = 0,
        export_mesh_type_selection: typing.Union[str, int] = 'view',
        export_global_forward_selection: typing.Union[str, int] = 'Y',
        export_global_up_selection: typing.Union[str, int] = 'Z',
        apply_global_orientation: bool = False,
        selected: bool = False,
        include_children: bool = False,
        include_armatures: bool = False,
        include_shapekeys: bool = False,
        deform_bones_only: bool = False,
        include_animations: bool = True,
        include_all_actions: bool = True,
        export_animation_type_selection: typing.Union[str, int] = 'sample',
        sampling_rate: int = 1,
        keep_smooth_curves: bool = False,
        keep_keyframes: bool = False,
        keep_flat_curves: bool = False,
        active_uv_only: bool = False,
        use_texture_copies: bool = True,
        triangulate: bool = True,
        use_object_instantiation: bool = True,
        use_blender_profile: bool = True,
        sort_by_name: bool = False,
        export_object_transformation_type: int = 0,
        export_object_transformation_type_selection: typing.
        Union[str, int] = 'matrix',
        export_animation_transformation_type: int = 0,
        export_animation_transformation_type_selection: typing.
        Union[str, int] = 'matrix',
        open_sim: bool = False,
        limit_precision: bool = False,
        keep_bind_info: bool = False):
    ''' Save a Collada file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param prop_bc_export_ui_section: Export Section, Only for User Interface organization * main Main, Data Export Section. * geometry Geom, Geometry Export Section. * armature Arm, Armature Export Section. * animation Anim, Animation Export Section. * collada Extra, Collada Export Section.
    :type prop_bc_export_ui_section: typing.Union[str, int]
    :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive))
    :type apply_modifiers: bool
    :param export_mesh_type: Resolution, Modifier resolution for export
    :type export_mesh_type: int
    :param export_mesh_type_selection: Resolution, Modifier resolution for export * view View, Apply modifier's view settings. * render Render, Apply modifier's render settings.
    :type export_mesh_type_selection: typing.Union[str, int]
    :param export_global_forward_selection: Global Forward Axis, Global Forward axis for export * X X Forward, Global Forward is positive X Axis. * Y Y Forward, Global Forward is positive Y Axis. * Z Z Forward, Global Forward is positive Z Axis. * -X -X Forward, Global Forward is negative X Axis. * -Y -Y Forward, Global Forward is negative Y Axis. * -Z -Z Forward, Global Forward is negative Z Axis.
    :type export_global_forward_selection: typing.Union[str, int]
    :param export_global_up_selection: Global Up Axis, Global Up axis for export * X X Up, Global UP is positive X Axis. * Y Y Up, Global UP is positive Y Axis. * Z Z Up, Global UP is positive Z Axis. * -X -X Up, Global UP is negative X Axis. * -Y -Y Up, Global UP is negative Y Axis. * -Z -Z Up, Global UP is negative Z Axis.
    :type export_global_up_selection: typing.Union[str, int]
    :param apply_global_orientation: Apply Global Orientation, Rotate all root objects to match the global orientation settings otherwise set the global orientation per Collada asset
    :type apply_global_orientation: bool
    :param selected: Selection Only, Export only selected elements
    :type selected: bool
    :param include_children: Include Children, Export all children of selected objects (even if not selected)
    :type include_children: bool
    :param include_armatures: Include Armatures, Export related armatures (even if not selected)
    :type include_armatures: bool
    :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects
    :type include_shapekeys: bool
    :param deform_bones_only: Deform Bones only, Only export deforming bones with armatures
    :type deform_bones_only: bool
    :param include_animations: Include Animations, Export animations if available (exporting animations will enforce the decomposition of node transforms into <translation> <rotation> and <scale> components)
    :type include_animations: bool
    :param include_all_actions: Include all Actions, Export also unassigned actions (this allows you to export entire animation libraries for your character(s))
    :type include_all_actions: bool
    :param export_animation_type_selection: Key Type, Type for exported animations (use sample keys or Curve keys) * sample Samples, Export Sampled points guided by sampling rate. * keys Curves, Export Curves (note: guided by curve keys).
    :type export_animation_type_selection: typing.Union[str, int]
    :param sampling_rate: Sampling Rate, The distance between 2 keyframes (1 to key every frame)
    :type sampling_rate: int
    :param keep_smooth_curves: Keep Smooth curves, Export also the curve handles (if available) (this does only work when the inverse parent matrix is the unity matrix, otherwise you may end up with odd results)
    :type keep_smooth_curves: bool
    :param keep_keyframes: Keep Keyframes, Use existing keyframes as additional sample points (this helps when you want to keep manual tweaks)
    :type keep_keyframes: bool
    :param keep_flat_curves: All keyed curves, Export also curves which have only one key or are totally flat
    :type keep_flat_curves: bool
    :param active_uv_only: Only Selected UV Map, Export only the selected UV Map
    :type active_uv_only: bool
    :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported
    :type use_texture_copies: bool
    :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles
    :type triangulate: bool
    :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data
    :type use_object_instantiation: bool
    :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)
    :type use_blender_profile: bool
    :param sort_by_name: Sort by Object name, Sort exported data by Object name
    :type sort_by_name: bool
    :param export_object_transformation_type: Transform, Object Transformation type for translation, scale and rotation
    :type export_object_transformation_type: int
    :param export_object_transformation_type_selection: Transform, Object Transformation type for translation, scale and rotation * matrix Matrix, Use <matrix> representation for exported transformations. * decomposed Decomposed, Use <rotate>, <translate> and <scale> representation for exported transformations.
    :type export_object_transformation_type_selection: typing.Union[str, int]
    :param export_animation_transformation_type: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab
    :type export_animation_transformation_type: int
    :param export_animation_transformation_type_selection: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab * matrix Matrix, Use <matrix> representation for exported transformations. * decomposed Decomposed, Use <rotate>, <translate> and <scale> representation for exported transformations.
    :type export_animation_transformation_type_selection: typing.Union[str, int]
    :param open_sim: Export to SL/OpenSim, Compatibility mode for SL, OpenSim and other compatible online worlds
    :type open_sim: bool
    :param limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits
    :type limit_precision: bool
    :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
    :type keep_bind_info: bool
    '''

    pass


def collada_import(filepath: str = "",
                   filter_blender: bool = False,
                   filter_backup: bool = False,
                   filter_image: bool = False,
                   filter_movie: bool = False,
                   filter_python: bool = False,
                   filter_font: bool = False,
                   filter_sound: bool = False,
                   filter_text: bool = False,
                   filter_btx: bool = False,
                   filter_collada: bool = True,
                   filter_alembic: bool = False,
                   filter_folder: bool = True,
                   filter_blenlib: bool = False,
                   filemode: int = 8,
                   display_type: typing.Union[str, int] = 'DEFAULT',
                   sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
                   import_units: bool = False,
                   fix_orientation: bool = False,
                   find_chains: bool = False,
                   auto_connect: bool = False,
                   min_chain_length: int = 0,
                   keep_bind_info: bool = False):
    ''' Load a Collada file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param import_units: Import Units, If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene
    :type import_units: bool
    :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)
    :type fix_orientation: bool
    :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected
    :type find_chains: bool
    :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone
    :type auto_connect: bool
    :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value
    :type min_chain_length: int
    :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
    :type keep_bind_info: bool
    '''

    pass


def context_collection_boolean_set(data_path_iter: str = "",
                                   data_path_item: str = "",
                                   type: typing.Union[str, int] = 'TOGGLE'):
    ''' Set boolean values for a collection of items

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str
    :param type: Type
    :type type: typing.Union[str, int]
    '''

    pass


def context_cycle_array(data_path: str = "", reverse: bool = False):
    ''' Set a context array value (useful for cycling the active mesh edit mode)

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool
    '''

    pass


def context_cycle_enum(data_path: str = "",
                       reverse: bool = False,
                       wrap: bool = False):
    ''' Toggle a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool
    '''

    pass


def context_cycle_int(data_path: str = "",
                      reverse: bool = False,
                      wrap: bool = False):
    ''' Set a context value (useful for cycling active material, vertex keys, groups, etc.)

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool
    '''

    pass


def context_menu_enum(data_path: str = ""):
    ''' Undocumented contribute <https://developer.blender.org/T51061>

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    '''

    pass


def context_modal_mouse(data_path_iter: str = "",
                        data_path_item: str = "",
                        header_text: str = "",
                        input_scale: float = 0.01,
                        invert: bool = False,
                        initial_x: int = 0):
    ''' Adjust arbitrary values with mouse input

    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str
    :param header_text: Header Text, Text to display in header during scale
    :type header_text: str
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta
    :type input_scale: float
    :param invert: invert, Invert the mouse input
    :type invert: bool
    :param initial_x: initial_x
    :type initial_x: int
    '''

    pass


def context_pie_enum(data_path: str = ""):
    ''' Undocumented contribute <https://developer.blender.org/T51061>

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    '''

    pass


def context_scale_float(data_path: str = "", value: float = 1.0):
    ''' Scale a float context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assign value
    :type value: float
    '''

    pass


def context_scale_int(data_path: str = "",
                      value: float = 1.0,
                      always_step: bool = True):
    ''' Scale an int context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assign value
    :type value: float
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0
    :type always_step: bool
    '''

    pass


def context_set_boolean(data_path: str = "", value: bool = True):
    ''' Set a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assignment value
    :type value: bool
    '''

    pass


def context_set_enum(data_path: str = "", value: str = ""):
    ''' Set a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assignment value (as a string)
    :type value: str
    '''

    pass


def context_set_float(data_path: str = "",
                      value: float = 0.0,
                      relative: bool = False):
    ''' Set a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assignment value
    :type value: float
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool
    '''

    pass


def context_set_id(data_path: str = "", value: str = ""):
    ''' Set a context value to an ID data-block

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assign value
    :type value: str
    '''

    pass


def context_set_int(data_path: str = "",
                    value: int = 0,
                    relative: bool = False):
    ''' Set a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assign value
    :type value: int
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool
    '''

    pass


def context_set_string(data_path: str = "", value: str = ""):
    ''' Set a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assign value
    :type value: str
    '''

    pass


def context_set_value(data_path: str = "", value: str = ""):
    ''' Set a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value: Value, Assignment value (as a string)
    :type value: str
    '''

    pass


def context_toggle(data_path: str = "", module: str = ""):
    ''' Toggle a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param module: Module, Optionally override the context with a module
    :type module: str
    '''

    pass


def context_toggle_enum(data_path: str = "",
                        value_1: str = "",
                        value_2: str = ""):
    ''' Toggle a context value

    :param data_path: Context Attributes, RNA context string
    :type data_path: str
    :param value_1: Value, Toggle enum
    :type value_1: str
    :param value_2: Value, Toggle enum
    :type value_2: str
    '''

    pass


def debug_menu(debug_value: int = 0):
    ''' Open a popup to set the debug level

    :param debug_value: Debug Value
    :type debug_value: int
    '''

    pass


def doc_view(doc_id: str = ""):
    ''' Open online reference docs in a web browser

    :param doc_id: Doc ID
    :type doc_id: str
    '''

    pass


def doc_view_manual(doc_id: str = ""):
    ''' Load online manual

    :param doc_id: Doc ID
    :type doc_id: str
    '''

    pass


def doc_view_manual_ui_context():
    ''' View a context based online manual in a web browser

    '''

    pass


def drop_blend_file(filepath: str = ""):
    ''' Undocumented contribute <https://developer.blender.org/T51061>

    :param filepath: filepath
    :type filepath: str
    '''

    pass


def interface_theme_preset_add(name: str = "",
                               remove_name: bool = False,
                               remove_active: bool = False):
    ''' Add or remove a theme preset

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def keyconfig_preset_add(name: str = "",
                         remove_name: bool = False,
                         remove_active: bool = False):
    ''' Add or remove a Key-config Preset

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    '''

    pass


def lib_reload(library: str = "",
               filepath: str = "",
               directory: str = "",
               filename: str = "",
               filter_blender: bool = True,
               filter_backup: bool = False,
               filter_image: bool = False,
               filter_movie: bool = False,
               filter_python: bool = False,
               filter_font: bool = False,
               filter_sound: bool = False,
               filter_text: bool = False,
               filter_btx: bool = False,
               filter_collada: bool = False,
               filter_alembic: bool = False,
               filter_folder: bool = True,
               filter_blenlib: bool = False,
               filemode: int = 8,
               relative_path: bool = True,
               display_type: typing.Union[str, int] = 'DEFAULT',
               sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA'):
    ''' Reload the given library

    :param library: Library, Library to reload
    :type library: str
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param filename: File Name, Name of the file
    :type filename: str
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    '''

    pass


def lib_relocate(
        library: str = "",
        filepath: str = "",
        directory: str = "",
        filename: str = "",
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        filter_blender: bool = True,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 8,
        relative_path: bool = True,
        display_type: typing.Union[str, int] = 'DEFAULT',
        sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA'):
    ''' Relocate the given library to one or several others

    :param library: Library, Library to relocate
    :type library: str
    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param filename: File Name, Name of the file
    :type filename: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    '''

    pass


def link(filepath: str = "",
         directory: str = "",
         filename: str = "",
         files: typing.
         Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
               List['bpy.types.OperatorFileListElement'],
               'bpy_prop_collection'] = None,
         filter_blender: bool = True,
         filter_backup: bool = False,
         filter_image: bool = False,
         filter_movie: bool = False,
         filter_python: bool = False,
         filter_font: bool = False,
         filter_sound: bool = False,
         filter_text: bool = False,
         filter_btx: bool = False,
         filter_collada: bool = False,
         filter_alembic: bool = False,
         filter_folder: bool = True,
         filter_blenlib: bool = True,
         filemode: int = 1,
         relative_path: bool = True,
         display_type: typing.Union[str, int] = 'DEFAULT',
         sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
         link: bool = True,
         autoselect: bool = True,
         active_collection: bool = True,
         instance_collections: bool = True):
    ''' Link from a Library .blend file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param directory: Directory, Directory of the file
    :type directory: str
    :param filename: File Name, Name of the file
    :type filename: str
    :param files: Files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param link: Link, Link the objects or data-blocks rather than appending
    :type link: bool
    :param autoselect: Select, Select new objects
    :type autoselect: bool
    :param active_collection: Active Collection, Put new objects on the active collection
    :type active_collection: bool
    :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
    :type instance_collections: bool
    '''

    pass


def memory_statistics():
    ''' Print memory statistics to the console

    '''

    pass


def open_mainfile(filepath: str = "",
                  filter_blender: bool = True,
                  filter_backup: bool = False,
                  filter_image: bool = False,
                  filter_movie: bool = False,
                  filter_python: bool = False,
                  filter_font: bool = False,
                  filter_sound: bool = False,
                  filter_text: bool = False,
                  filter_btx: bool = False,
                  filter_collada: bool = False,
                  filter_alembic: bool = False,
                  filter_folder: bool = True,
                  filter_blenlib: bool = False,
                  filemode: int = 8,
                  display_type: typing.Union[str, int] = 'DEFAULT',
                  sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
                  load_ui: bool = True,
                  use_scripts: bool = True,
                  display_file_selector: bool = True,
                  state: int = 0):
    ''' Open a Blender file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param load_ui: Load UI, Load user interface setup in the .blend file
    :type load_ui: bool
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool
    :param display_file_selector: Display File Selector
    :type display_file_selector: bool
    :param state: State
    :type state: int
    '''

    pass


def operator_cheat_sheet():
    ''' List all the Operators in a text-block, useful for scripting :file: startup/bl_operators/wm.py\:1442 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/wm.py$1442> _

    '''

    pass


def operator_defaults():
    ''' Set the active operator to its default values

    '''

    pass


def operator_pie_enum(data_path: str = "", prop_string: str = ""):
    ''' Undocumented contribute <https://developer.blender.org/T51061>

    :param data_path: Operator, Operator name (in python as string)
    :type data_path: str
    :param prop_string: Property, Property name (as a string)
    :type prop_string: str
    '''

    pass


def operator_preset_add(name: str = "",
                        remove_name: bool = False,
                        remove_active: bool = False,
                        operator: str = ""):
    ''' Add or remove an Operator Preset

    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool
    :param remove_active: remove_active
    :type remove_active: bool
    :param operator: Operator
    :type operator: str
    '''

    pass


def owner_disable(owner_id: str = ""):
    ''' Enable workspace owner ID

    :param owner_id: UI Tag
    :type owner_id: str
    '''

    pass


def owner_enable(owner_id: str = ""):
    ''' Enable workspace owner ID

    :param owner_id: UI Tag
    :type owner_id: str
    '''

    pass


def path_open(filepath: str = ""):
    ''' Open a path in a file browser

    :param filepath: filepath
    :type filepath: str
    '''

    pass


def previews_batch_clear(
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        directory: str = "",
        filter_blender: bool = True,
        filter_folder: bool = True,
        use_scenes: bool = True,
        use_collections: bool = True,
        use_objects: bool = True,
        use_intern_data: bool = True,
        use_trusted: bool = False,
        use_backups: bool = True):
    ''' Clear selected .blend file's previews

    :param files: files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param directory: directory
    :type directory: str
    :param filter_blender: filter_blender
    :type filter_blender: bool
    :param filter_folder: filter_folder
    :type filter_folder: bool
    :param use_scenes: Scenes, Clear scenes' previews
    :type use_scenes: bool
    :param use_collections: Collections, Clear collections' previews
    :type use_collections: bool
    :param use_objects: Objects, Clear objects' previews
    :type use_objects: bool
    :param use_intern_data: Mat/Tex/..., Clear 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: bool
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
    :type use_backups: bool
    '''

    pass


def previews_batch_generate(
        files: typing.
        Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.
              List['bpy.types.OperatorFileListElement'],
              'bpy_prop_collection'] = None,
        directory: str = "",
        filter_blender: bool = True,
        filter_folder: bool = True,
        use_scenes: bool = True,
        use_collections: bool = True,
        use_objects: bool = True,
        use_intern_data: bool = True,
        use_trusted: bool = False,
        use_backups: bool = True):
    ''' Generate selected .blend file's previews

    :param files: files
    :type files: typing.Union[typing.Dict[str, 'bpy.types.OperatorFileListElement'], typing.List['bpy.types.OperatorFileListElement'], 'bpy_prop_collection']
    :param directory: directory
    :type directory: str
    :param filter_blender: filter_blender
    :type filter_blender: bool
    :param filter_folder: filter_folder
    :type filter_folder: bool
    :param use_scenes: Scenes, Generate scenes' previews
    :type use_scenes: bool
    :param use_collections: Collections, Generate collections' previews
    :type use_collections: bool
    :param use_objects: Objects, Generate objects' previews
    :type use_objects: bool
    :param use_intern_data: Mat/Tex/..., Generate 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: bool
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
    :type use_backups: bool
    '''

    pass


def previews_clear(
        id_type: typing.Union[typing.Set[str], typing.Set[int]] = {
            'ALL', 'GEOMETRY', 'GROUP', 'IMAGE', 'LIGHT', 'MATERIAL', 'OBJECT',
            'SCENE', 'SHADING', 'TEXTURE', 'WORLD'
        }):
    ''' Clear data-block previews (only for some types like objects, materials, textures, etc.)

    :param id_type: Data-Block Type, Which data-block previews to clear * ALL All Types. * GEOMETRY All Geometry Types, Clear previews for scenes, collections and objects. * SHADING All Shading Types, Clear previews for materiasl, lights, worlds, textures and images. * SCENE Scenes. * GROUP Groups. * OBJECT Objects. * MATERIAL Materials. * LIGHT Lights. * WORLD Worlds. * TEXTURE Textures. * IMAGE Images.
    :type id_type: typing.Union[typing.Set[str], typing.Set[int]]
    '''

    pass


def previews_ensure():
    ''' Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

    '''

    pass


def properties_add(data_path: str = ""):
    ''' Undocumented contribute <https://developer.blender.org/T51061>

    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    '''

    pass


def properties_context_change(context: str = ""):
    ''' Jump to a different tab inside the properties editor

    :param context: Context
    :type context: str
    '''

    pass


def properties_edit(data_path: str = "",
                    property: str = "",
                    value: str = "",
                    default: str = "",
                    min: float = -10000,
                    max: float = 10000.0,
                    use_soft_limits: bool = False,
                    is_overridable_library: bool = False,
                    soft_min: float = -10000,
                    soft_max: float = 10000.0,
                    description: str = ""):
    ''' Undocumented contribute <https://developer.blender.org/T51061>

    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    :param property: Property Name, Property name edit
    :type property: str
    :param value: Property Value, Property value edit
    :type value: str
    :param default: Default Value, Default value of the property. Important for NLA mixing
    :type default: str
    :param min: Min
    :type min: float
    :param max: Max
    :type max: float
    :param use_soft_limits: Use Soft Limits
    :type use_soft_limits: bool
    :param is_overridable_library: Is Library Overridable
    :type is_overridable_library: bool
    :param soft_min: Min
    :type soft_min: float
    :param soft_max: Max
    :type soft_max: float
    :param description: Tooltip
    :type description: str
    '''

    pass


def properties_remove(data_path: str = "", property: str = ""):
    ''' Internal use (edit a property data_path)

    :param data_path: Property Edit, Property data_path edit
    :type data_path: str
    :param property: Property Name, Property name edit
    :type property: str
    '''

    pass


def quit_blender():
    ''' Quit Blender

    '''

    pass


def radial_control(data_path_primary: str = "",
                   data_path_secondary: str = "",
                   use_secondary: str = "",
                   rotation_path: str = "",
                   color_path: str = "",
                   fill_color_path: str = "",
                   fill_color_override_path: str = "",
                   fill_color_override_test_path: str = "",
                   zoom_path: str = "",
                   image_id: str = "",
                   secondary_tex: bool = False):
    ''' Set some size property (like e.g. brush size) with mouse wheel

    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
    :type data_path_primary: str
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
    :type data_path_secondary: str
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
    :type use_secondary: str
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display
    :type rotation_path: str
    :param color_path: Color Path, Path of property used to set the color of the control
    :type color_path: str
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
    :type fill_color_path: str
    :param fill_color_override_path: Fill Color Override Path
    :type fill_color_override_path: str
    :param fill_color_override_test_path: Fill Color Override Test
    :type fill_color_override_test_path: str
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control
    :type zoom_path: str
    :param image_id: Image ID, Path of ID that is used to generate an image for the control
    :type image_id: str
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
    :type secondary_tex: bool
    '''

    pass


def read_factory_settings(app_template: str = "Template",
                          use_empty: bool = False):
    ''' Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

    :type app_template: str
    :param use_empty: Empty
    :type use_empty: bool
    '''

    pass


def read_factory_userpref():
    ''' Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

    '''

    pass


def read_history():
    ''' Reloads history and bookmarks

    '''

    pass


def read_homefile(filepath: str = "",
                  load_ui: bool = True,
                  use_splash: bool = False,
                  app_template: str = "Template",
                  use_empty: bool = False):
    ''' Open the default file (doesn't save the current file)

    :param filepath: File Path, Path to an alternative start-up file
    :type filepath: str
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :type load_ui: bool
    :param use_splash: Splash
    :type use_splash: bool
    :type app_template: str
    :param use_empty: Empty
    :type use_empty: bool
    '''

    pass


def read_userpref():
    ''' Load last saved preferences

    '''

    pass


def recover_auto_save(filepath: str = "",
                      filter_blender: bool = True,
                      filter_backup: bool = False,
                      filter_image: bool = False,
                      filter_movie: bool = False,
                      filter_python: bool = False,
                      filter_font: bool = False,
                      filter_sound: bool = False,
                      filter_text: bool = False,
                      filter_btx: bool = False,
                      filter_collada: bool = False,
                      filter_alembic: bool = False,
                      filter_folder: bool = False,
                      filter_blenlib: bool = False,
                      filemode: int = 8,
                      display_type: typing.Union[str, int] = 'LIST_LONG',
                      sort_method: typing.Union[str, int] = 'FILE_SORT_TIME'):
    ''' Open an automatically saved file to recover it

    :param filepath: File Path, Path to file
    :type filepath: str
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    '''

    pass


def recover_last_session():
    ''' Open the last closed file ("quit.blend")

    '''

    pass


def redraw_timer(type: typing.Union[str, int] = 'DRAW',
                 iterations: int = 10,
                 time_limit: float = 0.0):
    ''' Simple redraw timer to test the speed of updating the interface

    :param type: Type * DRAW Draw Region, Draw Region. * DRAW_SWAP Draw Region + Swap, Draw Region and Swap. * DRAW_WIN Draw Window, Draw Window. * DRAW_WIN_SWAP Draw Window + Swap, Draw Window and Swap. * ANIM_STEP Anim Step, Animation Steps. * ANIM_PLAY Anim Play, Animation Playback. * UNDO Undo/Redo, Undo/Redo.
    :type type: typing.Union[str, int]
    :param iterations: Iterations, Number of times to redraw
    :type iterations: int
    :param time_limit: Time Limit, Seconds to run the test for (override iterations)
    :type time_limit: float
    '''

    pass


def revert_mainfile(use_scripts: bool = True):
    ''' Reload the saved file

    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool
    '''

    pass


def save_as_mainfile(filepath: str = "",
                     check_existing: bool = True,
                     filter_blender: bool = True,
                     filter_backup: bool = False,
                     filter_image: bool = False,
                     filter_movie: bool = False,
                     filter_python: bool = False,
                     filter_font: bool = False,
                     filter_sound: bool = False,
                     filter_text: bool = False,
                     filter_btx: bool = False,
                     filter_collada: bool = False,
                     filter_alembic: bool = False,
                     filter_folder: bool = True,
                     filter_blenlib: bool = False,
                     filemode: int = 8,
                     display_type: typing.Union[str, int] = 'DEFAULT',
                     sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
                     compress: bool = False,
                     relative_remap: bool = True,
                     copy: bool = False):
    ''' Save the current file in the desired location

    :param filepath: File Path, Path to file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param compress: Compress, Write compressed .blend file
    :type compress: bool
    :param relative_remap: Remap Relative, Make paths relative when saving to a different directory
    :type relative_remap: bool
    :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
    :type copy: bool
    '''

    pass


def save_homefile():
    ''' Make the current file the default .blend file

    '''

    pass


def save_mainfile(filepath: str = "",
                  check_existing: bool = True,
                  filter_blender: bool = True,
                  filter_backup: bool = False,
                  filter_image: bool = False,
                  filter_movie: bool = False,
                  filter_python: bool = False,
                  filter_font: bool = False,
                  filter_sound: bool = False,
                  filter_text: bool = False,
                  filter_btx: bool = False,
                  filter_collada: bool = False,
                  filter_alembic: bool = False,
                  filter_folder: bool = True,
                  filter_blenlib: bool = False,
                  filemode: int = 8,
                  display_type: typing.Union[str, int] = 'DEFAULT',
                  sort_method: typing.Union[str, int] = 'FILE_SORT_ALPHA',
                  compress: bool = False,
                  relative_remap: bool = False,
                  exit: bool = False):
    ''' Save the current Blender file

    :param filepath: File Path, Path to file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param display_type: Display Type * DEFAULT Default, Automatically determine display type for files. * LIST_SHORT Short List, Display files as short list. * LIST_LONG Long List, Display files as a detailed list. * THUMBNAIL Thumbnails, Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode * FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically. * FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type. * FILE_SORT_TIME Sort by time, Sort files by modification time. * FILE_SORT_SIZE Sort by size, Sort files by size.
    :type sort_method: typing.Union[str, int]
    :param compress: Compress, Write compressed .blend file
    :type compress: bool
    :param relative_remap: Remap Relative, Make paths relative when saving to a different directory
    :type relative_remap: bool
    :param exit: Exit, Exit Blender after saving
    :type exit: bool
    '''

    pass


def save_userpref():
    ''' Save preferences separately, overrides startup file preferences

    '''

    pass


def search_menu():
    ''' Pop-up a search menu over all available operators in current context

    '''

    pass


def set_stereo_3d(display_mode: typing.Union[str, int] = 'ANAGLYPH',
                  anaglyph_type: typing.Union[str, int] = 'RED_CYAN',
                  interlace_type: typing.Union[str, int] = 'ROW_INTERLEAVED',
                  use_interlace_swap: bool = False,
                  use_sidebyside_crosseyed: bool = False):
    ''' Toggle 3D stereo support for current window (or change the display mode)

    :param display_mode: Display Mode * ANAGLYPH Anaglyph, Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required). * INTERLACE Interlace, Render views for left and right eyes interlaced in a single image (3D-ready monitor is required). * TIMESEQUENTIAL Time Sequential, Render alternate eyes (also known as page flip, quad buffer support in the graphic card is required). * SIDEBYSIDE Side-by-Side, Render views for left and right eyes side-by-side. * TOPBOTTOM Top-Bottom, Render views for left and right eyes one above another.
    :type display_mode: typing.Union[str, int]
    :param anaglyph_type: Anaglyph Type
    :type anaglyph_type: typing.Union[str, int]
    :param interlace_type: Interlace Type
    :type interlace_type: typing.Union[str, int]
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
    :type use_interlace_swap: bool
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice-versa
    :type use_sidebyside_crosseyed: bool
    '''

    pass


def splash():
    ''' Open the splash screen with release info

    '''

    pass


def sysinfo(filepath: str = ""):
    ''' Generate system information, saved into a text file

    :param filepath: filepath
    :type filepath: str
    '''

    pass


def tool_set_by_id(name: str = "",
                   cycle: bool = False,
                   space_type: typing.Union[str, int] = 'EMPTY'):
    ''' Set the tool by name (for keymaps)

    :param name: Identifier, Identifier of the tool
    :type name: str
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool
    :param space_type: Type
    :type space_type: typing.Union[str, int]
    '''

    pass


def tool_set_by_index(index: int = 0,
                      cycle: bool = False,
                      expand: bool = True,
                      space_type: typing.Union[str, int] = 'EMPTY'):
    ''' Set the tool by index (for keymaps)

    :param index: Index in toolbar
    :type index: int
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool
    :param expand: expand, Include tool sub-groups
    :type expand: bool
    :param space_type: Type
    :type space_type: typing.Union[str, int]
    '''

    pass


def toolbar():
    ''' Undocumented contribute <https://developer.blender.org/T51061> :file: startup/bl_operators/wm.py\:1611 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/wm.py$1611> _

    '''

    pass


def url_open(url: str = ""):
    ''' Open a website in the web-browser

    :param url: URL, URL to open
    :type url: str
    '''

    pass


def userpref_autoexec_path_add():
    ''' Add path to exclude from autoexecution

    '''

    pass


def userpref_autoexec_path_remove(index: int = 0):
    ''' Remove path to exclude from autoexecution

    :param index: Index
    :type index: int
    '''

    pass


def window_close():
    ''' Close the current window

    '''

    pass


def window_fullscreen_toggle():
    ''' Toggle the current window fullscreen

    '''

    pass


def window_new():
    ''' Create a new window

    '''

    pass


def window_new_main():
    ''' Create a new main window with its own workspace and scene selection

    '''

    pass
