class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)
        longest = 0

        for number in numbers:
            # A sequence starts when there is no previous number
            if number - 1 not in numbers:
                current = number
                length = 1

                while current + 1 in numbers:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest