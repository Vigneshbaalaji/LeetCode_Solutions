class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_str = str(x)
        number_str_rev = number_str[::-1]
        if number_str == number_str_rev:return True
        else: return False
