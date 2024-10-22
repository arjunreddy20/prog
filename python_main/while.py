def except_five(n):
    i=1
    while i <= n:  
        if i % 5 == 0:
            i=i+1
            continue   
        else:
            print(i)
        i=i+1
n=int(input(""))
print(except_five(n))

#even number
def find_even(n):
    i=1
    while i<=n:
        if i % 2 == 0:
            print(i)
        i=i+1
n=int(input("n="))
print(find_even(n))

# series print 1 4 9 16 25 36 49 with input 49
def find_series(n):
    i=1
    j=0
    while i <= n:
        j=i*i
        if j > n:
            break
        print(j)
        i=i+1
n=int(input("n="))
print(find_series(n))
