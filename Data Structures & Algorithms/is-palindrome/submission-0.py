class Solution:
    def isPalindrome(self, s: str) -> bool:
        strr=''
        left=0
       
        for char in s:
            if char.isalnum():
                strr +=char.lower()
        right =  len(strr)-1
        while(left<right):
            if(strr[left] != strr[right]):
                return False
            else: 
                left +=1
                right -=1
        return True
        