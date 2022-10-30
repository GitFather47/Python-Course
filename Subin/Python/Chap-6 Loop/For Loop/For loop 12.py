import turtle

turtle.shape("turtle")
turtle.speed(2)

for len in range(250, 300, 10):
	for i in range(4):
		turtle.forward(len)
		turtle.left(90)
		
turtle.exitonclick()