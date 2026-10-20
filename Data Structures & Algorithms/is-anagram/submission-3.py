class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = {}
        t_hash = {}
        for i in s:
            s_hash[i] = s_hash.get(i, 0) + 1
        for i in t:
            t_hash[i] = t_hash.get(i, 0) + 1
        if s_hash == t_hash:
            return True
        else:
            return False