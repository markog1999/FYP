import Config


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

    # Return the next available time (in Unix time) for a proposed journey to this node from a neighbour
    def NextAvailableTime(self, flight_start: float, duration: float):  # Start should be in Unix time, duration
        # should be expected flight duration in seconds TODO: Implement a better search method

        duration += Config.values["occupation_time_safety_margin"]

        if len(self._occupiedTimes) == 0:
            return flight_start

        i = 0
        # loop should end iterate over all but the last element of the list (where i == len(self.occupiedTimes) )
        while i < len(self._occupiedTimes):

            prev_interval_end = (self._occupiedTimes[i])[1]
            # Checks that a time interval ends before the new interval starts, if not iterates to the next
            if prev_interval_end > flight_start:

                i += 1
                continue

            # If the time interval ends before the new interval starts
            elif prev_interval_end <= flight_start:
                next_interval_start = (self._occupiedTimes[i + 1])[0]

                # If the duration before the start of the next interval is longer than the expected flight duration
                if (next_interval_start - (flight_start + duration)) >= 0:
                    # Return the end of previous interval as next available time
                    return flight_start
                else:
                    # The flight cannot begin during this interval, try start of next interval
                    flight_start = self._occupiedTimes[i + 1][1]
                    i += 1
                    continue

        # If the function iterates over all items of the list and finds no available interval, return end of last
        # occupied interval
        return (self._occupiedTimes[i])[1]

    # Add a tuple to the node representing a period of time that the node will be occupied
    def OccupyTime(self, start: float, end: float):  # Start and end should be times in seconds since Unix time
        # TODO: Implement a better search method to speed up insertion
        end += Config.values["occupation_time_safety_margin"]
        i = 0
        while i < len(self._occupiedTimes):
            if (self._occupiedTimes[i])[1] > start:
                i += 1
                continue
            elif (self._occupiedTimes[i])[1] < start:
                if (self._occupiedTimes[i + 1])[0] <= end:
                    raise Exception("Overlap between timestamps")
                else:
                    self._occupiedTimes.insert(i + 1, (start, end))
                    break
        if len(self._occupiedTimes) == 0:
            self._occupiedTimes.insert(0, (start, end))

        elif i == len(self._occupiedTimes):
            self._occupiedTimes.insert(i, (start, end))

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
                    node = GridNode(self, i, j, k)
                    self.Array[i][j].append(node)
                    if (i - 1) > 0:
                        node.AddAdjacent((i - 1, j, k))
                    if (i + 1) < xLimit:
                        node.AddAdjacent((i + 1, j, k))
                    if (j - 1) > 0:
                        node.AddAdjacent((i, j - 1, k))
                    if (j + 1) < zLimit:
                        node.AddAdjacent((i, j + 1, k))
                    if (k - 1) > 0:
                        node.AddAdjacent((i, j, k - 1))
                    if (k + 1) < zLimit:
                        node.AddAdjacent((i, j, k + 1))

                    k += 1
                j += 1
            i += 1

    def getNode(self, coords):
        x = coords[0]
        y = coords[1]
        z = coords[2]
        node = self.Array[x][y][z]
        return node

    def __str__(self):
        result = ""
        for i in self.Array:
            for j in i:
                for k in j:
                    result += str(k)
                    result += " "
            result += " \n"
        return result
