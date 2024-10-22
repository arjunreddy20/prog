


def find_max(a,b,c):
    """write the code inside this block to find the maximum between three numbers
    only print the maximum number  """
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    else:
        return c
    
    """Dont change anything below. If changed click on reset."""
a = int(input())
b = int(input())
c = int(input())
result = find_max(a,b,c)
print(result)