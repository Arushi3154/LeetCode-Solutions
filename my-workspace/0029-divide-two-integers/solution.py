class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            num_divisors = 1
            
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1
                
            abs_dividend -= temp_divisor
            quotient += num_divisors
            
        if is_negative:
            quotient = -quotient
            
        return max(INT_MIN, min(INT_MAX, quotient))
