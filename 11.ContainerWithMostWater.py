class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxo=0
        l,r,li,ri=height[0],height[len(height)-1],0,len(height)-1
        
        while li<ri:
            area= (min(l,r)*(ri-li))
            if area>maxo:
                maxo=area
            if l<r:
                li=li+1
                l=height[li]
            else:
                ri=ri-1
                r=height[ri]
               
        return maxo
                    
                