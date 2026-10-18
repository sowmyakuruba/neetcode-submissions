class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If the first number is positive, the sum cannot be zero
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicate second numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate third numbers
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result