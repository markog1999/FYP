
import Grid as g
import SimplePath

myArray = g.Array3D(10, 10,10)

#abc

x = SimplePath.simplePath((2,4,1), (8,9,1), myArray,[])
y = SimplePath.simplePath((2,4,1), (8,9,1), myArray,[])
z = SimplePath.simplePath((2,4,1), (8,9,1), myArray,[])
a = SimplePath.simplePath((2,4,1), (8,9,1), myArray,[])



def report(*args):
    if len(args) >=2:
        report = ""
        for arg in args:
            report += str(arg)
            report += '\n'
        print(report)
    else:
        print(args)

report(x,y,z,a)
