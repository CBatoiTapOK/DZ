class Solution(object):
    def maxArea(self, height):
        max_area = 0
        l ,r = 0, len(height) - 1

        while l < r:
            if height[l] >= height[r]:
                area = (r - l) * height[r]
            elif height[r] >= height[l]:
                area = (r - l) * height[l]

            if area > max_area:
                max_area = area

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return max_area


sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])

print(sol.maxArea([1,8,6,2,5,4,8,3,7]), sol.maxArea([4,3,2,1,4]))
