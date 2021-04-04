#Iterative Version
def iterative():
    x = float(input("Enter the x: "))
    n = int(input("Enter the value of n: "))
    ans = 0
    for i in range(1,n+1):
        ans = ans + (1/(x**i))
    print("The sum of the series is: {0:.2f}".format(ans))

# Recursive Version
def recursive(x,n):
    if n==-1:
        return n
    else:
        return float(1/x**n) + recursive(x,n-1)
iterative()
x = int(input("Enter the x: "))
n = int(input("Enter the value of n: "))
ans = recursive(x,n)
print("The sum of the series is: {0:.2f}".format(ans))
