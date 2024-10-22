#patterns of different type s== for loop y=Mx+c y=no.of *'s + 1
for i in range(1,6,1):
    patt=0
    for j in range(1,1+i,1):
        patt=patt+j
    print(patt)
        
print("===============================================================")
for i in range(1,6,1):
    repatt=""
    for j in range(1,7-i,1):
        repatt=repatt+"*"
    print(repatt)
print("===============================================================")
for i in range(1,11,1):
    stting=""
    for j in range(1,7-i,1):
        stting=stting+"*"

    for j in range(1,i-4,1):
        stting=stting+"*"

    for j in range(1,2*i-1,1):
        stting=stting+" "
        
    for j in range(7,-2*i+11,1):
        stting=stting+"1"

  
    
    for j in range(1,7-i,1):
        stting=stting+"*"

    print(stting)

print("===============================================================")

#patterns of different type s== for loop y=Mx+c y=no.of *'s

def pattern(n):
    i=1
    while i<=n:
        output=""
        j=1
        while j<=6-i:
            output=output+"*"
            j+=1
        print(output)
        i+=1
n=5
print(pattern(n))

print("===============================================================")

def patte(n):
    x=1
    while x<=n:
        get=""
        j=1
        while j <= x:
            get=get+"*"
            j+=1
        print(get)
        x+=1
n=5
print(patte(n))

print("===============================================================")

def spl_pattern(s):

    for i in range (1,s,1):
        put=""

        for j in range (1,i+1,1):
            put=put+"*"

        for j in range (1,6-i,1):
            put=put+" "

        for j in range (1,i+1,1):
            put=put+"*"

        print(put)

s=5
print(spl_pattern(s))
print("===============================================================")
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))