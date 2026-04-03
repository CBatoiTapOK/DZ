class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_length = 0
        seen_letters = set()

        for right in range(len(s)):
            while s[right] in seen_letters:
                seen_letters.remove(s[left])
                left += 1

            seen_letters.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length

sol = Solution()

s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s=s))
