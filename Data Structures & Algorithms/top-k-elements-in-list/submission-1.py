class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}

        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1

        # Index represents frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in frequency.items():
            buckets[count].append(number)

        result = []

        for count in range(len(buckets) - 1, 0, -1):
            for number in buckets[count]:
                result.append(number)

                if len(result) == k:
                    return result