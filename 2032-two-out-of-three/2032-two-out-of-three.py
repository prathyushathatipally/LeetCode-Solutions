class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums1:
            if i not in l:
                l.append(i)
        l1=[]
        for i in nums2:
            if i not in l1:
                l1.append(i)
        l2=[]
        for i in nums3:
            if i not in l2:
                l2.append(i)
        k=[]
        for i in l+l1+l2:
            if i not in k:
                c=0
                if i in l:
                    c+=1
                if i in l1:
                    c+=1
                if i in l2:
                    c+=1
                if c>=2:
                    k.append(i)
        return k


                
      


        