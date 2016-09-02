import turtle
import math

#draw four obliqueSquares firstly
turtle.setup(800,600)
turtle.bgcolor('#1E0028')

dis=60
def obliqueSquare(t,x,y):
	t.width(0.5)
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

#define four points, draw a line through these points with no delay
#a,b,c,d are the names of the points
steps=dis*2
stepsize=1/2

def fourPointGooto(t,a,b,c,d):
	t.shape("circle")
	t.width(0.3)
	t.shapesize(0.2, 0.2)
	t.up()
	t.goto(a)
	t.down()
	t.stamp()
	t.goto(b)
	t.stamp()
	t.goto(c)
	t.stamp()
	t.goto(d)
	t.stamp()
	t.goto(a)

def drawSquare1(t):
	t.hideturtle()

	change1=(stepsize/math.sqrt(2),stepsize/math.sqrt(2))
	change1=list(change1)
	
	a0=(-3*dis/math.sqrt(2),0)
	b0=(0,3*dis/math.sqrt(2))
	c0=(3*dis/math.sqrt(2),0)
	d0=(0,-3*dis/math.sqrt(2))
	a0=list(a0)
	b0=list(b0)
	c0=list(c0)
	d0=list(d0)

	a1=(-2*dis/math.sqrt(2),dis/math.sqrt(2))
	b1=(dis/math.sqrt(2),2*dis/math.sqrt(2))
	c1=(2*dis/math.sqrt(2),-dis/math.sqrt(2))
	d1=(-dis/math.sqrt(2),-2*dis/math.sqrt(2))
	a1=list(a1)
	b1=list(b1)
	c1=list(c1)
	d1=list(d1)

	a2=(-dis/math.sqrt(2),0)
	b2=(0,dis/math.sqrt(2))
	c2=(dis/math.sqrt(2),0)
	d2=(0,-dis/math.sqrt(2))
	a2=list(a2)
	b2=list(b2)
	c2=list(c2)
	d2=list(d2)

	a3=(-2*dis/math.sqrt(2),-dis/math.sqrt(2))
	b3=(-dis/math.sqrt(2),2*dis/math.sqrt(2))
	c3=(2*dis/math.sqrt(2),dis/math.sqrt(2))
	d3=(dis/math.sqrt(2),-2*dis/math.sqrt(2))
	a3=list(a3)
	b3=list(b3)
	c3=list(c3)
	d3=list(d3)

	while 1:
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

			fourPointGooto(t,a2,b2,c2,d2)
			a2=[a2[0]-change1[0],a2[1]-change1[1]]
			b2=[b2[0]-change1[0],b2[1]+change1[1]]
			c2=[c2[0]+change1[0],c2[1]+change1[1]]
			d2=[d2[0]+change1[0],d2[1]-change1[1]]

			fourPointGooto(t,a3,b3,c3,d3)
			a3=[a3[0]-change1[0],a3[1]+change1[1]]
			b3=[b3[0]+change1[0],b3[1]+change1[1]]
			c3=[c3[0]+change1[0],c3[1]-change1[1]]
			d3=[d3[0]-change1[0],d3[1]-change1[1]]
			
			turtle.update()
			t.clearstamps()


		for j in range(steps):
			t.clear()
			turtle.tracer(0,0)
			fourPointGooto(t,a0,b0,c0,d0)
			a0=[a0[0]+change1[0],a0[1]-change1[1]]
			b0=[b0[0]-change1[0],b0[1]-change1[1]]
			c0=[c0[0]-change1[0],c0[1]+change1[1]]
			d0=[d0[0]+change1[0],d0[1]+change1[1]]

			fourPointGooto(t,a1,b1,c1,d1)
			a1=[a1[0]-change1[0],a1[1]-change1[1]]
			b1=[b1[0]-change1[0],b1[1]+change1[1]]
			c1=[c1[0]+change1[0],c1[1]+change1[1]]
			d1=[d1[0]+change1[0],d1[1]-change1[1]]

			fourPointGooto(t,a2,b2,c2,d2)
			a2=[a2[0]-change1[0],a2[1]+change1[1]]
			b2=[b2[0]+change1[0],b2[1]+change1[1]]
			c2=[c2[0]+change1[0],c2[1]-change1[1]]
			d2=[d2[0]-change1[0],d2[1]-change1[1]]

			fourPointGooto(t,a3,b3,c3,d3)
			a3=[a3[0]+change1[0],a3[1]+change1[1]]
			b3=[b3[0]+change1[0],b3[1]-change1[1]]
			c3=[c3[0]-change1[0],c3[1]-change1[1]]
			d3=[d3[0]-change1[0],d3[1]+change1[1]]

			turtle.update()
			t.clearstamps()

		for k in range(steps):
			t.clear()
			turtle.tracer(0,0)
			fourPointGooto(t,a0,b0,c0,d0)
			a0=[a0[0]-change1[0],a0[1]-change1[1]]
			b0=[b0[0]-change1[0],b0[1]+change1[1]]
			c0=[c0[0]+change1[0],c0[1]+change1[1]]
			d0=[d0[0]+change1[0],d0[1]-change1[1]]

			fourPointGooto(t,a1,b1,c1,d1)
			a1=[a1[0]-change1[0],a1[1]+change1[1]]
			b1=[b1[0]+change1[0],b1[1]+change1[1]]
			c1=[c1[0]+change1[0],c1[1]-change1[1]]
			d1=[d1[0]-change1[0],d1[1]-change1[1]]

			fourPointGooto(t,a2,b2,c2,d2)
			a2=[a2[0]+change1[0],a2[1]+change1[1]]
			b2=[b2[0]+change1[0],b2[1]-change1[1]]
			c2=[c2[0]-change1[0],c2[1]-change1[1]]
			d2=[d2[0]-change1[0],d2[1]+change1[1]]

			fourPointGooto(t,a3,b3,c3,d3)
			a3=[a3[0]+change1[0],a3[1]-change1[1]]
			b3=[b3[0]-change1[0],b3[1]-change1[1]]
			c3=[c3[0]-change1[0],c3[1]+change1[1]]
			d3=[d3[0]+change1[0],d3[1]+change1[1]]

			turtle.update()
			t.clearstamps()

		for l in range(steps):
			t.clear()
			turtle.tracer(0,0)
			fourPointGooto(t,a0,b0,c0,d0)
			a0=[a0[0]-change1[0],a0[1]+change1[1]]
			b0=[b0[0]+change1[0],b0[1]+change1[1]]
			c0=[c0[0]+change1[0],c0[1]-change1[1]]
			d0=[d0[0]-change1[0],d0[1]-change1[1]]

			fourPointGooto(t,a1,b1,c1,d1)
			a1=[a1[0]+change1[0],a1[1]+change1[1]]
			b1=[b1[0]+change1[0],b1[1]-change1[1]]
			c1=[c1[0]-change1[0],c1[1]-change1[1]]
			d1=[d1[0]-change1[0],d1[1]+change1[1]]

			fourPointGooto(t,a2,b2,c2,d2)
			a2=[a2[0]+change1[0],a2[1]-change1[1]]
			b2=[b2[0]-change1[0],b2[1]-change1[1]]
			c2=[c2[0]-change1[0],c2[1]+change1[1]]
			d2=[d2[0]+change1[0],d2[1]+change1[1]]

			fourPointGooto(t,a3,b3,c3,d3)
			a3=[a3[0]-change1[0],a3[1]-change1[1]]
			b3=[b3[0]-change1[0],b3[1]+change1[1]]
			c3=[c3[0]+change1[0],c3[1]+change1[1]]
			d3=[d3[0]+change1[0],d3[1]-change1[1]]

			turtle.update()
			t.clearstamps()

Amy=turtle.Turtle()
Amy.color('white')
drawSquare1(Amy)

