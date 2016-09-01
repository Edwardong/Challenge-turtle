import turtle
import math


#draw four obliqueSquares firstly
turtle.setup(800,600)
# screen.colormode(255)
# turtle.bgcolor((30,0,40))

# screen.setup(width=.75, height=0.5, startx=None, starty=None)
dis=90
def obliqueSquare(t,x,y):
	t.up()
	t.goto(x,y)
	t.down()
	t.left(45)
	t.forward(dis)
	t.right(90)
	t.forward(dis)
	t.right(90)
	t.forward(dis)
	t.right(90)
	t.forward(dis)
	t.right(135)

Edward=turtle.Turtle()
Edward.color('purple')
Edward.hideturtle()
Edward.speed(0)
turtle.tracer(0,0)
obliqueSquare(Edward,-3*dis/math.sqrt(2),0)
obliqueSquare(Edward,-dis/math.sqrt(2),2*dis/math.sqrt(2))
obliqueSquare(Edward,dis/math.sqrt(2),0)
obliqueSquare(Edward,-dis/math.sqrt(2),-2*dis/math.sqrt(2))
turtle.update()
#——————————————————————————————————————

#define for points, draw a line through these points with no delay
#a,b,c,d are the names of the points
steps=dis*3
stepsize=1/3


def drawSquare1(t):
	a=(-3*dis/math.sqrt(2),0)
	b=(0,3*dis/math.sqrt(2))
	c=(3*dis/math.sqrt(2),0)
	d=(0,-3*dis/math.sqrt(2))
	change1=(stepsize/math.sqrt(2),stepsize/math.sqrt(2))
	a=list(a)
	b=list(b)
	c=list(c)
	d=list(d)
	change1=list(change1)
	for i in range(steps):
		turtle.tracer(0,0)
		t.hideturtle()
		t.up()
		t.goto(a)
		t.down()
		t.left(45)
		t.goto(b)
		t.right(90)
		t.goto(c)
		t.right(90)
		t.goto(d)
		t.right(90)
		t.goto(a)
		turtle.update()
		t.reset()
		a=[a[0]+change1[0],a[1]+change1[1]]
		b=[b[0]+change1[0],b[1]-change1[1]]
		c=[c[0]-change1[0],c[1]-change1[1]]
		d=[d[0]-change1[0],d[1]+change1[1]]
		a=tuple(a)
		b=tuple(b)
		c=tuple(c)
		d=tuple(d)
	for j in range(steps):
		turtle.tracer(0,0)
		t.hideturtle()
		t.up()
		t.goto(a)
		t.down()
		t.left(45)
		t.goto(b)
		t.right(90)
		t.goto(c)
		t.right(90)
		t.goto(d)
		t.right(90)
		t.goto(a)
		turtle.update()
		t.reset()
		a=[a[0]+change1[0],a[1]-change1[1]]
		b=[b[0]-change1[0],b[1]-change1[1]]
		c=[c[0]-change1[0],c[1]+change1[1]]
		d=[d[0]+change1[0],d[1]+change1[1]]
		a=tuple(a)
		b=tuple(b)
		c=tuple(c)
		d=tuple(d)
	for k in range(steps):
		turtle.tracer(0,0)
		t.hideturtle()
		t.up()
		t.goto(a)
		t.down()
		t.left(45)
		t.goto(b)
		t.right(90)
		t.goto(c)
		t.right(90)
		t.goto(d)
		t.right(90)
		t.goto(a)
		turtle.update()
		t.reset()
		a=[a[0]-change1[0],a[1]-change1[1]]
		b=[b[0]-change1[0],b[1]+change1[1]]
		c=[c[0]+change1[0],c[1]+change1[1]]
		d=[d[0]+change1[0],d[1]-change1[1]]
		a=tuple(a)
		b=tuple(b)
		c=tuple(c)
		d=tuple(d)
	for l in range(steps):
		turtle.tracer(0,0)
		t.hideturtle()
		t.up()
		t.goto(a)
		t.down()
		t.left(45)
		t.goto(b)
		t.right(90)
		t.goto(c)
		t.right(90)
		t.goto(d)
		t.right(90)
		t.goto(a)
		turtle.update()
		t.reset()
		a=[a[0]-change1[0],a[1]+change1[1]]
		b=[b[0]+change1[0],b[1]+change1[1]]
		c=[c[0]+change1[0],c[1]-change1[1]]
		d=[d[0]-change1[0],d[1]-change1[1]]
		a=tuple(a)
		b=tuple(b)
		c=tuple(c)
		d=tuple(d)


def drawSquare2(t):
	a=(-2*dis/math.sqrt(2),dis/math.sqrt(2))
	b=(dis/math.sqrt(2),2*dis/math.sqrt(2))
	c=(2*dis/math.sqrt(2),-dis/math.sqrt(2))
	d=(-dis/math.sqrt(2),-2*dis/math.sqrt(2))
	change1=(stepsize/math.sqrt(2),stepsize/math.sqrt(2))
	a=list(a)
	b=list(b)
	c=list(c)
	d=list(d)
	change1=list(change1)
	for m in range(steps):
		turtle.tracer(0,0)
		t.hideturtle()
		t.up()
		t.goto(a)
		t.down()
		t.left(45)
		t.goto(b)
		t.right(90)
		t.goto(c)
		t.right(90)
		t.goto(d)
		t.right(90)
		t.goto(a)
		turtle.update()
		t.reset()
		a=[a[0]+change1[0],a[1]-change1[1]]
		b=[b[0]-change1[0],b[1]-change1[1]]
		c=[c[0]-change1[0],c[1]+change1[1]]
		d=[d[0]+change1[0],d[1]+change1[1]]
		a=tuple(a)
		b=tuple(b)
		c=tuple(c)
		d=tuple(d)
	for n in range(steps):
		turtle.tracer(0,0)
		t.hideturtle()
		t.up()
		t.goto(a)
		t.down()
		t.left(45)
		t.goto(b)
		t.right(90)
		t.goto(c)
		t.right(90)
		t.goto(d)
		t.right(90)
		t.goto(a)
		turtle.update()
		t.reset()
		a=[a[0]-change1[0],a[1]-change1[1]]
		b=[b[0]-change1[0],b[1]+change1[1]]
		c=[c[0]+change1[0],c[1]+change1[1]]
		d=[d[0]+change1[0],d[1]-change1[1]]
		a=tuple(a)
		b=tuple(b)
		c=tuple(c)
		d=tuple(d)
	for o in range(steps):
		turtle.tracer(0,0)
		t.hideturtle()
		t.up()
		t.goto(a)
		t.down()
		t.left(45)
		t.goto(b)
		t.right(90)
		t.goto(c)
		t.right(90)
		t.goto(d)
		t.right(90)
		t.goto(a)
		turtle.update()
		t.reset()
		a=[a[0]-change1[0],a[1]+change1[1]]
		b=[b[0]+change1[0],b[1]+change1[1]]
		c=[c[0]+change1[0],c[1]-change1[1]]
		d=[d[0]-change1[0],d[1]-change1[1]]
		a=tuple(a)
		b=tuple(b)
		c=tuple(c)
		d=tuple(d)
	for p in range(steps):
		turtle.tracer(0,0)
		t.hideturtle()
		t.up()
		t.goto(a)
		t.down()
		t.left(45)
		t.goto(b)
		t.right(90)
		t.goto(c)
		t.right(90)
		t.goto(d)
		t.right(90)
		t.goto(a)
		turtle.update()
		t.reset()
		a=[a[0]+change1[0],a[1]+change1[1]]
		b=[b[0]+change1[0],b[1]-change1[1]]
		c=[c[0]-change1[0],c[1]-change1[1]]
		d=[d[0]-change1[0],d[1]+change1[1]]
		a=tuple(a)
		b=tuple(b)
		c=tuple(c)
		d=tuple(d)
		

Amy=turtle.Turtle()

drawSquare1(Amy)
drawSquare2(Amy)
