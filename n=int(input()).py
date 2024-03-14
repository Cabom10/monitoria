n=int(input())
a=1
b=0
fib=[]
for i in range(1,n+1):
    calc=a+b
    a=b
    b=calc
    #fib.append(calc)
    print(calc,end=" ")
