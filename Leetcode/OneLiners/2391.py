class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        return (lambda m,p,g,c:(sum(travel[:m[-1][0]])+c['M'] if m else 0)+(sum(travel[:p[-1][0]])+c['P'] if p else 0)+(sum(travel[:g[-1][0]]) + c['G'] if g else 0))(list(filter(lambda x:'M' in x[1],list(enumerate(garbage)))),list(filter(lambda x:'P' in x[1],list(enumerate(garbage)))),list(filter(lambda x:'G' in x[1], list(enumerate(garbage)))),Counter(''.join(garbage)))