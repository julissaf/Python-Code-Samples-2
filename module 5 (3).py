# Julissa Franco
# February 14, 2019
# Program will create a polygon


import turtle
wn= turtle.Screen ()
alex = turtle.Turtle ()



sideNumber= int(input("How many sides for your polygon?"))

aColor= str(input ( "What color for your polygon?"))

sideLength= int(input ("What side length for your polygon?"))

fColor= str(input("What color is filled in the polygon?"))

angle= 360/sideNumber

alex.begin_fill()


for x in range (sideNumber):
    
    alex.forward(sideLength)
    alex. left(angle)

alex.color(aColor)
alex.fillcolor(fColor)
alex.end_fill()

wn.exitonclick()

