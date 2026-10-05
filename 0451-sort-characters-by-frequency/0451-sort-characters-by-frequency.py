class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        l=list(s)
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=sorted(d.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for key,values in s:
            ans+=key*values
        return ans


























       

        