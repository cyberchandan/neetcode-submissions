
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        Topk=[]
    
        for num in nums:
            if num not in dic:
                dic[num]=1
            else :
                dic[num]=dic[num]+1
        sortedDic=dict(sorted(dic.items(),key=lambda item:item[1],reverse=True))
        count=0
        for key in sortedDic:
            count = count+1
            Topk.append(key)
            if count == k:
                break
        return Topk

        
            
       