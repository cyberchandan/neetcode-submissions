class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        if(len(s)!=len(t)):
            return False
        for char in s:
            if(char not in dic1):
                dic1[char]=1
            elif(char in dic1) :
                dic1[char]=dic1[char]+1
        for char in t:
            if(char not in dic2):
                dic2[char]=1
            elif(char in dic2) :
                dic2[char]=dic2[char]+1
        for key in dic1:
            if(key in dic2):
                if(dic1[key]!=dic2[key]):
                    return False
            if(key not in dic2):
                return False
        return True      




