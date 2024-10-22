# all numbers
for i in range(1,25,2):
    print(i)
    #(1=start,25=end,2=series)
#odd num
def odd_num(a):
    for i in range(1,a+1,2):
        print(i)
a=7
print(odd_num(a))
#print series 1 8 27 64 125 if 125 is input
def series_print(nm):
    for i in range(1,nm):
        j=i**3
        if j <= nm:
            print(j)
nm=int(input("enter= "))
print(series_print(nm))