class Solution:
    def binary_search(self, arr, index_start, index_end, target):

        # if the relative arr size is less than 2 and the target is not present, then return -1  
        if (index_end - index_start <= 2):
            if (target in arr[index_start:index_end+1]): return arr.index(target)
            else: return -1

        # Compute index check as start index + floor (n/2)
        index_check= (index_end - index_start)/2
        index_check= index_check - (index_check % 1) # Calculate floor without function
        index_check= int(index_start + index_check)

        # Check if the index check contains the target, update the start and end index and repeat
        if arr[index_check] == target: 
            return index_check
        elif arr[index_check] > target:
            return self.binary_search(arr, index_start, index_check, target)
        else:
            return self.binary_search(arr, index_check, index_end, target)

    def search(self, nums, target):
        # Use binary search since the array is sorted
        return self.binary_search(nums, 0, len(nums)-1, target)
