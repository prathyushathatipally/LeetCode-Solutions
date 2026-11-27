class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        blue="B"
        green="G"
        red="R"
        l=[]
        c=0
        for i in range(0,len(rings),2):
            l.append(rings[i]+rings[i+1])
        for i in range(10):
            b=0
            g=0
            r=0
            for j in range(len(l)):
                temp=l[j]
                if temp[1]==str(i):
                    if temp[0]==blue:
                        b=1
                    elif temp[0]==green:
                        g=1
                    elif temp[0]==red:
                        r=1
            if b==1 and g==1 and r==1:
                c+=1
        return c
