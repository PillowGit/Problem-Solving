class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i, j in zip(l, r):
            arr = sorted(nums[i:j+1], key=lambda x:-x)
            ans.append(True)
            for i in range(1, len(arr)-1, 1):
                if arr[i]*2 != arr[i-1] + arr[i+1]:
                    ans[-1] = False
                    break
        return ans