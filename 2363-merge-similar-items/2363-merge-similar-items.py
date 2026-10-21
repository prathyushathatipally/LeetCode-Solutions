class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        l=items1+items2
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

        