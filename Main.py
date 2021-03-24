
import Grid as g
import SimpleTimedPath
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

x_limit = 100
y_limit = 100
z_limit = 100
start_times_range = 0
n = 5000000

print("Generating node array")
myArray = g.Array3D(x_limit+1,y_limit+1,z_limit+1)
print("Generating random paths")
testPaths = GenerateRandomPaths(n, x_limit, y_limit, z_limit)
print("Generating start times")
start_times = [randint(0, start_times_range) for i in range(0,n)]
print("Checking Paths")

paths_checked = 0 #((0/n)*100)//1
results = [] #The estimated duration of each path, listed sequentially
rolling_average = []



for path in testPaths:
    duration = SimpleTimedPath.DirectPath(path[0],path[1],start_times[paths_checked],myArray)
    results.append(duration)
    try:
        average_over_last_10 = sum([results[x] for x in range (-51,-1)]) / 50
        rolling_average.append(average_over_last_10)
    except:
        rolling_average.append(0)
    paths_checked += 1
    print("\rProgress %i percent" % ((paths_checked/n *100)//1), end="")
print("\n")



pyplot.plot([n for n in range(0,n)], results)
pyplot.plot([n for n in range(0,n)], rolling_average)
pyplot.show()






"""
node1 = myArray.getNode((1,1,1))
node2 = myArray.getNode((1,1,1))

print(SimpleTimedPath.find_flight_window(node1,node2, 200,100))
"""

"""
a = SimpleTimedPath.DirectPath((1, 1, 1), (1, 5, 5), 1000, myArray)
b = SimpleTimedPath.DirectPath((1, 1, 1), (1, 5, 5), 1000, myArray)
c = SimpleTimedPath.DirectPath((1, 1, 1), (1, 5, 5), 1000, myArray)
x = SimpleTimedPath.DirectPath((1, 1, 1), (1, 5, 5), 1000, myArray)
y = SimpleTimedPath.DirectPath((1, 5, 5), (1, 1, 1), 1000, myArray)
z =SimpleTimedPath.DirectPath((2, 8, 0), (3, 8, 7), 1000, myArray)


def report(*args):
    if len(args) >=2:
        report = ""
        for arg in args:
            report += str(arg)
            report += '\n'
        print(report)
    else:
        print(args)

report(a,b,c,x,y,z)

"""
