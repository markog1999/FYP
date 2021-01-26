from math import sqrt
from Grid import *

def simplePath(start, end, grid, path):
    if start == end:
        path.append(start)
        return path
    else:
        grid.getNode(start).SetAvailability(False)
        path.append(start)
        start_node = grid.getNode(start)
        next_node = None
        start_node.UpdateAvailableNodes()
        next_node = nextStep(start_node,end)
        return simplePath(next_node,end, grid, path)

def distance(coords1,coords2):

    x1 = coords1[0]
    x2 = coords2[0]
    y1 = coords1[1]
    y2 = coords2[1]
    z1 = coords1[2]
    z2 = coords2[2]

    distance = sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return distance

def nextStep(node,end):
    # calculates next step by finding available node with minimum distance
    dist = float('inf')
    next_step = None
    for step in node.GetAvailableNodes():
        if distance(step,end) < dist:
            dist = distance(step,end)
            next_step = step
    return next_step
