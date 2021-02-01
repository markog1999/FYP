import time as time


class GridNode:
    def __init__(self, gridPointer, x, y, z):
        self._grid = gridPointer  # The parent grid of the node
        self._coord = (x, y, z)  # co-ordinates within the parent grid
        self._occupiedTimes = []  # a list of tuples, [(start,end)] , indicating times node is occupied
        self._adjacentNodes = []  # other nodes which can be reached directly from this node

    # Add a node (tuple representing their co-ordinates) which can be reached directly from this node
    def AddAdjacent(self, new: tuple):
        self._adjacentNodes.append(new)

    # Re
    def GetAdjacents(self):
        return self._adjacentNodes
    
    def CheckAvailability(self, start: float, end: float):  # Start and end should be times in seconds since Unix time
        # TODO: Implement a binary search for speed
        i = 0
        while i <= len(self._occupiedTimes):
            if (self._occupiedTimes[i])[1] > start:
                i += 1
                continue
            elif (self._occupiedTimes[i])[1] < start:
                if (self._occupiedTimes[i + 1])[0] <= end:
                    raise Exception("Overlap between timestamps")
                else:
                    self._occupiedTimes.insert(i + 1, (start, end))

    # Add a tuple to the node representing a period of time that the node will be occupied
    def OccupyTime(self, start: float, end: float):  # Start and end should be times in seconds since Unix time
        # TODO: Implement a binary search to speed up insertion
        i = 0
        while i <= len(self._occupiedTimes):
            if (self._occupiedTimes[i])[1] > start:
                i += 1
                continue
            elif (self._occupiedTimes[i])[1] < start:
                if (self._occupiedTimes[i + 1])[0] <= end:
                    raise Exception("Overlap between timestamps")
                else:
                    self._occupiedTimes.insert(i + 1, (start, end))

    # Get co-ordinates of the node
    def GetCoords(self):
        return self._coord

    def __str__(self):
        return str(self._coord)


class Array3D:
    def __init__(self, xLimit, yLimit, zLimit):
        self.Array = []
        i = 0
        while i < xLimit:
            self.Array.append([])
            j = 0
            while j < yLimit:
                self.Array[i].append([])
                k = 0
                while k < zLimit:
                    newNode = GridNode(self, i, j, k)
                    self.Array[i][j].append(newNode)
                    if (i - 1) > 0:
                        newNode.AddAdjacent((i - 1, j, k))
                    if (i + 1) < xLimit:
                        newNode.AddAdjacent((i + 1, j, k))
                    if (j - 1) > 0:
                        newNode.AddAdjacent((i, j - 1, k))
                    if (j + 1) < zLimit:
                        newNode.AddAdjacent((i, j + 1, k))
                    if (k - 1) > 0:
                        newNode.AddAdjacent((i, j, k - 1))
                    if (k + 1) < zLimit:
                        newNode.AddAdjacent((i, j, k + 1))

                    k += 1
                j += 1
            i += 1

    def getNode(self, coords):
        x = coords[0]
        y = coords[1]
        z = coords[2]
        Node = self.Array[x][y][z]
        return Node

    def __str__(self):
        result = ""
        for i in self.Array:
            for j in i:
                for k in j:
                    result += str(k)
                    result += " "
            result += " \n"
        return result
