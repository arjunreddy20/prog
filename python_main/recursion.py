


class Solution:
    def recursive(self,i,n,sum):
        if i >= n:
            return sum
        return self.recursive(i + 2, n, sum + i)
	
x=Solution()
print(x.recursive(0,10,0))



#printing multiples of 5 with recursion


def print_out(n,i,sum):
    if i >= n:
        return 
    else:
        print(sum)
        return print_out(n,i+1,sum+5)
n=5
print(print_out(5,0,0))

#ANOTHER APPROCH

def print_output(n,current=0):
    """Print all multiples of 5  """
    
    if n < current: 
        return 
    else:
        print(current)
        return print_output(n,current+5)

def main():
    n=int(input())
    print_output(n)
    
main()

