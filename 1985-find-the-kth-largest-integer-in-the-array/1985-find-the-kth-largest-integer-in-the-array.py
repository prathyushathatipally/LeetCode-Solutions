class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        s=" ".join(map(str,nums))
        m=list(map(int,s.split()))
        l=sorted(m,reverse=True)
        n=l[k-1]
        return str(n)