class Solution:
    def maxScore(self, cardPoints: List[int], K: int) -> int:
        
        n = len(cardPoints)
        
        # 1. Get the total sum of all cards
        total = sum(cardPoints)
        
        # 2. Find the size of the middle window we want to leave behind
        W = n - K        
        
        # If we are taking all the cards, just return the total
        if W == 0:
            return total
        
        # 3. Calculate the sum of the very first window
        winSum = sum(cardPoints[0:W]) 
        minSum = winSum
        
        # 4. Slide the window across the list from left to right
        for r in range(W, n):
            # 5. Add the new card on the right and remove the old card on the left
            winSum += cardPoints[r] - cardPoints[r - W]
            
            # 6. Keep track of the smallest window sum we have seen
            minSum = min(minSum, winSum)
            
        # 7. Subtract the smallest middle sum from the total to get the maximum score
        return total - minSum

    # # --- Example Usage ---
    # # Suppose you have these cards and you can pick K = 3 cards from the ends
    # card_list = [1, 2, 3, 4, 5, 6, 1]
    # picks = 3

    # result = max_card_points(card_list, picks)
    # print("Maximum points:", result)  # Output will be 12 (by picking 1, 6, 5)
