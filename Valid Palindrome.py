class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all the non-alphanumeric characters and convert the string to lower case
        if(s==''): return True
        compare_str= ''
        for letter in s:
            if(letter.isalnum()): compare_str+=letter.lower()
        if(compare_str==''): return True

        # Use a 2 pointer approach to compare strings from both ends, return False if an unmatch found 
        pointer1= 0
        pointer2= len(compare_str)-1

        while(pointer1 < pointer2):
            if(compare_str[pointer1] != compare_str[pointer2]): return False
            pointer1+=1
            pointer2-=1

        return True
