from turtle import *

#we want to paint a house

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)       #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("purple")
left(30)
forward(60)
left(90)
#step 4: draw a square

width(4)
color("brown")
forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(20)
left(90)
forward(40)
left(90)
forward(22)
left(90)
forward(22)
left(90)
forward(44)

color("white")
forward(90)
right(90)
forward(20)
left(90)
forward(20)



#step 4: draw a square

width(4)
color("brown")
forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(20)
left(90)
forward(40)
left(90)
forward(22)
left(90)
forward(22)
left(90)
forward(44)




#end of square

exitonclick()