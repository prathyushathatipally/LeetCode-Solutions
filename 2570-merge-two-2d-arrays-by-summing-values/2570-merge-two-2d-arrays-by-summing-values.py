class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        l=nums1+nums2
        result=[]
        for i in range(len(l)):
            for j in range(len(result)):
                if result[j][0]==l[i][0]:
                    result[j][1]+=l[i][1]
                    break
            else:
                result.append([l[i][0],l[i][1]])
        result.sort()
        return result    