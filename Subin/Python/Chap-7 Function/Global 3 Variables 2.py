# after declaring an argument's value, we need  to declare the next value of the next argument as well.To understand,check Global 3 variables 1
def myfnc(x, y=99, z=0):
	print("x =", x)
	print("y =", y)
	print("z =", z)
x = 8
y = 9
z = 10
myfnc(x, y, z)
myfnc(x, y)
myfnc(x)