
import Grid as g
import SimpleTimedPath

myArray = g.Array3D(10, 10,10)

#abc

x = SimpleTimedPath.SimpleTimedPath((1,2,3),(1,2,5),1000,myArray)




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
