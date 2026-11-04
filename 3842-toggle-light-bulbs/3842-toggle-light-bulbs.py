class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(len(bulbs)):
            if bulbs.count(bulbs[i])%2!=0:
                l.append(bulbs[i])
        k=[]
        for i in range(len(l)):
            if l[i] not in k:
                k.append(l[i])
        return sorted(k)



        