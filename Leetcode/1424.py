class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        ans = []
        q = deque()
        q.append((0,0))
        while q:
            i, j = q.popleft()
            ans.append(nums[i][j])
            if j == 0 and i + 1 < m:
                q.append((i + 1, j))
            if j + 1 < len(nums[i]):
                q.append((i, j + 1))
        return ans