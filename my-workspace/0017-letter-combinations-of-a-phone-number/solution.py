class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        if not digits:
            return []
   
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        combinations = []
        
        def backtrack(index: int, current_path: list[str]):
    
            if len(current_path) == len(digits):
                combinations.append("".join(current_path))
                return
      
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]
            
            for letter in possible_letters:
                current_path.append(letter)       
                backtrack(index + 1, current_path) 
                current_path.pop()               
                
       
        backtrack(0, [])
        return combinations
        
