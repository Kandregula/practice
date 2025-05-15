#Two pointer approach --> We can use two pointers to read the positive
# and negative parts of the array - one pointer
# "left" in the positive direction, and another "right" in the negative direction.
#two pointer approach used to solve --> Two Sum in Sorted Arrays
# , Closest Two Sum, Three Sum, Four Sum, Trapping Rain Water
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0]*n
        left = 0
        right = n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            res[i] = square * square
        return res

tc = Solution()
print(tc.sortedSquares([-4,-1,0,1,4]))
print(tc.sortedSquares([-4,-3,-2,-1,0]))