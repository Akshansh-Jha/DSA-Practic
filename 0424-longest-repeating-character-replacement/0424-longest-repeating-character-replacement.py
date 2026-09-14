class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26

        maxLen = 0
        maxFreq = 0
        left = 0
        right = 0

        while right < n:
            ch = s[right]

            freq[ord(ch) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(ch) - ord('A')])

            if (right - left + 1) - maxFreq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen