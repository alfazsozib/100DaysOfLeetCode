class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_dict = {}
        
        
        for i, j in enumerate(nums):
            if (target - j) in my_dict:
                return [my_dict[target - j],i]
            
            my_dict[j] = i
        return None    
