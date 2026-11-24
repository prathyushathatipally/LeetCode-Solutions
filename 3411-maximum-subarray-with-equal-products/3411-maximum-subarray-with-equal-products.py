class Solution:
    def maxLength(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                l.append(nums[i:j])
        k=[]
        ans=0
        for i in range(len(l)):
            temp=l[i]
            p=1
            for j in range(len(temp)):
                p=p*temp[j]
            k.append(p)
            m=math.lcm(*temp)
            n=math.gcd(*temp)
            if k[i]==m*n:
                ans=max(ans,len(temp))
        return ans
        
        