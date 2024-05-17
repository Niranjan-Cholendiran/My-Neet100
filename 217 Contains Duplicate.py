class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert the list to set
        num_set=set(nums)
        
        # If the set size and list size is same, there are no duplicates and return False
        if (len(num_set)==len(nums)): return False
        else: return True