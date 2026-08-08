class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_array = []
        for char in s:
            if char.isalnum():
                char_array.append(char.lower())

        clean_s = "".join(char_array)
        l = 0;
        r = len(clean_s) - 1
        while(l < r):
            if(clean_s[l] != clean_s[r]):
                return False
            l +=1 
            r -=1
        return True
                
        