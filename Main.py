
import Grid as g
import Pathing
from random import randint
from matplotlib import pyplot

def GenerateRandomPaths(n, x_limit,y_limit,z_limit):
    myTestPaths = []
    for new_path in range(0,n):
        x1 = randint(1, x_limit)
        y1 = randint(1, y_limit)
        z1 = randint(1, z_limit)

        x2 = randint(1, x_limit)
        y2 = randint(1, y_limit)
        z2 = randint(1, z_limit)

        myTestPaths.append(((x1,y1,z1), (x2,y2,z2)))

    return myTestPaths

x_limit = 10
y_limit = 10
z_limit = 10
start_times_range = 0
n = 10000

print("Generating node array")
myArray = g.Array3D(x_limit+1,y_limit+1,z_limit+1)
print("Generating random paths")
testPaths = GenerateRandomPaths(n, x_limit, y_limit, z_limit)
print("Generating start times")
start_times = [randint(0, start_times_range) for i in range(0,n)]
print("Checking Paths")

paths_checked = 0 #((0/n)*100)//1
durations = [] #The estimated duration of each path, listed sequentially
finishtimes = []
starttimes = []
rolling_average = []



for path in testPaths:
    route = Pathing.DirectPath(path[0], path[1], start_times[paths_checked], myArray)
    route.commit(myArray)
    durations.append(route.duration())
    finishtimes.append(route.endTime())
    starttimes.append(route.startTime())


    try:
        average_over_last_10 = sum([finishtimes[x] for x in range (-51,-1)]) / 50
        rolling_average.append(average_over_last_10)
    except:
        rolling_average.append(0)
    paths_checked += 1
    print("\rProgress %i percent" % ((paths_checked/n *100)//1), end="")
print("\n")


pyplot.plot([n for n in range(0,n)], finishtimes)
# pyplot.plot([n for n in range(0,n)], durations)
# pyplot.plot([n for n in range(0,n)], durations)
# pyplot.plot([n for n in range(0,n)], starttimes)
pyplot.plot([n for n in range(0,n)], rolling_average)

pyplot.xlabel("Drones routed though the airspace")
pyplot.ylabel("Duration of flight")
pyplot.show()

