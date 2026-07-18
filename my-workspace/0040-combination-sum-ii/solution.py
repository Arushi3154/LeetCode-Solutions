class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        
        def backtrack(start_index: int, remain: int, current_path: list[int]):
            if remain == 0:
                result.append(list(current_path))
                return
            
            for i in range(start_index, len(candidates)):
                if candidates[i] > remain:
                    break
                
            
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                current_path.append(candidates[i])
                
            
                backtrack(i + 1, remain - candidates[i], current_path)
                
                current_path.pop()
                
        backtrack(0, target, [])
        return result
