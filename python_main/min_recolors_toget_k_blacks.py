class Solution():
    def minrecolors(self,s,k):
        self.k=k
        self.s=s
        n=len(s)
        min_recolors=0
        current_colors=sum(1 for i in range (self.k) if self.s[i]=="W")
        min_recolors=current_colors
        for i in range (k,n):
            if self.s[i-self.k]=="W":
                current_colors-=1
            if self.s[i]=="W":
                current_colors+=1
            min_recolors=min(min_recolors,current_colors)
        return min_recolors

s=Solution()
n=(input("enter="))
print(s.minrecolors(n,int(input())))
