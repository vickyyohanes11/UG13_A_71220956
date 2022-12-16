import turtle

s =  turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.setx(-80)
t.sety(20)

t.pensize(20)
t.right(60)
t.forward(100)
t.left(120)
t.forward(100)
t.right(60)
t.penup()


t.goto(90,-45)
t.pendown()
t.circle(35)
t.circle(35,70)
t.goto(90,-100)
t.penup()

t.goto(220,30)
t.pendown()
t.left(110)
t.forward(40)
t.left(90)
t.forward(60)
t.left(90)
t.forward(10)
t.right(150)
t.circle(40,-180)
t.left(150)
t.forward(50)
t.penup()

t.goto(320,30)
t.pendown()
t.left(65)
t.forward(80)
t.circle(30)
t.penup()

t.goto(400,30)
t.pendown()
t.left(60)
t.forward(100)
t.left(120)
t.forward(100)
t.left(180)
t.forward(170)



