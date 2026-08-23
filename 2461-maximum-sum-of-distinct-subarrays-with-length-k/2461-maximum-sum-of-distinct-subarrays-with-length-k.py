class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        sum_window = 0
        best = 0

        for r in range (len(nums)):
            sum_window += nums[r]
            freq [nums[r]] += 1

            if r >= k:
                sum_window -= nums[r-k]
                freq [nums[r-k]] -= 1
                
                if freq [nums[r-k]] == 0:
                    del freq [nums[r-k]]
            
            if r >= k - 1:
                if len(freq) < k:
                    continue
                else:
                    best = max(best , sum_window)
        return best



        