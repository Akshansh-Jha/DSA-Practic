class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxm = 0
        while left < right:
            area = (right - left) * min(height[left],height[right])
            maxm = max(maxm,area)
            if height[left] <= height[right] :
                left += 1 
            else :
                right -= 1
        return maxm
        