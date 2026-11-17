class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        dic={}
        Uniquelen=0
        while (right < len(s)):
            if(s[right] not in dic):
                dic[s[right]]=1
                Uniquelen=max(Uniquelen,len(dic))
                right +=1
            else :
                while s[right] in dic:
                    del dic[s[left]]
                    left +=1
        return Uniquelen
   
                

        
        