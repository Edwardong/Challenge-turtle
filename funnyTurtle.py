import turtle
import math

#draw four obliqueSquares firstly
turtle.setup(500,500)
dis=80
def obliqueSquare(t,x,y):
	t.up()
	t.goto(x,y)
	t.down()
	t.left(45)
	t.forward(dis*math.sqrt(2))
	t.right(90)
	t.forward(dis*math.sqrt(2))
	t.right(90)
	t.forward(dis*math.sqrt(2))
	t.right(90)
	t.forward(dis*math.sqrt(2))
	t.right(135)

Edward=turtle.Turtle()
Edward.color('purple')
Edward.hideturtle()
Edward.speed(0)
turtle.tracer(0,0)
obliqueSquare(Edward,-3*dis,0)
obliqueSquare(Edward,-dis,2*dis)
obliqueSquare(Edward,dis,0)
obliqueSquare(Edward,-dis,-2*dis)
turtle.update()
#——————————————————————————————————————

#define for points, draw a line through these points with no delay
#a,b,c,d are the names of the points
def drawSquare(z,a,b,c,d,e,f,g,h):
	z.up()
	z.goto(-3*dis,0)
	z.down()
	z.goto(0,3*dis)
	z.goto(3*dis,0)
	z.goto(0,-3*dis)
	z.goto(-3*dis,0)