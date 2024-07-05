class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        if target<0:
            return []
        elif target==0:
            return [[]]
        else:
            thisCombo=[[candidates[-1]]+combo for combo in self.combinationSum(candidates,target-candidates[-1])]
            othersOnly=self.combinationSum(candidates[:-1],target)
            return thisCombo+othersOnly
            