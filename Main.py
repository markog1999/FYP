
import Grid as g
import SimpleTimedPath

myLovelyArray = g.Array3D(10,10,10)
myOtherArray = g.Array3D(2,2,2)

#abc

x = SimpleTimedPath.SimpleTimedPath((1,1,1),(1,5,5),1000,myArray)
y = SimpleTimedPath.SimpleTimedPath((1,1,1),(1,5,5),1000,myArray)
z = SimpleTimedPath.SimpleTimedPath((1,5,5),(1,1,1),1000,myArray)





def report(*args):
    if len(args) >=2:
        report = ""
        for arg in args:
            report += str(arg)
            report += '\n'
        print(report)
    else:
        print(args)

report(x)
