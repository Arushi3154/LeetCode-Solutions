class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        
        def backtrack(start_index: int, remain: int, current_path: list[int]):
            if remain == 0:
                result.append(list(current_path))
                return
            
            for i in range(start_index, len(candidates)):
                
                if candidates[i] > remain:
                    break
                
                current_path.append(candidates[i])
                
                
                backtrack(i, remain - candidates[i], current_path)
                
                current_path.pop()
                
        backtrack(0, target, [])
        return result
