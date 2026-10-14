class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        l=[]
        mini=cost[0]
        for i in range(len(cost)):
            if cost[i]<mini:
                mini=cost[i]
            l.append(mini)
        return l
        