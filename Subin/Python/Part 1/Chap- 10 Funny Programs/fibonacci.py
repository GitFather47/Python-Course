n=int(input())
def fibonacci(n):
    fib1=1
    fib2=1
    if n<=2:
        fibn=1
    else:
        i = 3
        while i<=n:
            i+=1
            #1st method
            #fibt=fib1+fib2
            #fib1=fib2
            #fib2=fibt
            #or method 2
            fib2, fib1= fib1+fib2, fib2
            #fibn=fibt(for method1)
        fibn=fib2
    print(fibn)
fibonacci(n)