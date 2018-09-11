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

def takeoff_landing_constrains(graph, path, takeoff_landing_distance):
    """
        Given a path as a list of nodes, returns true or false accordingly
        Return True if there exists a continuous runway of atleast the given distance
    """
    total_continuous_runway = [0]
    total_index = 0
    previous_runway = graph[path[0]][path[1]]['runway_type']

    for i in range(len(path)-1):
        temp_type = graph[path[i]][path[i+1]]['runway_type']
        temp_dist = graph[path[i]][path[i+1]]['distance']
         
        if previous_runway == temp_type and 'R' in temp_type:
            total_continuous_runway[total_index] += temp_dist

        if previous_runway != temp_type:
            previous_runway = temp_type

            if 'R' in temp_type:
                total_continuous_runway.append(temp_dist)
            else:
                total_continuous_runway.append(0)
            
            total_index += 1
            runway_type = temp_type

        if 'R' not in temp_type:
            previous_runway = 'T'

    print 'R->', total_continuous_runway

    if max(total_continuous_runway) > takeoff_landing_distance:
        return True
    
    return False

def get_all_paths_with_constrains(graph, source, destination, takeoff_landing_distance):
    """
        This function will call the get_all_paths and the takeoff_landing_constrains functions
    """
    all_path_constrains = []

    for path in get_all_paths(graph, source, destination):
        print path
        if takeoff_landing_constrains(graph, path, takeoff_landing_distance):
            all_path_constrains.append(path)

    return all_path_constrains

if __name__ == "__main__":
    map_file = "data/mum_airport_full_map.txt"

    all_lines  = read_map_file(map_file)
    g = populate_graph(all_lines)
    print g.edges()
    print g[4]
    #print g[0][22]

    #print get_all_paths(g, 0, 39)
    
    p = [0, 1, 2, 3, 19, 18, 17, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print takeoff_landing_constrains(g, p, 20)
    
    """ 
    test_f = get_all_paths_with_constrains(g, 0, 13, 20)
    print test_f
    print len(test_f)
    """
