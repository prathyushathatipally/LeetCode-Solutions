class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s)>k:
            t=[]
            u=[]
            l=[]
            for i in range(0,len(s),k):
                l.append(s[i:i+k])
            for i in range(len(l)):
                u.append(int(l[i]))
            for i in range(len(u)):
                temp=u[i]
                a=[]
                while temp>0:
                    digits=temp%10
                    a.append(digits)
                    temp=temp//10
                h=sum(a)
                t.append(h)
            s=""
            for i in range(len(t)):
                s=s+str(t[i])
        return s







        