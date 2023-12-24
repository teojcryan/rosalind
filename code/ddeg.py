import sys
import os
import argparse

# Double-Degree Array (ddeg)
# Given: A simple graph with n≤10^3 vertices in the edge list format
# Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbours

def ddeg(input_file):
    edge_list, neighbour_deg_list = [], []

    with open(input_file, 'r') as file:
        lines = file.read().split("\n")

        n_vertices, n_edges = map(int, lines[0].split(" "))
        lines = [i for i in lines[1:] if i != '']
        
        # obtain edge list in tuple format
        for line in lines:
            edge_list.append(tuple(map(int, line.split(" "))))
        
        edge_list_flat = [item for sublist in edge_list for item in sublist]

        # populate adjacency list
        for vertex in range(1, n_vertices+1):
            neighour_deg = 0
            for edge in edge_list:
                if vertex in edge:
                    neighour_deg += edge_list_flat.count(edge[0] if edge[1] == vertex else edge[1])
            neighbour_deg_list.append(str(neighour_deg))
            
        print(' '.join(neighbour_deg_list))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="path to input file")
    parser.add_argument("-o", "--output", action="store_true", help="Flag to enable output")
    args = parser.parse_args()

    # save answer to file
    input_file = args.input_file
    output_flag = args.output  # Set to False to not output the result

    ddeg(input_file)

    if output_flag:
        output_file_path = "output/" + os.path.basename(input_file)
        with open(output_file_path, 'w') as output_file:
            sys.stdout = output_file  # Redirect stdout to output_file
            ddeg(input_file)

