class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        
        res = 0
        is_negative = x < 0
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
        
            if res > (MAX_INT // 10) or (res == (MAX_INT // 10) and digit > 7):
                return 0
            
       
            res = (res * 10) + digit
            
        return -res if is_negative else res
        
