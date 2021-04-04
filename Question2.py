# Find the next term in the series
def find_next(n):
    if n%2==0:
        return (n*n) - 1
    else:
        return (n*n) + 1
n = int(input("Enter the number: "))
series_value = find_next(n)
print("The {} series number is {}".format(n,series_value))