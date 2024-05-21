class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return False if the length of words are different
        if(len(s)!=len(t)):
            return False
        
        # 1. Pick the first letter in s, check if it is available in t. If not, return False.
        # 2. If present, count the frequency of it in both strings and return False if they are different.
        # 3. Remove the letter in both strings and repeat 1-3

        current_str_1= s
        current_str_2= t

        while len(current_str_1)!=0:
            letter= current_str_1[0]
            if(letter not in current_str_2): return False

            count_str_1= current_str_1.count(letter)
            count_str_2= current_str_2.count(letter)
            if(count_str_1!=count_str_2): return False

            current_str_1= current_str_1.replace(letter,"")
            current_str_2= current_str_2.replace(letter,"")
        
        return True

