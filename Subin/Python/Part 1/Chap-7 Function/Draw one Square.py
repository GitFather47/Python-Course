import turtle 
def draw_sqrn(length):
	for i in range(4):
		turtle.forward(length)
		turtle.left(90)
draw_sqrn(300)
turtle.exitonclick()