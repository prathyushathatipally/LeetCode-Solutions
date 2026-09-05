class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        s=0
        while n>0:
            digit=n%10
            s=s*10+digit
            n=n//10
        if s==x:
            return True
        return False
        