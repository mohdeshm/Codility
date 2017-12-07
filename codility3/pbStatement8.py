class solution:
    def soltion(self,A):
        len=A.__len__()
        d=sorted(map(abs,A))[0]
        for i in range(len-1):
            x=A[i]
            for j in range(i+1,len):
                x+=A[j]
                if(d>abs(x)):
                    d=abs(x)
        return d
obj=solution()
print(obj.soltion([2,-4,6,-3,9,0]))