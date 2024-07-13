class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = []
        for i in (str(x)):
            lst.append(i)   
            
        if lst[0::] == lst[::-1]:
            return True
        else:
            return False
            
