#! /usr/bin/python
from generate_graph import parse_graph
from generate_graph import merge_graph
from generate_graph import eliminate_graph
import matplotlib.pyplot as plt
import networkx as nx
import sys
def test1(argv):
        trace_file = argv[0];        
        G = parse_graph(trace_file);
        nx.write_graphml(G, 'file.xml');



test1(sys.argv[1:])
