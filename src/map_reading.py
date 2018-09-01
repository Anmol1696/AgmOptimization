import networkx as nx

def read_map_file(mapfile_name):
    """
        Return all the lines from the map file, which will later feed into the graph to fill it
        Some pre-processing is also done before returning the file
    """
    with open(mapfile_name) as file_open:
        all_lines = file_open.readlines()

    for index in range(len(all_lines)):
        all_lines[index] = all_lines[index].split('\n')[0].split(' ')

    return all_lines

def populate_graph(all_lines):
    """
        all_lines is the output of the read_map_file function
        Output is a graph which will be replaced by the map
    """

    graph = nx.Graph()

    for node_index in range(len(all_lines)):
        for destination, distance, runway_type in zip(*[iter(all_lines[node_index])]*3):
            graph.add_edge(int(node_index), int(destination))
            graph[int(node_index)][int(destination)]['distance']=int(distance)
            graph[int(node_index)][int(destination)]['runway_type']=runway_type

    return graph

def get_all_paths(graph, source, destination):
    return [x for x in nx.all_simple_paths(graph, source, destination)]

if __name__ == "__main__":
    map_file = "data/mum_airport_full_map.txt"

    all_lines  = read_map_file(map_file)
    g = populate_graph(all_lines)
    print g.edges()
    print g[0]

    print get_all_paths(g, 0, 39)
