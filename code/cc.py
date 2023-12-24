import sys
import os
import argparse
from utils import Graph

# Connected components (cc)
# Given: A simple graph with n≤10^3 vertices in the edge list format
# Return: The number of connected components in the graph.

def dfs(G):
    cc = [0]      # identifier for connected component
    visited = [False] * len(G.nodes)

    def explore(G, u):
        visited[u-1] = True
        if u in G.edges.keys():
            for v in G.edges[u]:
                if visited[v-1] == False:
                    explore(G, v)

    for v in G.nodes:
        if visited[v-1] == False:
            cc[0] += 1
            explore(G, v)

    print(cc[0])

def cc(input_file):
    G = Graph().generate_from_edge_list_file(input_file)
    dfs(G)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="path to input file")
    parser.add_argument("-o", "--output", action="store_true", help="Flag to enable output")
    args = parser.parse_args()

    # save answer to file
    input_file = args.input_file
    output_flag = args.output  # Set to False to not output the result

    cc(input_file)

    if output_flag:
        output_file_path = "output/" + os.path.basename(input_file)
        with open(output_file_path, 'w') as output_file:
            sys.stdout = output_file  # Redirect stdout to output_file
            cc(input_file)

