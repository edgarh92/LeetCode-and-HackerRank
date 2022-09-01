class Solution:
    def trap(self, height: List[int]) -> int:
        
        trapped_water = 0
        l , r = 0, len(height) -1
        highest_left_bound, highest_right_bound = height[l], height[r]
        
    
        while l < r:
            
            if highest_left_bound < highest_right_bound:
                l+=1 #TODO explain this more clearly.
                highest_left_bound = max(highest_left_bound, height[l])
                trapped_water += highest_left_bound - height[l]
               
            else:
                r-=1
                highest_right_bound = max(highest_right_bound, height[r])
                trapped_water+= highest_right_bound - height[r]
                
            
        return trapped_water