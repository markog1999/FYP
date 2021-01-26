
import time as time

class GridNode:
    def __init__(self, gridPointer, x, y, z):
        self._grid = gridPointer
        self._coord = (x, y, z)
        self._availability = True
        self._adjacentNodes = []
        self._availableNodes = []

    def AddAdjacent(self, new: tuple):
        self._adjacentNodes.append(new)
    def GetAdjacents(self):
        return self._adjacentNodes

    def AddAvailable(self, new: tuple):
        self._availableNodes.append(new)
    def GetAvailableNodes(self):
        return self._availableNodes
    def UpdateAvailableNodes(self):
        self._availableNodes = []
        for coordinates in self.GetAdjacents():
            if self._grid.getNode(coordinates).GetAvailability() == True:
                self._availableNodes.append(coordinates)

    def GetAvailability(self):
        return self._availability

    def SetAvailability(self, b: bool):
        self._availability = b

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

