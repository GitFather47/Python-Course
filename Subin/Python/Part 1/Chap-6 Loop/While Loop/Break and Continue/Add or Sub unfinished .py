terminate=False
while not terminate:
    inp1=input("Enter a number: ")
	num1=int(inp1)
	inp2=input("Enter another number: ")
	num2=int(inp2)
    while True:
    operation=input("Enter add/sub or quit to exit: ")
	  if operation=="quit":
		terminate=True
		break
	  if operation not in ["add", "sub"]:
	 print("Unknown operation!")
	continue
	  if operation=="add":
		print("Result is", num1+num2)
		break
	  if operation=="sub":
		print("Result is", num1-num2)
		break
	