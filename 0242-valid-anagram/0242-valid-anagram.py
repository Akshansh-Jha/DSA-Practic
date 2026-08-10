class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        seen = {}
        for x in s:
            seen[x] = seen.get(x, 0) + 1
        for x in t:
            if x not in seen:
                return False
            seen[x] -=1
            if seen[x] < 0 :
                return False
        return True

        