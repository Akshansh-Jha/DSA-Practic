class Solution:
    def twoSum(self, num: List[int] , target: int):
        val_ind ={}
        for i , val in enumerate(num):
            if target - val in val_ind:
                return [i, val_ind[target - val]]
            val_ind[val]= i
