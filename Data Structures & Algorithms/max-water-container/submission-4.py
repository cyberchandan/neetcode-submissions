class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0
        right =len(heights)-1
        maxWater=0
        while(left<right):
            h=min(heights[left],heights[right])
            l=right-left
            if(maxWater<h*l):
                maxWater=h*l
            if(heights[left]>heights[right]):
                right -=1
            else:
                left +=1
        return maxWater    
            
        