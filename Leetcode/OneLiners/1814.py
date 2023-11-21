class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        return sum(count*(count-1)//2 for count in Counter(n - int(str(n)[::-1]) for n in nums).values()) % (10**9 + 7)