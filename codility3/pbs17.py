
import math
class Solution:

    def nCr(self,n,r):
        f=math.factorial
        if(n>=r):
            return f(n) / f(r) / f(n - r)
        else:
            return 0

    def solution(self,A):
        len=A.__len__()
        A=sorted(A)
        print(A)
        count=0
        copy=A[0]-1
        for i in range(0,len):
            if(copy != A[i]):
              n=A.count(A[i])
              copy=A[i]
              count=count+self.nCr(n,2)
            else:
                continue

        return count
obj=Solution()
print(obj.solution([3,5,6,3,3,5]))

