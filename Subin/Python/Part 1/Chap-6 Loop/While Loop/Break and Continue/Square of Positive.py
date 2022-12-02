while True:
	n=input("Enter a Plus Number: ")
	l=int(n)
	if l< 0:
		print("Given number is not a Plus number.Try again.")
		continue
	if l==0:
		break
	print("Square of ", l,"is", l*l) 
		
		