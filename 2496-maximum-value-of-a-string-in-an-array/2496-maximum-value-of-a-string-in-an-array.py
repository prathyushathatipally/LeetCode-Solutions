class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        l=[]
        l1=[]
        l2=[]
        for i in strs:
            if i.isdigit():
                l.append(int(i))
            else:
                l1.append(len(i))
        l2=l1+l
        return max(l2)
        


        