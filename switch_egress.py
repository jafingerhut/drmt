dM = 9
dA = 1
dS = 0
nodes = \
{'_condition_55': {'num_fields': 1, 'type': 'action'},
 '_condition_56': {'num_fields': 1, 'type': 'action'},
 '_condition_57': {'num_fields': 1, 'type': 'action'},
 '_condition_58': {'num_fields': 1, 'type': 'action'},
 '_condition_59': {'num_fields': 1, 'type': 'action'},
 '_condition_60': {'num_fields': 1, 'type': 'action'},
 '_condition_61': {'num_fields': 1, 'type': 'action'},
 '_condition_62': {'num_fields': 1, 'type': 'action'},
 '_condition_63': {'num_fields': 1, 'type': 'action'},
 '_condition_64': {'num_fields': 1, 'type': 'action'},
 '_condition_65': {'num_fields': 1, 'type': 'action'},
 '_condition_66': {'num_fields': 1, 'type': 'action'},
 '_condition_67': {'num_fields': 1, 'type': 'action'},
 '_condition_68': {'num_fields': 1, 'type': 'action'},
 '_condition_69': {'num_fields': 1, 'type': 'action'},
 '_condition_70': {'num_fields': 1, 'type': 'action'},
 '_condition_71': {'num_fields': 1, 'type': 'action'},
 '_condition_72': {'num_fields': 1, 'type': 'action'},
 '_condition_73': {'num_fields': 1, 'type': 'action'},
 '_condition_74': {'num_fields': 1, 'type': 'action'},
 'egress_bd_map_ACTION': {'num_fields': 3, 'type': 'action'},
 'egress_bd_map_MATCH': {'key_width': 16, 'type': 'match'},
 'egress_bd_stats_ACTION': {'num_fields': 0, 'type': 'action'},
 'egress_bd_stats_MATCH': {'key_width': 19, 'type': 'match'},
 'egress_filter_ACTION': {'num_fields': 3, 'type': 'action'},
 'egress_filter_drop_ACTION': {'num_fields': 1, 'type': 'action'},
 'egress_ip_acl_ACTION': {'num_fields': 2, 'type': 'action'},
 'egress_ip_acl_MATCH': {'key_width': 120, 'type': 'match'},
 'egress_ipv6_acl_ACTION': {'num_fields': 2, 'type': 'action'},
 'egress_ipv6_acl_MATCH': {'key_width': 312, 'type': 'match'},
 'egress_l4_dst_port_ACTION': {'num_fields': 1, 'type': 'action'},
 'egress_l4_dst_port_MATCH': {'key_width': 16, 'type': 'match'},
 'egress_l4_src_port_ACTION': {'num_fields': 1, 'type': 'action'},
 'egress_l4_src_port_MATCH': {'key_width': 16, 'type': 'match'},
 'egress_l4port_fields_ACTION': {'num_fields': 2, 'type': 'action'},
 'egress_l4port_fields_MATCH': {'key_width': 3, 'type': 'match'},
 'egress_mac_acl_ACTION': {'num_fields': 2, 'type': 'action'},
 'egress_mac_acl_MATCH': {'key_width': 144, 'type': 'match'},
 'egress_nat_ACTION': {'num_fields': 6, 'type': 'action'},
 'egress_nat_MATCH': {'key_width': 14, 'type': 'match'},
 'egress_port_mapping_ACTION': {'num_fields': 4, 'type': 'action'},
 'egress_port_mapping_MATCH': {'key_width': 9, 'type': 'match'},
 'egress_qos_map_ACTION': {'num_fields': 1, 'type': 'action'},
 'egress_qos_map_MATCH': {'key_width': 13, 'type': 'match'},
 'egress_system_acl_ACTION': {'num_fields': 3, 'type': 'action'},
 'egress_system_acl_MATCH': {'key_width': 43, 'type': 'match'},
 'egress_vlan_xlate_ACTION': {'num_fields': 7, 'type': 'action'},
 'egress_vlan_xlate_MATCH': {'key_width': 32, 'type': 'match'},
 'egress_vni_ACTION': {'num_fields': 1, 'type': 'action'},
 'egress_vni_MATCH': {'key_width': 21, 'type': 'match'},
 'int_bos_ACTION': {'num_fields': 1, 'type': 'action'},
 'int_bos_MATCH': {'key_width': 24, 'type': 'match'},
 'int_insert_ACTION': {'num_fields': 18, 'type': 'action'},
 'int_insert_MATCH': {'key_width': 3, 'type': 'match'},
 'int_inst_0003_ACTION': {'num_fields': 10, 'type': 'action'},
 'int_inst_0003_MATCH': {'key_width': 4, 'type': 'match'},
 'int_inst_0407_ACTION': {'num_fields': 8, 'type': 'action'},
 'int_inst_0407_MATCH': {'key_width': 4, 'type': 'match'},
 'int_inst_0811_ACTION': {'num_fields': 0, 'type': 'action'},
 'int_inst_0811_MATCH': {'key_width': 4, 'type': 'match'},
 'int_inst_1215_ACTION': {'num_fields': 0, 'type': 'action'},
 'int_inst_1215_MATCH': {'key_width': 4, 'type': 'match'},
 'int_meta_header_update_ACTION': {'num_fields': 1, 'type': 'action'},
 'int_meta_header_update_MATCH': {'key_width': 8, 'type': 'match'},
 'int_outer_encap_ACTION': {'num_fields': 7, 'type': 'action'},
 'int_outer_encap_MATCH': {'key_width': 8, 'type': 'match'},
 'l3_rewrite_ACTION': {'num_fields': 3, 'type': 'action'},
 'l3_rewrite_MATCH': {'key_width': 15, 'type': 'match'},
 'mirror_ACTION': {'num_fields': 4, 'type': 'action'},
 'mirror_MATCH': {'key_width': 16, 'type': 'match'},
 'mtu_ACTION': {'num_fields': 1, 'type': 'action'},
 'mtu_MATCH': {'key_width': 10, 'type': 'match'},
 'replica_type_ACTION': {'num_fields': 1, 'type': 'action'},
 'replica_type_MATCH': {'key_width': 17, 'type': 'match'},
 'rewrite_ACTION': {'num_fields': 7, 'type': 'action'},
 'rewrite_MATCH': {'key_width': 16, 'type': 'match'},
 'rewrite_multicast_ACTION': {'num_fields': 1, 'type': 'action'},
 'rewrite_multicast_MATCH': {'key_width': 14, 'type': 'match'},
 'rid_ACTION': {'num_fields': 8, 'type': 'action'},
 'rid_MATCH': {'key_width': 16, 'type': 'match'},
 'smac_rewrite_ACTION': {'num_fields': 1, 'type': 'action'},
 'smac_rewrite_MATCH': {'key_width': 9, 'type': 'match'},
 'tunnel_decap_process_inner_ACTION': {'num_fields': 3, 'type': 'action'},
 'tunnel_decap_process_inner_MATCH': {'key_width': 3, 'type': 'match'},
 'tunnel_decap_process_outer_ACTION': {'num_fields': 7, 'type': 'action'},
 'tunnel_decap_process_outer_MATCH': {'key_width': 7, 'type': 'match'},
 'tunnel_dmac_rewrite_ACTION': {'num_fields': 1, 'type': 'action'},
 'tunnel_dmac_rewrite_MATCH': {'key_width': 14, 'type': 'match'},
 'tunnel_dst_rewrite_ACTION': {'num_fields': 1, 'type': 'action'},
 'tunnel_dst_rewrite_MATCH': {'key_width': 14, 'type': 'match'},
 'tunnel_encap_process_inner_ACTION': {'num_fields': 6, 'type': 'action'},
 'tunnel_encap_process_inner_MATCH': {'key_width': 5, 'type': 'match'},
 'tunnel_encap_process_outer_ACTION': {'num_fields': 25, 'type': 'action'},
 'tunnel_encap_process_outer_MATCH': {'key_width': 10, 'type': 'match'},
 'tunnel_mtu_ACTION': {'num_fields': 1, 'type': 'action'},
 'tunnel_mtu_MATCH': {'key_width': 14, 'type': 'match'},
 'tunnel_rewrite_ACTION': {'num_fields': 18, 'type': 'action'},
 'tunnel_rewrite_MATCH': {'key_width': 14, 'type': 'match'},
 'tunnel_smac_rewrite_ACTION': {'num_fields': 1, 'type': 'action'},
 'tunnel_smac_rewrite_MATCH': {'key_width': 9, 'type': 'match'},
 'tunnel_src_rewrite_ACTION': {'num_fields': 1, 'type': 'action'},
 'tunnel_src_rewrite_MATCH': {'key_width': 9, 'type': 'match'},
 'vlan_decap_ACTION': {'num_fields': 3, 'type': 'action'},
 'vlan_decap_MATCH': {'key_width': 2, 'type': 'match'}}

edges = \
{('_condition_55', '_condition_56'): {'delay': dS},
 ('_condition_55', '_condition_66'): {'delay': dS},
 ('_condition_55', '_condition_68'): {'delay': dS},
 ('_condition_55', '_condition_70'): {'delay': dS},
 ('_condition_55', '_condition_71'): {'delay': dS},
 ('_condition_55', '_condition_72'): {'delay': dS},
 ('_condition_55', 'egress_filter_ACTION'): {'delay': dS},
 ('_condition_55', 'egress_l4_dst_port_ACTION'): {'delay': dS},
 ('_condition_55', 'egress_l4_src_port_ACTION'): {'delay': dS},
 ('_condition_55', 'egress_l4port_fields_ACTION'): {'delay': dS},
 ('_condition_55', 'egress_port_mapping_ACTION'): {'delay': dS},
 ('_condition_56', '_condition_57'): {'delay': dS},
 ('_condition_56', 'mirror_ACTION'): {'delay': dS},
 ('_condition_57', 'replica_type_ACTION'): {'delay': dS},
 ('_condition_57', 'rid_ACTION'): {'delay': dS},
 ('_condition_58', 'vlan_decap_ACTION'): {'delay': dS},
 ('_condition_59', '_condition_60'): {'delay': dS},
 ('_condition_60', 'tunnel_decap_process_inner_ACTION'): {'delay': dS},
 ('_condition_60', 'tunnel_decap_process_outer_ACTION'): {'delay': dS},
 ('_condition_61', 'rewrite_ACTION'): {'delay': dS},
 ('_condition_61', 'rewrite_multicast_ACTION'): {'delay': dS},
 ('_condition_62', 'egress_qos_map_ACTION'): {'delay': dS},
 ('_condition_63', 'l3_rewrite_ACTION'): {'delay': dS},
 ('_condition_63', 'smac_rewrite_ACTION'): {'delay': dS},
 ('_condition_64', 'int_bos_ACTION'): {'delay': dS},
 ('_condition_64', 'int_inst_0003_ACTION'): {'delay': dS},
 ('_condition_64', 'int_inst_0407_ACTION'): {'delay': dS},
 ('_condition_64', 'int_inst_0811_ACTION'): {'delay': dS},
 ('_condition_64', 'int_inst_1215_ACTION'): {'delay': dS},
 ('_condition_65', 'egress_nat_ACTION'): {'delay': dS},
 ('_condition_66', '_condition_67'): {'delay': dS},
 ('_condition_66', 'egress_vni_ACTION'): {'delay': dS},
 ('_condition_66', 'tunnel_dmac_rewrite_ACTION'): {'delay': dS},
 ('_condition_66', 'tunnel_dst_rewrite_ACTION'): {'delay': dS},
 ('_condition_66', 'tunnel_encap_process_outer_ACTION'): {'delay': dS},
 ('_condition_66', 'tunnel_mtu_ACTION'): {'delay': dS},
 ('_condition_66', 'tunnel_rewrite_ACTION'): {'delay': dS},
 ('_condition_66', 'tunnel_smac_rewrite_ACTION'): {'delay': dS},
 ('_condition_66', 'tunnel_src_rewrite_ACTION'): {'delay': dS},
 ('_condition_67', 'tunnel_encap_process_inner_ACTION'): {'delay': dS},
 ('_condition_68', '_condition_69'): {'delay': dS},
 ('_condition_68', 'egress_ip_acl_ACTION'): {'delay': dS},
 ('_condition_69', 'egress_ipv6_acl_ACTION'): {'delay': dS},
 ('_condition_69', 'egress_mac_acl_ACTION'): {'delay': dS},
 ('_condition_70', 'int_outer_encap_ACTION'): {'delay': dS},
 ('_condition_71', 'egress_vlan_xlate_ACTION'): {'delay': dS},
 ('_condition_72', '_condition_73'): {'delay': dS},
 ('_condition_73', 'egress_filter_drop_ACTION'): {'delay': dS},
 ('_condition_74', 'egress_system_acl_ACTION'): {'delay': dS},
 ('egress_bd_map_ACTION', '_condition_65'): {'delay': dA},
 ('egress_bd_map_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('egress_bd_map_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('egress_bd_map_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('egress_bd_map_ACTION', 'smac_rewrite_MATCH'): {'delay': dA},
 ('egress_bd_map_MATCH', 'egress_bd_map_ACTION'): {'delay': dM},
 ('egress_bd_stats_MATCH', 'egress_bd_stats_ACTION'): {'delay': dM},
 ('egress_filter_ACTION', '_condition_73'): {'delay': dA},
 ('egress_ip_acl_ACTION', 'egress_system_acl_MATCH'): {'delay': dA},
 ('egress_ip_acl_MATCH', 'egress_ip_acl_ACTION'): {'delay': dM},
 ('egress_ipv6_acl_ACTION', 'egress_system_acl_MATCH'): {'delay': dA},
 ('egress_ipv6_acl_MATCH', 'egress_ipv6_acl_ACTION'): {'delay': dM},
 ('egress_l4_dst_port_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('egress_l4_dst_port_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('egress_l4_dst_port_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dS},
 ('egress_l4_dst_port_MATCH', 'egress_l4_dst_port_ACTION'): {'delay': dM},
 ('egress_l4_src_port_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('egress_l4_src_port_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('egress_l4_src_port_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dS},
 ('egress_l4_src_port_MATCH', 'egress_l4_src_port_ACTION'): {'delay': dM},
 ('egress_l4port_fields_ACTION', 'egress_l4_dst_port_MATCH'): {'delay': dA},
 ('egress_l4port_fields_ACTION', 'egress_l4_src_port_MATCH'): {'delay': dA},
 ('egress_l4port_fields_ACTION', 'tunnel_encap_process_inner_ACTION'): {'delay': dS},
 ('egress_l4port_fields_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('egress_l4port_fields_MATCH', 'egress_l4port_fields_ACTION'): {'delay': dM},
 ('egress_mac_acl_ACTION', 'egress_system_acl_MATCH'): {'delay': dA},
 ('egress_mac_acl_ACTION', 'egress_vlan_xlate_ACTION'): {'delay': dS},
 ('egress_mac_acl_MATCH', 'egress_mac_acl_ACTION'): {'delay': dM},
 ('egress_nat_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('egress_nat_ACTION', 'egress_l4port_fields_ACTION'): {'delay': dA},
 ('egress_nat_ACTION', 'int_outer_encap_ACTION'): {'delay': dS},
 ('egress_nat_ACTION', 'tunnel_dst_rewrite_ACTION'): {'delay': dA},
 ('egress_nat_ACTION', 'tunnel_encap_process_inner_ACTION'): {'delay': dA},
 ('egress_nat_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('egress_nat_ACTION', 'tunnel_src_rewrite_ACTION'): {'delay': dA},
 ('egress_nat_MATCH', 'egress_nat_ACTION'): {'delay': dM},
 ('egress_port_mapping_ACTION', '_condition_66'): {'delay': dA},
 ('egress_port_mapping_ACTION', '_condition_67'): {'delay': dA},
 ('egress_port_mapping_ACTION', '_condition_71'): {'delay': dA},
 ('egress_port_mapping_ACTION', '_condition_73'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'egress_filter_ACTION'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'egress_qos_map_MATCH'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'egress_vlan_xlate_MATCH'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'egress_vni_MATCH'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'int_outer_encap_MATCH'): {'delay': dA},
 ('egress_port_mapping_ACTION', 'tunnel_encap_process_outer_MATCH'): {'delay': dA},
 ('egress_port_mapping_MATCH', '_condition_58'): {'delay': dM},
 ('egress_port_mapping_MATCH', '_condition_59'): {'delay': dM},
 ('egress_port_mapping_MATCH', '_condition_61'): {'delay': dM},
 ('egress_port_mapping_MATCH', '_condition_62'): {'delay': dM},
 ('egress_port_mapping_MATCH', '_condition_63'): {'delay': dM},
 ('egress_port_mapping_MATCH', '_condition_65'): {'delay': dM},
 ('egress_port_mapping_MATCH', 'egress_bd_map_ACTION'): {'delay': dM},
 ('egress_port_mapping_MATCH', 'egress_bd_stats_ACTION'): {'delay': dM},
 ('egress_port_mapping_MATCH', 'egress_port_mapping_ACTION'): {'delay': dM},
 ('egress_port_mapping_MATCH', 'int_insert_ACTION'): {'delay': dM},
 ('egress_port_mapping_MATCH', 'mtu_ACTION'): {'delay': dM},
 ('egress_qos_map_ACTION', 'l3_rewrite_ACTION'): {'delay': dA},
 ('egress_qos_map_MATCH', 'egress_qos_map_ACTION'): {'delay': dM},
 ('egress_system_acl_MATCH', 'egress_system_acl_ACTION'): {'delay': dM},
 ('egress_vlan_xlate_MATCH', 'egress_vlan_xlate_ACTION'): {'delay': dM},
 ('egress_vni_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('egress_vni_MATCH', 'egress_vni_ACTION'): {'delay': dM},
 ('int_bos_ACTION', 'int_meta_header_update_ACTION'): {'delay': dS},
 ('int_bos_MATCH', 'int_bos_ACTION'): {'delay': dM},
 ('int_insert_ACTION', '_condition_64'): {'delay': dA},
 ('int_insert_ACTION', '_condition_70'): {'delay': dA},
 ('int_insert_ACTION', 'int_inst_0003_ACTION'): {'delay': dA},
 ('int_insert_ACTION', 'int_meta_header_update_MATCH'): {'delay': dA},
 ('int_insert_ACTION', 'int_outer_encap_ACTION'): {'delay': dA},
 ('int_insert_MATCH', 'int_insert_ACTION'): {'delay': dM},
 ('int_inst_0003_ACTION', 'int_bos_ACTION'): {'delay': dA},
 ('int_inst_0003_MATCH', 'int_inst_0003_ACTION'): {'delay': dM},
 ('int_inst_0407_ACTION', 'int_bos_ACTION'): {'delay': dA},
 ('int_inst_0407_MATCH', 'int_inst_0407_ACTION'): {'delay': dM},
 ('int_inst_0811_MATCH', 'int_inst_0811_ACTION'): {'delay': dM},
 ('int_inst_1215_MATCH', 'int_inst_1215_ACTION'): {'delay': dM},
 ('int_meta_header_update_MATCH', 'int_meta_header_update_ACTION'): {'delay': dM},
 ('int_outer_encap_MATCH', 'int_outer_encap_ACTION'): {'delay': dM},
 ('l3_rewrite_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('l3_rewrite_ACTION', 'egress_nat_ACTION'): {'delay': dS},
 ('l3_rewrite_ACTION', 'tunnel_dmac_rewrite_ACTION'): {'delay': dA},
 ('l3_rewrite_ACTION', 'tunnel_dst_rewrite_ACTION'): {'delay': dS},
 ('l3_rewrite_ACTION', 'tunnel_encap_process_inner_ACTION'): {'delay': dA},
 ('l3_rewrite_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('l3_rewrite_ACTION', 'tunnel_rewrite_ACTION'): {'delay': dA},
 ('l3_rewrite_MATCH', 'l3_rewrite_ACTION'): {'delay': dM},
 ('mirror_ACTION', '_condition_61'): {'delay': dA},
 ('mirror_ACTION', 'egress_bd_map_MATCH'): {'delay': dA},
 ('mirror_ACTION', 'egress_bd_stats_MATCH'): {'delay': dA},
 ('mirror_ACTION', 'egress_filter_ACTION'): {'delay': dA},
 ('mirror_ACTION', 'egress_ip_acl_ACTION'): {'delay': dA},
 ('mirror_ACTION', 'egress_ipv6_acl_ACTION'): {'delay': dA},
 ('mirror_ACTION', 'egress_mac_acl_ACTION'): {'delay': dA},
 ('mirror_ACTION', 'egress_system_acl_MATCH'): {'delay': dA},
 ('mirror_ACTION', 'egress_vlan_xlate_MATCH'): {'delay': dA},
 ('mirror_ACTION', 'egress_vni_MATCH'): {'delay': dA},
 ('mirror_ACTION', 'rewrite_MATCH'): {'delay': dA},
 ('mirror_ACTION', 'tunnel_rewrite_ACTION'): {'delay': dA},
 ('mirror_MATCH', 'mirror_ACTION'): {'delay': dM},
 ('mtu_ACTION', 'egress_system_acl_MATCH'): {'delay': dA},
 ('mtu_ACTION', 'int_outer_encap_ACTION'): {'delay': dS},
 ('mtu_ACTION', 'tunnel_encap_process_inner_ACTION'): {'delay': dS},
 ('mtu_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dS},
 ('mtu_ACTION', 'tunnel_mtu_ACTION'): {'delay': dA},
 ('mtu_MATCH', 'mtu_ACTION'): {'delay': dM},
 ('replica_type_ACTION', '_condition_61'): {'delay': dA},
 ('replica_type_ACTION', '_condition_63'): {'delay': dA},
 ('replica_type_ACTION', 'rewrite_ACTION'): {'delay': dA},
 ('replica_type_MATCH', 'replica_type_ACTION'): {'delay': dM},
 ('rewrite_ACTION', '_condition_63'): {'delay': dA},
 ('rewrite_ACTION', '_condition_66'): {'delay': dA},
 ('rewrite_ACTION', '_condition_67'): {'delay': dA},
 ('rewrite_ACTION', '_condition_73'): {'delay': dA},
 ('rewrite_ACTION', 'egress_bd_map_MATCH'): {'delay': dA},
 ('rewrite_ACTION', 'egress_bd_stats_MATCH'): {'delay': dA},
 ('rewrite_ACTION', 'egress_filter_ACTION'): {'delay': dA},
 ('rewrite_ACTION', 'egress_vlan_xlate_MATCH'): {'delay': dA},
 ('rewrite_ACTION', 'egress_vni_MATCH'): {'delay': dA},
 ('rewrite_ACTION', 'int_outer_encap_MATCH'): {'delay': dA},
 ('rewrite_ACTION', 'l3_rewrite_ACTION'): {'delay': dA},
 ('rewrite_ACTION', 'mtu_MATCH'): {'delay': dA},
 ('rewrite_ACTION', 'tunnel_encap_process_outer_MATCH'): {'delay': dA},
 ('rewrite_ACTION', 'tunnel_mtu_MATCH'): {'delay': dA},
 ('rewrite_ACTION', 'tunnel_rewrite_MATCH'): {'delay': dA},
 ('rewrite_MATCH', 'rewrite_ACTION'): {'delay': dM},
 ('rewrite_multicast_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('rewrite_multicast_ACTION', 'egress_nat_ACTION'): {'delay': dS},
 ('rewrite_multicast_ACTION', 'l3_rewrite_ACTION'): {'delay': dA},
 ('rewrite_multicast_ACTION', 'tunnel_dmac_rewrite_ACTION'): {'delay': dA},
 ('rewrite_multicast_ACTION', 'tunnel_dst_rewrite_ACTION'): {'delay': dS},
 ('rewrite_multicast_ACTION', 'tunnel_encap_process_inner_ACTION'): {'delay': dS},
 ('rewrite_multicast_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('rewrite_multicast_MATCH', 'rewrite_multicast_ACTION'): {'delay': dM},
 ('rid_ACTION', '_condition_60'): {'delay': dA},
 ('rid_ACTION', '_condition_61'): {'delay': dA},
 ('rid_ACTION', '_condition_63'): {'delay': dA},
 ('rid_ACTION', '_condition_66'): {'delay': dA},
 ('rid_ACTION', '_condition_67'): {'delay': dA},
 ('rid_ACTION', '_condition_72'): {'delay': dA},
 ('rid_ACTION', '_condition_73'): {'delay': dA},
 ('rid_ACTION', 'egress_bd_map_MATCH'): {'delay': dA},
 ('rid_ACTION', 'egress_bd_stats_MATCH'): {'delay': dA},
 ('rid_ACTION', 'egress_filter_ACTION'): {'delay': dA},
 ('rid_ACTION', 'egress_port_mapping_ACTION'): {'delay': dA},
 ('rid_ACTION', 'egress_vlan_xlate_MATCH'): {'delay': dA},
 ('rid_ACTION', 'egress_vni_MATCH'): {'delay': dA},
 ('rid_ACTION', 'int_outer_encap_MATCH'): {'delay': dA},
 ('rid_ACTION', 'replica_type_MATCH'): {'delay': dA},
 ('rid_ACTION', 'rewrite_ACTION'): {'delay': dA},
 ('rid_ACTION', 'tunnel_encap_process_outer_MATCH'): {'delay': dA},
 ('rid_ACTION', 'tunnel_mtu_MATCH'): {'delay': dA},
 ('rid_ACTION', 'tunnel_rewrite_MATCH'): {'delay': dA},
 ('rid_MATCH', 'rid_ACTION'): {'delay': dM},
 ('smac_rewrite_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('smac_rewrite_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('smac_rewrite_ACTION', 'tunnel_smac_rewrite_ACTION'): {'delay': dA},
 ('smac_rewrite_MATCH', 'smac_rewrite_ACTION'): {'delay': dM},
 ('tunnel_decap_process_inner_ACTION', 'egress_l4port_fields_MATCH'): {'delay': dA},
 ('tunnel_decap_process_inner_ACTION', 'egress_nat_ACTION'): {'delay': dA},
 ('tunnel_decap_process_inner_ACTION', 'int_outer_encap_ACTION'): {'delay': dA},
 ('tunnel_decap_process_inner_ACTION', 'tunnel_encap_process_inner_MATCH'): {'delay': dA},
 ('tunnel_decap_process_inner_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('tunnel_decap_process_inner_MATCH', 'tunnel_decap_process_inner_ACTION'): {'delay': dM},
 ('tunnel_decap_process_outer_ACTION', '_condition_68'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', '_condition_69'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'egress_nat_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'egress_vlan_xlate_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'int_outer_encap_MATCH'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'l3_rewrite_MATCH'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'mtu_MATCH'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'rewrite_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'rewrite_multicast_MATCH'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'smac_rewrite_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'tunnel_dmac_rewrite_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'tunnel_dst_rewrite_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'tunnel_encap_process_inner_MATCH'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'tunnel_rewrite_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'tunnel_smac_rewrite_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_ACTION', 'tunnel_src_rewrite_ACTION'): {'delay': dA},
 ('tunnel_decap_process_outer_MATCH', 'tunnel_decap_process_outer_ACTION'): {'delay': dM},
 ('tunnel_dmac_rewrite_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('tunnel_dmac_rewrite_MATCH', 'tunnel_dmac_rewrite_ACTION'): {'delay': dM},
 ('tunnel_dst_rewrite_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('tunnel_dst_rewrite_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('tunnel_dst_rewrite_MATCH', 'tunnel_dst_rewrite_ACTION'): {'delay': dM},
 ('tunnel_encap_process_inner_ACTION', '_condition_68'): {'delay': dA},
 ('tunnel_encap_process_inner_ACTION', '_condition_69'): {'delay': dA},
 ('tunnel_encap_process_inner_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('tunnel_encap_process_inner_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('tunnel_encap_process_inner_ACTION', 'int_outer_encap_MATCH'): {'delay': dA},
 ('tunnel_encap_process_inner_ACTION', 'tunnel_dst_rewrite_ACTION'): {'delay': dA},
 ('tunnel_encap_process_inner_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('tunnel_encap_process_inner_ACTION', 'tunnel_mtu_ACTION'): {'delay': dA},
 ('tunnel_encap_process_inner_ACTION', 'tunnel_src_rewrite_ACTION'): {'delay': dA},
 ('tunnel_encap_process_inner_MATCH', 'tunnel_encap_process_inner_ACTION'): {'delay': dM},
 ('tunnel_encap_process_outer_ACTION', '_condition_68'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', '_condition_69'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'egress_system_acl_ACTION'): {'delay': dS},
 ('tunnel_encap_process_outer_ACTION', 'egress_vlan_xlate_ACTION'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'int_outer_encap_MATCH'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'tunnel_dmac_rewrite_ACTION'): {'delay': dS},
 ('tunnel_encap_process_outer_ACTION', 'tunnel_dst_rewrite_ACTION'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'tunnel_mtu_MATCH'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'tunnel_rewrite_MATCH'): {'delay': dA},
 ('tunnel_encap_process_outer_ACTION', 'tunnel_smac_rewrite_ACTION'): {'delay': dS},
 ('tunnel_encap_process_outer_ACTION', 'tunnel_src_rewrite_ACTION'): {'delay': dA},
 ('tunnel_encap_process_outer_MATCH', 'tunnel_encap_process_outer_ACTION'): {'delay': dM},
 ('tunnel_mtu_ACTION', 'egress_system_acl_MATCH'): {'delay': dA},
 ('tunnel_mtu_MATCH', 'tunnel_mtu_ACTION'): {'delay': dM},
 ('tunnel_rewrite_ACTION', 'egress_filter_ACTION'): {'delay': dA},
 ('tunnel_rewrite_ACTION', 'egress_ip_acl_ACTION'): {'delay': dS},
 ('tunnel_rewrite_ACTION', 'egress_ipv6_acl_ACTION'): {'delay': dS},
 ('tunnel_rewrite_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('tunnel_rewrite_ACTION', 'egress_system_acl_ACTION'): {'delay': dS},
 ('tunnel_rewrite_ACTION', 'egress_vlan_xlate_ACTION'): {'delay': dA},
 ('tunnel_rewrite_ACTION', 'tunnel_dmac_rewrite_MATCH'): {'delay': dA},
 ('tunnel_rewrite_ACTION', 'tunnel_dst_rewrite_MATCH'): {'delay': dA},
 ('tunnel_rewrite_ACTION', 'tunnel_smac_rewrite_MATCH'): {'delay': dA},
 ('tunnel_rewrite_ACTION', 'tunnel_src_rewrite_MATCH'): {'delay': dA},
 ('tunnel_rewrite_MATCH', 'tunnel_rewrite_ACTION'): {'delay': dM},
 ('tunnel_smac_rewrite_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('tunnel_smac_rewrite_MATCH', 'tunnel_smac_rewrite_ACTION'): {'delay': dM},
 ('tunnel_src_rewrite_ACTION', 'egress_ip_acl_MATCH'): {'delay': dA},
 ('tunnel_src_rewrite_ACTION', 'egress_ipv6_acl_MATCH'): {'delay': dA},
 ('tunnel_src_rewrite_MATCH', 'tunnel_src_rewrite_ACTION'): {'delay': dM},
 ('vlan_decap_ACTION', 'egress_mac_acl_MATCH'): {'delay': dA},
 ('vlan_decap_ACTION', 'egress_vlan_xlate_ACTION'): {'delay': dA},
 ('vlan_decap_ACTION', 'tunnel_decap_process_outer_ACTION'): {'delay': dA},
 ('vlan_decap_ACTION', 'tunnel_encap_process_outer_ACTION'): {'delay': dA},
 ('vlan_decap_ACTION', 'tunnel_rewrite_ACTION'): {'delay': dA},
 ('vlan_decap_MATCH', 'vlan_decap_ACTION'): {'delay': dM}}

# Number of processors in system
num_procs = 12

# Match key and action field limit for each processor
# We assume the processors don't share resources for now
action_fields_limit = 32
match_unit_limit = 8
match_unit_size  = 80

# Throughput required
throughput = 1.0
