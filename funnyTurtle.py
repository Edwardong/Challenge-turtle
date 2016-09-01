import turtle
import math
from threading import Thread
from time import sleep

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

##############################################

#define for points, draw a line through these points with no delay
#a,b,c,d are the names of the points
steps=dis*3
stepsize=1/3

def fourPointGooto(t,a,b,c,d):
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

def drawSquare1(t):
	t.hideturtle()

	a0=(-3*dis/math.sqrt(2),0)
	b0=(0,3*dis/math.sqrt(2))
	c0=(3*dis/math.sqrt(2),0)
	d0=(0,-3*dis/math.sqrt(2))
	change1=(stepsize/math.sqrt(2),stepsize/math.sqrt(2))
	a0=list(a0)
	b0=list(b0)
	c0=list(c0)
	d0=list(d0)
	change1=list(change1)

	a1=(-2*dis/math.sqrt(2),dis/math.sqrt(2))
	b1=(dis/math.sqrt(2),2*dis/math.sqrt(2))
	c1=(2*dis/math.sqrt(2),-dis/math.sqrt(2))
	d1=(-dis/math.sqrt(2),-2*dis/math.sqrt(2))
#	change11=(stepsize/math.sqrt(2),stepsize/math.sqrt(2))
	a1=list(a1)
	b1=list(b1)
	c1=list(c1)
	d1=list(d1)
#	change11=list(change11)

	for i in range(steps):
		t.clear()
		turtle.tracer(0,0)
		fourPointGooto(t,a0,b0,c0,d0)
		a0=[a0[0]+change1[0],a0[1]+change1[1]]
		b0=[b0[0]+change1[0],b0[1]-change1[1]]
		c0=[c0[0]-change1[0],c0[1]-change1[1]]
		d0=[d0[0]-change1[0],d0[1]+change1[1]]

		fourPointGooto(t,a1,b1,c1,d1)
		a1=[a1[0]+change1[0],a1[1]-change1[1]]
		b1=[b1[0]-change1[0],b1[1]-change1[1]]
		c1=[c1[0]-change1[0],c1[1]+change1[1]]
		d1=[d1[0]+change1[0],d1[1]+change1[1]]
		
		turtle.update()


	for j in range(steps):
		t.clear()
		turtle.tracer(0,0)
		fourPointGooto(t,a0,b0,c0,d0)
		a0=[a0[0]+change1[0],a[1]-change1[1]]
		b0=[b0[0]-change1[0],b[1]-change1[1]]
		c0=[c0[0]-change1[0],c[1]+change1[1]]
		d0=[d0[0]+change1[0],d[1]+change1[1]]

		fourPointGooto(t,a1,b1,c1,d1)
		a=[a[0]-change1[0],a[1]-change1[1]]
		b=[b[0]-change1[0],b[1]+change1[1]]
		c=[c[0]+change1[0],c[1]+change1[1]]
		d=[d[0]+change1[0],d[1]-change1[1]]

		turtle.update()

	for k in range(steps):
		t.clear()
		turtle.tracer(0,0)
		fourPointGooto(t,a0,b0,c0,d0)
		a=[a[0]-change1[0],a[1]-change1[1]]
		b=[b[0]-change1[0],b[1]+change1[1]]
		c=[c[0]+change1[0],c[1]+change1[1]]
		d=[d[0]+change1[0],d[1]-change1[1]]

		fourPointGooto(t,a1,b1,c1,d1)
		a=[a[0]-change1[0],a[1]+change1[1]]
		b=[b[0]+change1[0],b[1]+change1[1]]
		c=[c[0]+change1[0],c[1]-change1[1]]
		d=[d[0]-change1[0],d[1]-change1[1]]

		turtle.update()

	for l in range(steps):
		t.clear()
		turtle.tracer(0,0)
		fourPointGooto(t,a0,b0,c0,d0)
		a=[a[0]-change1[0],a[1]+change1[1]]
		b=[b[0]+change1[0],b[1]+change1[1]]
		c=[c[0]+change1[0],c[1]-change1[1]]
		d=[d[0]-change1[0],d[1]-change1[1]]

		fourPointGooto(t,a1,b1,c1,d1)
		a=[a[0]+change1[0],a[1]+change1[1]]
		b=[b[0]+change1[0],b[1]-change1[1]]
		c=[c[0]-change1[0],c[1]-change1[1]]
		d=[d[0]-change1[0],d[1]+change1[1]]

		turtle.update()
	

# def drawSquare2(t):
# 	a1=(-2*dis/math.sqrt(2),dis/math.sqrt(2))
# 	b1=(dis/math.sqrt(2),2*dis/math.sqrt(2))
# 	c1=(2*dis/math.sqrt(2),-dis/math.sqrt(2))
# 	d1=(-dis/math.sqrt(2),-2*dis/math.sqrt(2))
# 	change1=(stepsize/math.sqrt(2),stepsize/math.sqrt(2))
# 	a1=list(a1)
# 	b1=list(b1)
# 	c1=list(c1)
# 	d1=list(d1)
# 	change11=list(change11)

# 	for n in range(steps):
# 		turtle.tracer(0,0)
# 		t.hideturtle()
# 		t.up()
# 		t.goto(a)
# 		t.down()
# 		t.left(45)
# 		t.goto(b)
# 		t.right(90)
# 		t.goto(c)
# 		t.right(90)
# 		t.goto(d)
# 		t.right(90)
# 		t.goto(a)
# 		turtle.update()
# 		t.reset()
# 		a=[a[0]-change1[0],a[1]-change1[1]]
# 		b=[b[0]-change1[0],b[1]+change1[1]]
# 		c=[c[0]+change1[0],c[1]+change1[1]]
# 		d=[d[0]+change1[0],d[1]-change1[1]]
# 		a=tuple(a)
# 		b=tuple(b)
# 		c=tuple(c)
# 		d=tuple(d)
# 	for o in range(steps):
# 		turtle.tracer(0,0)
# 		t.hideturtle()
# 		t.up()
# 		t.goto(a)
# 		t.down()
# 		t.left(45)
# 		t.goto(b)
# 		t.right(90)
# 		t.goto(c)
# 		t.right(90)
# 		t.goto(d)
# 		t.right(90)
# 		t.goto(a)
# 		turtle.update()
# 		t.reset()
# 		a=[a[0]-change1[0],a[1]+change1[1]]
# 		b=[b[0]+change1[0],b[1]+change1[1]]
# 		c=[c[0]+change1[0],c[1]-change1[1]]
# 		d=[d[0]-change1[0],d[1]-change1[1]]
# 		a=tuple(a)
# 		b=tuple(b)
# 		c=tuple(c)
# 		d=tuple(d)
# 	for p in range(steps):
# 		turtle.tracer(0,0)
# 		t.hideturtle()
# 		t.up()
# 		t.goto(a)
# 		t.down()
# 		t.left(45)
# 		t.goto(b)
# 		t.right(90)
# 		t.goto(c)
# 		t.right(90)
# 		t.goto(d)
# 		t.right(90)
# 		t.goto(a)
# 		turtle.update()
# 		t.reset()
# 		a=[a[0]+change1[0],a[1]+change1[1]]
# 		b=[b[0]+change1[0],b[1]-change1[1]]
# 		c=[c[0]-change1[0],c[1]-change1[1]]
# 		d=[d[0]-change1[0],d[1]+change1[1]]
# 		a=tuple(a)
# 		b=tuple(b)
# 		c=tuple(c)
# 		d=tuple(d)

# 	sleep(0.5)

Amy=turtle.Turtle()
# Douglas=turtle.Turtle()
drawSquare1(Amy)
# drawSquare2(Douglas)
#while True:
# t1 = Thread(target = drawSquare1, args = (Amy,))
# t1.start()
# #t1.sleep(0.05)
# t2 = Thread(target = drawSquare2, args = (Douglas,))
# t2.start()
	#t2.sleep(0.05)
