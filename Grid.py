
import time as time

class GridNode:
    def __init__(self, gridPointer, x, y, z):
        self._grid = gridPointer
        self._coord = (x, y, z)
        self._occupiedTimes = []
        self._unOccupiedTimes = []
        self._adjacentNodes = []

    def AddAdjacent(self, new: tuple):
        self._adjacentNodes.append(new)

    def GetAdjacents(self):
        return self._adjacentNodes

    def CheckAvailability(self, start, end):
    # TODO: Optimise, use binary search or similar
    # In order to affirm that the time is available, we must check that there is no previous timestamp between start/end
        i = 0

        # This loop checks that another drone does not begin "occupying" the node in between start and end times.
        while i < len(self._occupiedTimes):
            timeStamp = self._occupiedTimes[i]
            if timeStamp < start:
                i += 1
                continue
            if timeStamp > start:
                if timeStamp <= end:
                    return False #TODO: Instead, return time until node becomes available
                if timeStamp > end:
                    break
            if timeStamp == start:
                return False #TODO: Instead, return time until node becomes available


    def OccupyTime(self, start, end):
        # TODO: Optimise, use binary search or similar to find insertion index faster
        def InsertTime(time, list):
            i = 0
            while i < len(list):
                if list[i] == time:
                    raise Exception(f"Timestamp cannot be inserted into GridNode at {self._coord}, stamp already recorded")
                elif list[i] < time:
                    i += 1
                    continue
                elif list[i] > time:
                    list.insert(i, time)
                    break

        if (self.CheckAvailability(start, end)):
            InsertTime(start, self._occupiedTimes)
            InsertTime(start, self._unOccupiedTimes)

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

