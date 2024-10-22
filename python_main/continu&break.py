#continue in while
n=7
i=1
while i<n:
    if i % 5 == 0:
        i+=1
        continue
    print(i)
    i+=1
#continue in for
def except_5(x):

    for i in range(1,x,1):
        if i % 5 == 0:
            i+=1
            continue
        print(i)
        i=i+1
x=7
print(except_5(x))
#break with while
a=6
j=1
while j<a:
    if j>4:
        break
    else:
        print(j)
    j+=1       # incresing the value of iterating variable is necessary
#break with for
for i in range(1,10):
    if i > 5:
        break
    print(i)