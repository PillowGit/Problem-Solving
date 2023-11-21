class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum((lambda p:[0 if l==r or l==-1 else len(set(s[l+1:r])) for l, r in p])([[s.find(c), max([-1 if x != c else i for i, x in enumerate(s)])] for c in 'abcdefghijklmnopqrstuvwxyz']))