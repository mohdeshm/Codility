class Solution:
    def solution(self,A,B):
        len = A.__len__()
        C = []

        for num in range(0, len):
            C.append(A[num] + B[num] / 1000000.0)
        count = 0
        for i in range(0, len-1):
            for j in range(i+1,len):
                if (C[i]*C[j])>=(C[i]+C[j]):
                    count=count+1
        if count>1000000000:
            return 1000000000
        return count

A=[0,1,2,2,3,5]
B=[500000,500000,0,0,0,20000]
solution = Solution()
multiplicativePairs=solution.solution(A,B)
print(multiplicativePairs)