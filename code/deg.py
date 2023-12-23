import sys
import os

# Degree Array (deg)
# Given: A simple graph with n≤10^3 vertices in the edge list format
# Return: An array D[1..n] where D[i] is the degree of vertex i

def deg(input_file):
    edge_list = []
    with open(input_file, 'r') as file:
        lines = file.read().split("\n")
        lines = [i for i in lines[1:] if i != '']
        
        # obtain vertice labels (in case not natural numbers)
        verts = set(map(int, ' '.join(lines).split(" ")))
        
        # obtain edge list in tuple format
        for line in lines:
            edge_list.append(tuple(map(int, line.split(" "))))

        # observe that the deg of a vert is the number of occurrences in a flattened edge list
        edge_list_flat = [i for edge in edge_list for i in edge]

        deg_array = []
        for vert in verts:
            deg_array.append(str(len([i for i in edge_list_flat if i == vert])))

        print(' '.join(deg_array))

if __name__ == "__main__":
    input_file = sys.argv[1]

    # print answer
    deg(input_file)

    # save answer to file
    output_file_path = "output/" + os.path.basename(input_file)
    with open(output_file_path, 'w') as output_file:
        sys.stdout = output_file  # Redirect stdout to output_file
        deg(input_file)
