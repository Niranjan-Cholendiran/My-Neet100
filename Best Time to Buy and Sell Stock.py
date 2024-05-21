class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Use the 2 pointer approach, with left pointer in position 0 and right at 1.
        # Initate the max_profit as 0. Start calculating the difference between right and left value, if it negativem, then move your left value to the right position. 
        # If not update the max_profit and increase right by 1.
        # This way the max_profit will capture the max profit possible. It will work even for the test case [7,2,5,1,3,3] where the max is 5-2= 3 but not 3-1=2

        left_pointer= 0
        right_pointer= 1
        max_profit=0
        
        while right_pointer<len(prices):
            if (prices[right_pointer] <= prices[left_pointer]): 
                left_pointer= right_pointer
            else:
                max_profit = max(max_profit, prices[right_pointer] - prices[left_pointer])
            right_pointer+=1
            
        return max_profit