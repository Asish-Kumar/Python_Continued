# Author: Asish Kumar
# in this we are learning to import and use some modules
# import turtle
# or we could import only the methods that we need
from turtle import forward, right, done
# the error/ warning here is just a bug in the IDE,
#  forward and right functions are there in turtel.py line 1616
#####
# from turtle import *  # this will import every function in the turtle.py
# using import* is not recommended as it may import a function that we do not know about
# and later we may be declaring a variable of the same name

# turtle.forward(120)
# turtle.right(89)
# turtle.forward(60)
# turtle.done()  # this stops the graphics window until we manually close it
# and we now do not need to write turtle.function name, instead we can simply write function name
forward(120)
right(89)
forward(60)
done()
