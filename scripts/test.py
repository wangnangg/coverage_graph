#! /usr/bin/python
from generate_graph import parse_graph
from generate_graph import merge_graph
from generate_graph import eliminate_graph
import matplotlib.pyplot as plt
import networkx as nx
import sys
def test1(argv):
        f = open(argv[0]);
        G_list = [];
        line = f.readline();
        while line:
                G = parse_graph(line);
                if G:
                        G_list.append(G);
                line = f.readline();
        f.close();
        G = merge_graph(G_list, 1);
        G = eliminate_graph(G, 10);
        size_list = [];
        for node_key in G.nodes():
                size_list.append(G.node[node_key]['size']);
	pos = nx.graphviz_layout(G);
        nx.draw(G, pos, node_size=size_list, with_labels=False, width=0.3);
        plt.savefig("abc");



test1(sys.argv[1:])
