class Solution:
    def countHomogenous(self, s: str) -> int:
        return int(sum([(len(p[0]))*((len(p[0])+1)/2) for p in findall(r'((.)\2*)', s)])%(1e9+7))