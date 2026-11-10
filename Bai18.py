from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        LeetCode 18: 4Sum (Medium)

        Return all unique quadruplets whose sum equals ``target``. Sort the
        input, fix the first two values, then use two pointers to find the
        remaining pair. Skipping equal values prevents duplicate quadruplets.

        Complexity:
        - Time: O(n^3)
        - Extra space: O(1), excluding the returned result
        """
        nums.sort()
        quadruplets: List[List[int]] = []
        length = len(nums)

        for first in range(length - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, length - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                left, right = second + 1, length - 1

                while left < right:
                    total = nums[first] + nums[second] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        quadruplets.append(
                            [nums[first], nums[second], nums[left], nums[right]]
                        )
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return quadruplets


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([], 0, []),
        ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
        ([-3, -1, 0, 2, 4, 5], 2, [[-3, -1, 2, 4]]),
    ]

    for index, (nums, target, expected) in enumerate(test_cases, start=1):
        result = solution.fourSum(nums.copy(), target)
        assert result == expected, f"Test {index} failed: expected {expected}, got {result}"
        print(f"Test {index:02d}: PASSED")

    print("All tests passed successfully!")
