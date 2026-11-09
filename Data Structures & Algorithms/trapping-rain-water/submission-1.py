class Solution:
    def trap(self, height: List[int]) -> int:
        Lmax=0
        Rmax=0
        l=0
        r=len(height)-1
        result=0
        while(l<r):
            if(height[l]< height[r]):
                Lmax=max(Lmax,height[l])
                result +=Lmax-height[l]
                l +=1
            else:
                Rmax=max(Rmax,height[r])
                result +=Rmax-height[r]
                r -=1
        return result
  
