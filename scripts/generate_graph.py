#! /usr/bin/python
import sys
import networkx as nx

def parse_graph(trace_line):
        G = nx.DiGraph();
        tokens = trace_line.split();
        if len(tokens) < 1:
                return None;
        for i in range(0, len(tokens)-1):
               G.add_edge(tokens[i], tokens[i+1]);
        return G;

def merge_graph(graph_list, delta):
        G = graph_list[0];
        keys = map(lambda x: x, G.node);
        for k in keys:
                G.node[k]['size'] = delta;
        for tmp_g in graph_list[1:]:
                for edge in tmp_g.edges():
                        if G.has_edge(*edge):
                                #src
                                G.node[edge[0]]['size'] = G.node[edge[0]]['size'] + delta;
                                #des
                                G.node[edge[1]]['size'] = G.node[edge[1]]['size'] + delta;
                        else:
                                G.add_edge(*edge);
                                #node src exists:
                                if G.node[edge[0]].has_key('size'):
                                        G.node[edge[0]]['size'] = G.node[edge[0]]['size'] + delta;
                                else: #node src not exists
                                        G.node[edge[0]]['size'] = delta;
                                #node des exists:
                                if G.node[edge[1]].has_key('size'):
                                        G.node[edge[1]]['size'] = G.node[edge[1]]['size'] + delta;
                                else: #node des not exists:
                                        G.node[edge[1]]['size'] = delta;
                                
        return G;

def eliminate_graph(G, threshold):
        for node_key in G.nodes():
                if G.node[node_key]['size'] < threshold:
                        G.remove_node(node_key);
        return G;
                                

def usage():
        print 'generate_graph.py input_file1 input_file2 ... output_file';

def main(argv):
        if len(argv) < 2:
                usage();
                sys.exit(-1);

if __name__ == '__main__':
        main(argv[1:]);
