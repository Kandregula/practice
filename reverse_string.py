# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
# You must do this by modifying the input array in -place with O(1) extra memory.
#
# Example 1:
# Input: s = ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]
# Example 2:
# Input: s = ["H", "a", "n", "n", "a", "h"]
# Output: ["h", "a", "n", "n", "a", "H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        print(s)

#Time Complexity: The while left < right: loop runs approximately n/2 times, where n is the length of the list s.
#Each iteration performs a constant-time swap: s[left], s[right] = s[right], s[left]
#So overall, the function runs in linear time relative to the size of the input list
#Space Complexity: O(1) (in-place; uses no extra space beyond a few variables)