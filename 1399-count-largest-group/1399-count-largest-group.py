class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        for i in range(1,n+1):
            l.append(i)
        m=[]
        for i in range(len(l)):
            temp=l[i]
            s=0
            while temp>0:
                digits=temp%10
                s+=digits
                temp=temp//10
            m.append(s)
        d={}
        for i in m:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        maxi=max(d.values())
        c=0
        for i in d.values():
            if i==maxi:
                c+=1
        return c



        
            

        