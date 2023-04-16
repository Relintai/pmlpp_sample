
pandemonium_branch = 'master'

engine_repository = [ ['https://github.com/Relintai/pandemonium_engine.git', 'git@github.com:Relintai/pandemonium_engine.git'], 'pandemonium_engine', '' ]

# Relative to this script's directory
module_install_folder = './pandemonium_engine/custom_modules/'

module_repositories = [
	[ ['https://github.com/Relintai/pmlpp.git', 'git@github.com:Relintai/pmlpp.git'], 'pmlpp', '' ],
]

removed_modules = [
]

addon_repositories = [
]

third_party_addon_repositories = [
]

# Relative to the engine directory
custom_module_folders = 'custom_modules'

slim_args = ''
slim_args += 'module_bmp_enabled=no '
slim_args += 'module_broken_seals_module_enabled=no '
slim_args += 'module_cscript_enabled=no '
slim_args += 'module_database_enabled=no '
slim_args += 'module_database_sqlite_enabled=no '
slim_args += 'module_dds_enabled=no '
slim_args += 'module_enet_enabled=no '
slim_args += 'module_entity_spell_system_enabled=no '
slim_args += 'module_fastnoise_enabled=no ' 
#slim_args += 'module_freetype_enabled=no ' 
#slim_args += 'module_gdscript_enabled=no ' 
slim_args += 'module_gridmap_enabled=no '
slim_args += 'module_hdr_enabled=no '
slim_args += 'module_http_server_simple_enabled=no '
slim_args += 'module_jpg_enabled=no '
slim_args += 'module_lz4_enabled=no '
slim_args += 'module_material_maker_enabled=no '
#slim_args += 'module_mbedtls_enabled=no '
slim_args += 'module_mesh_data_resource_enabled=no '
slim_args += 'module_mesh_utils_enabled=no '
slim_args += 'module_minimp3_enabled=no '
#slim_args += 'module_navigation_enabled=no '
slim_args += 'module_network_synchronizer_enabled=no '
slim_args += 'module_ogg_enabled=no '
slim_args += 'module_opensimplex_enabled=no '
slim_args += 'module_opus_enabled=no '
slim_args += 'module_paint_enabled=no '
slim_args += 'module_props_enabled=no '
slim_args += 'module_props_2d_enabled=no '
slim_args += 'module_pvr_enabled=no '
#slim_args += 'module_regex_enabled=no '
slim_args += 'module_skeleton_2d_enabled=no '
slim_args += 'module_skeleton_3d_enabled=no '
slim_args += 'module_squish_enabled=no '
slim_args += 'module_stb_vorbis_enabled=no '
slim_args += 'module_steering_ai_enabled=no '
#slim_args += 'module_svg_enabled=no '
slim_args += 'module_terraman_enabled=no '
slim_args += 'module_terraman_2d_enabled=no '
slim_args += 'module_texture_packer_enabled=no '
slim_args += 'module_tga_enabled=no '
slim_args += 'module_theora_enabled=no '
slim_args += 'module_tile_map_enabled=no '
slim_args += 'module_ui_extensions_enabled=no '
#slim_args += 'module_unit_test_enabled=no '
slim_args += 'module_upnp_enabled=no '
slim_args += 'module_users_enabled=no '
slim_args += 'module_vhacd_enabled=no '
slim_args += 'module_vorbis_enabled=no '
slim_args += 'module_voxelman_enabled=no '
slim_args += 'module_web_enabled=no '
slim_args += 'module_websocket_enabled=no '
slim_args += 'module_wfc_enabled=no '
slim_args += 'module_cvtt_enabled=no '
#slim_args += 'module_editor_code_editor_enabled=no '
slim_args += 'module_etc_enabled=no '
slim_args += 'module_gltf_enabled=no '
slim_args += 'module_plugin_refresher_enabled=no '
slim_args += 'module_shader_editor_enabled=no '
#slim_args += 'module_text_editor_enabled=no '
slim_args += 'module_tinyexr_enabled=no '

#slim_args += 'disable_advanced_gui=yes '
#slim_args += 'disable_3d=yes '
