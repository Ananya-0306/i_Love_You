from turtle import color, back, left, forward, right, exitonclick
import turtle
color("black")
back(450)
color("red")

left(90)
forward(100)
back(100)
right(90)
color("white")
forward(100)
left(90)
color("red")
forward(100)
back(100)
right(90)
color("red")
forward(50)
color("white")
forward(50)
color("red")
forward(50)
back(50)
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
left(90)
color("white")
forward(100)
color("red")
left(120)
forward(110)
back(110)
right(60)
forward(110)
back(110)
right(60)
color("white")
forward(100)
color("red")
forward(50)
back(50)
left(90)
forward(100)
right(90)
forward(50)
back(50)
right(90)
forward(50)
left(90)
forward(50)
back(50)
right(90)
forward(50)
left(90)
forward(50)
color("white")
forward(150)
color("red")
left(90)
forward(50)
left(45)
forward(75)
back(75)
right(90)
forward(75)
back(75)
left(45)
back(50)
right(90)
color("white")
forward(100)
color("red")
forward(50)
back(50)
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
left(90)
color("white")
forward(100)
color("red")
back(50)
left(90)
forward(100)
back(100)
right(90)
forward(50)
left(90)
forward(107)
color("white")
pen = turtle.Turtle() 

def curve(): 

    for i in range(200): 

        pen.right(1) 

        pen.forward(1) 

def heart():

    pen.fillcolor('red')

    pen.begin_fill()

    pen.left(150)

    pen.forward(113)

    curve()

    pen.left(120)

    curve()

    pen.forward(112)

    pen.end_fill()

heart()

def txt(x="" ):

    pen.up()

    pen.setpos(-70, 60)

    pen.down()

    pen.color('lightgreen')

    pen.write(x, font=("Verdana", 10, ""))

    

# put name in txt(" name ")

txt()

pen.ht()
exitonclick()
