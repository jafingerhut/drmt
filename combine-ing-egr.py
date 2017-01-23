#! /usr/bin/env python

# Given 2 input files, one for ingress nodes and edges, the other with
# egress nodes and edges, combine them while uniquifying their node
# names.

# ingress node names are changed from '_condition_<foo>' to
# '_condition_ing_<foo>' for condition nodes, and otherwise prepended
# with 'ing_'.

# egress nodes are renamed similarly, except with 'egr_' instead of
# 'ing_'.

import sys
import pprint as pp
import re
import copy


if len(sys.argv) != 3:
    print('usage: %s <ing_sched_data_fname> <egr_sched_data_fname>'
          '' % sys.argv[0], file=sys.stderr)
    sys.exit(1)
ing_fname = sys.argv[1]
egr_fname = sys.argv[2]


def rename_nodes(nodes, edges, prepend_str):
    
    orig_node_name = {}
    modified_node_name = {}
    new_nodes = {}
    new_edges = {}
    
    for node_name in nodes:
        node_dat = nodes[node_name]
        assert(len(node_dat) != 0)
        new_node_name = None
    
        condition_node = re.match(r"^(_condition_)(.*)$", node_name)
        if condition_node:
            new_node_name = (condition_node.group(1) +
                             prepend_str + condition_node.group(2))
        if new_node_name is None:
            new_node_name = prepend_str + node_name

        assert(new_node_name)
        if node_name in orig_node_name:
            print('internal error: saw orig node name %s multiple times'
                  '' % (node_name))
            sys.exit(1)
        # Make sure we are not introducing any name collisions
        if new_node_name in modified_node_name:
            print('internal error: tried to use new node name %s multiple times'
                  '' % (new_node_name))
            sys.exit(1)
    
        modified_node_name[node_name] = new_node_name
        orig_node_name[new_node_name] = node_name
    
        new_nodes[new_node_name] = node_dat
    
    for edge in edges:
        edge_dat = edges[edge]
    
        assert(isinstance(edge, tuple))
        assert(len(edge) == 2)
        assert(isinstance(edge[0], str))
        assert(isinstance(edge[1], str))
        assert(edge[0] in modified_node_name)
        assert(edge[1] in modified_node_name)
        new_edge = (modified_node_name[edge[0]], modified_node_name[edge[1]])
    
        new_edges[new_edge] = edge_dat

    return new_nodes, new_edges


def combine_dicts_check_keys_unique(d1, d2):
    new_d = copy.deepcopy(d1)
    for k in d2:
        assert(k not in new_d)
        new_d[k] = d2[k]
    return new_d


exec(open(ing_fname).read())
ing_nodes = nodes
ing_edges = edges

exec(open(egr_fname).read())
egr_nodes = nodes
egr_edges = edges

new_ing_nodes, new_ing_edges = rename_nodes(ing_nodes, ing_edges, 'ing_')
new_egr_nodes, new_egr_edges = rename_nodes(egr_nodes, egr_edges, 'egr_')

new_nodes = combine_dicts_check_keys_unique(new_ing_nodes, new_egr_nodes)
new_edges = combine_dicts_check_keys_unique(new_ing_edges, new_egr_edges)

print('nodes = \\')
pp.pprint(new_nodes)

print('\nedges = \\')
pp.pprint(new_edges)
