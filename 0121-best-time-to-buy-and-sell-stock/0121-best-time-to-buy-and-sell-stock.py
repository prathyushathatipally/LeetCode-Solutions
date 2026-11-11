class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini=prices[0]
        maxi=0
        for i in range(len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            if prices[i]-mini>maxi:
                maxi=prices[i]-mini
        return maxi
        
