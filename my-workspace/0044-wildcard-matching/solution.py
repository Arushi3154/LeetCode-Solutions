class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx, p_idx = 0, 0
        
        star_idx = -1
        s_match = -1
        
        while s_idx < s_len:
            if p_idx < p_len and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
                
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_match = s_idx
                p_idx += 1
                
            elif star_idx != -1:
                p_idx = star_idx + 1
                s_match += 1
                s_idx = s_match
                
            else:
                return False
                
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == p_len
