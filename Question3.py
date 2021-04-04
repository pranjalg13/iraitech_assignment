# evalute the following expression

def calculate_fun(x,y,a,b):
    # By solving the equation we get the shorter version as: (x/y)^(a+b)
    return (x/y)**(a+b)
# Considering all as int(as not specified in question)
x = int(input("Enter the x: "))
y = int(input("Enter the y: "))
a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
ans = calculate_fun(x,y,a,b)
print("The answer of the expression is: {}".format(ans))