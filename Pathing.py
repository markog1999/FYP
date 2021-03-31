from typing import List
from Grid import *
from math import sqrt
from Route import RouteObject


# TODO: This implementation always waits to access node in the "right" direction, implement a version which searches
#  for faster paths
def DirectPath(start_coords: tuple, end_coords: tuple, start_time: float, grid: Array3D):

    start_node: GridNode = grid.getNode(start_coords)

    # TODO: Implement variable traverse duration based on distance between nodes and drone capabilities
    node_weights = {start_node: 0}

    # First establish the shortest path geometrically
    direct_path: List[tuple] = [start_coords]
    path_times: List[tuple] = []
    current_step = start_coords
    while current_step != end_coords: # TODO: Assumes a path exists from start to end, implement handling if this is not the case
        adjacents = grid.getNode(current_step).GetAdjacents()
        distances = [distance(end_coords, x) for x in adjacents]
        next_step = adjacents[(distances).index(min(distances))]
        direct_path.append(next_step)
        current_step = next_step


    current_search_start_time = start_time
    i = 1
    while i < len(direct_path):
        nodes_travel_time = 100
        node1 =  grid.getNode(direct_path[i-1])
        node2 = grid.getNode((direct_path[i]))

        current_search_start_time = find_flight_window(node1,node2, current_search_start_time, nodes_travel_time)
        path_times.append((current_search_start_time, (current_search_start_time + nodes_travel_time)))
        current_search_start_time += nodes_travel_time
        i+=1

    route_object = RouteObject(direct_path,path_times)
    return route_object

def OptimisedPath(start_coords: tuple, end_coords: tuple, start_time: float, grid: Array3D):
    # Assume constant flight time of 100s TODO: Implement distance-adjusted flight time
    direct_route = DirectPath(start_coords, end_coords, start_time, grid)
    direct_duration = direct_route.endTime()
    start_node = grid.getNode(start_coords)

    # This will be a dictionary of each node checked and the best time to reach it
    node_weights = {start_coords:0}
    # This list will hold nodes yet to be checked, initialised with neighbours of the starting point
    unvisited_nodes = []
    unvisited_nodes.extend(start_node.GetAdjacents())


    for node in unvisited_nodes:
        node_object: GridNode = grid.getNode(node)
        adjacents = node_object.GetAdjacents()
        weights = []
        for neighbour in adjacents:
            if neighbour in node_weights:
                weights.append((neighbour,node_weights[neighbour]))

        best_neighbour = min(weights, key = lambda x: x[1])
        node_weight = find_flight_window(grid.getNode(best_neighbour[0]), grid.getNode(node), best_neighbour[1], 100)+100
        node_weights[node] = node_weight

        # If node is within bounds, add its neighbours (that are "further away") to be checked
        if node_weight <= direct_duration:
            for node in adjacents:
                # Check if node is already in dictionary, to avoid overwriting better paths
                if node in node_weights:
                    if node_weights[node] > node_weight:
                        if node not in unvisited_nodes:
                            unvisited_nodes.append(node)
                else:
                    if node not in unvisited_nodes:
                        unvisited_nodes.append(node)


    # Now that we have built a dictionary of nodes and the time taken to reach them, work backwards from the end,
    # taking the best option at each step.
    path = [end_coords]
    times = [(node_weights[end_coords], node_weights[end_coords]+100)]

    while 1:
        possible_steps_weights = []
        neighbours = grid.getNode(path[0]).GetAdjacents()
        for next_step in neighbours: #Get the neighbours of the last step (front of the path)
            possible_steps_weights.append(node_weights[next_step])
        best_next_step = min(tuple(zip(neighbours, possible_steps_weights)), key = lambda x: x[1])
        path.insert(0,best_next_step[0])
        if path[0] == start_coords:
            break

        times.insert(0,(best_next_step[1], best_next_step[1]+100))

    return RouteObject(path,times)

def find_flight_window(node1: GridNode, node2: GridNode, search_start_time: float, flight_duration: float):
    while 1:
        # Find the time that the first node could start the flight
        first_node_window = node1.NextAvailableTime(search_start_time, flight_duration)
        # find the nearest time after this that the second node could begin the flight
        second_node_window = node2.NextAvailableTime(first_node_window, flight_duration)

        # if the second window is within the same interval as the first,
        check = node1.NextAvailableTime(second_node_window, flight_duration)
        if check == second_node_window:
            return second_node_window
        else:
            search_start_time = second_node_window

def nextStep(node: GridNode, end: tuple):
    # calculates next step by finding available node with minimum distance
    dist = float('inf')
    next_step = None
    for step in node.GetAdjacents():
        if distance(step, end) < dist:
            dist = distance(step, end)
            next_step = step
    return next_step

def distance(coords1, coords2):
    x1 = coords1[0]
    x2 = coords2[0]
    y1 = coords1[1]
    y2 = coords2[1]
    z1 = coords1[2]
    z2 = coords2[2]

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
