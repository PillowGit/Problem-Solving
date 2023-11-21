class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        return [curr:=0,[curr:=min((curr:=curr)+1,x) for x in sorted(arr)], curr:=curr][-1]