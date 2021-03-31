import Grid as g
import Pathing
from random import randint
from matplotlib import pyplot

def GeneratePaths(n, x_limit, y_limit, z_limit):
    myTestPaths = []
    for new_path in range(0,n):
        x1 = 1
        y1 = 1
        z1 = 1

        x2 = 9
        y2 = 9
        z2 = 9

        myTestPaths.append(((x1,y1,z1), (x2,y2,z2)))

    return myTestPaths

x_limit = 10
y_limit = 10
z_limit = 10
start_times_range = 0
n = 100

print("Generating node array")
myArray = g.Array3D(x_limit+1,y_limit+1,z_limit+1)
myArray2 = g.Array3D(x_limit+1,y_limit+1,z_limit+1)

print("Generating random paths")
testPaths = GeneratePaths(n, x_limit, y_limit, z_limit)
print("Generating start times")
start_times = [randint(0, start_times_range) for i in range(0,n)]
print("Checking Paths")

paths_checked = 0 #((0/n)*100)//1
times1 = []
times2 = []
rolling_average = []


for path in testPaths:
    route = Pathing.DirectPath(path[0], path[1], start_times[paths_checked], myArray)
    route.commit(myArray)
    times1.append(route.endTime())

    route = Pathing.OptimisedPath(path[0], path[1], start_times[paths_checked], myArray2)
    route.commit(myArray2)
    times2.append(route.endTime())

    try:
        average_over_last_10 = sum([times1[x] for x in range (-51, -1)]) / 50
        rolling_average.append(average_over_last_10)
    except:
        rolling_average.append(0)
    paths_checked += 1
    print("\rProgress %i percent" % ((paths_checked/n *100)//1), end="")
print("\n")

#pyplot.plot([n for n in range(0,n)], times1)
#pyplot.plot([n for n in range(0,n)], times2)

pyplot.xlabel("Drones routed though the airspace")
pyplot.ylabel("Duration of flight")
pyplot.bar(list(range(0, len(times1))), times1)
pyplot.bar(list(range(0, len(times2))), times2)
pyplot.show()