from Grid import *

class RouteObject:
    def __init__(self):
        self._nodes = []
        self._times = []

    def __init__(self, nodes, times):
        self._nodes = nodes
        self._times = times

    def nodes(self):
        return self._nodes

    def times(self):
        return self._times

    def commit(self, grid):
        i = 0
        for node in (self._nodes[:-1]):
            node_object = grid.getNode(node)
            interval = self._times[i]
            node_object.OccupyTime(interval[0],interval[1])
            i += 1

    def endTime(self):
        if len(self._times) == 0:
            return 0
        else:
            return self._times[-1][-1]

    def startTime(self):
        if len(self._times) == 0:
            return 0
        else:
            return self._times[0][0]

    def duration(self):
        if len(self._times) == 0:
            return 0
        else:
            return (self._times[-1][-1]) - (self._times[0][0])