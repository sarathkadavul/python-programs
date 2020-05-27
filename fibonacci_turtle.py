import turtle
#q2
x=0
y=1
turtle.pensize(1)
turtle.speed(1)
turtle.pendown()
turtle.penup()
range_val=14
for i in range(1,range_val):
	turtle.setpos((x,0))
	turtle.pendown()
	turtle.setpos((x,y))
	turtle.setpos((-1,y))
	turtle.penup()
	turtle.setpos((0,0))
	c=x+y
	x=y
	y=c

#q1
x=0
y=1
turtle.pensize(1)
turtle.speed(1)
turtle.pendown()
turtle.penup()

for i in range(1,range_val):	
	ax=x-(2*x)
	turtle.setpos((ax,0))
	turtle.pendown()
	turtle.setpos((ax,y))
	turtle.setpos((0,y))
	turtle.penup()
	turtle.setpos((0,0))
	c=x+y
	x=y
	y=c

#q3
x=0
y=-1

turtle.pensize(1)
turtle.speed(1)
turtle.pendown()
turtle.penup()

for i in range(1,range_val):
	turtle.setpos((x,0))
	turtle.pendown()
	turtle.setpos((x,y))
	turtle.setpos((0,y))
	turtle.penup()
	turtle.setpos((0,0))
	c=x+y
	x=y
	y=c

#q4
x=0
y=1
turtle.pensize(1)
turtle.speed(1)
turtle.pendown()
turtle.penup()

for i in range(1,range_val):
	ay=y-(2*y)
	turtle.setpos((x,0))
	turtle.pendown()
	turtle.setpos((x,ay))
	turtle.setpos((-1,ay))
	turtle.penup()
	turtle.setpos((0,0))
	c=x+y
	x=y
	y=c

turtle.exitonclick()