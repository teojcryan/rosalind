import sys
import os
import argparse

# Breadth-First Search (bfs)
# Given: A simple graph with n≤10^3 vertices in the edge list format
# Return: An array D[1..n] where D[i] is the length of the shortest path from vertex 1 to i. D[1] = 0. 
#         D[i] = -1 if i is not reachable from 1.

def bfs(input_file):
    edge_list, dir_list = [], []

    with open(input_file, 'r') as file:
        lines = file.read().split("\n")

        n_vertices, n_edges = map(int, lines[0].split(" "))
        lines = [i for i in lines[1:] if i != '']
        
        # obtain edge list in tuple format
        for line in lines:
            edge_list.append(tuple(map(int, line.split(" "))))

        # populate direction list
        for vertex in range(1, n_vertices+1):
            neighbours = []
            for edge in edge_list:
                if vertex == edge[0]:
                    neighbours.append(edge[1])
            dir_list.append(neighbours)
        
        s = 1
        D = [-1] * n_vertices # distance array
        D[s-1] = 0 
        Q = [s] # initiate queue
        while Q:
            u = Q.pop(0)
            for v in dir_list[u-1]:
                if D[v-1] == -1:
                    Q.append(v)
                    D[v-1] = D[u-1] + 1

        print(' '.join(str(i) for i in D))                                      

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="path to input file")
    parser.add_argument("-o", "--output", action="store_true", help="Flag to enable output")
    args = parser.parse_args()

    # save answer to file
    input_file = args.input_file
    output_flag = args.output  # Set to False to not output the result

    bfs(input_file)

    if output_flag:
        output_file_path = "output/" + os.path.basename(input_file)
        with open(output_file_path, 'w') as output_file:
            sys.stdout = output_file  # Redirect stdout to output_file
            bfs(input_file)

