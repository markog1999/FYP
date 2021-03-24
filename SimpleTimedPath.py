from typing import List

from Grid import *
from math import sqrt


# TODO: This implementation always waits to access node in the "right" direction, implement a version which searches
#  for faster paths
def DirectPath(start_coords: tuple, end_coords: tuple, start_time: float, grid: Array3D):

    start_node: GridNode = grid.getNode(start_coords)

    # TODO: Implement variable traverse duration based on distance between nodes and drone capabilities
    node_weights = {start_node: 0}

    # First establish the shortest path geometrically
    direct_path: List[tuple] = [start_coords]
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
        node1 =  grid.getNode(direct_path[i-1])
        node2 = grid.getNode((direct_path[i]))

        current_search_start_time = find_flight_window(node1,node2, current_search_start_time, 100)
        node1.OccupyTime(current_search_start_time, (current_search_start_time + 100))


        i+=1

    # return direct_path, start_time, current_search_start_time + 100
    return (current_search_start_time + 100) - start_time # Temporary output for testing, returns path travel duration

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
