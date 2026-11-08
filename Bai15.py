from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        LeetCode 15: 3Sum (Medium)

        Cho mảng số nguyên `nums`, trả về mọi bộ ba phần tử khác vị trí có
        tổng bằng 0. Mỗi bộ ba trong kết quả phải là duy nhất.

        Cách làm: sắp xếp mảng, cố định từng phần tử đầu tiên rồi dùng hai
        con trỏ ở phần còn lại để tìm hai phần tử có tổng đối nghịch. Bỏ qua
        các giá trị trùng lặp để tránh thêm cùng một bộ ba nhiều lần.

        Độ phức tạp:
        - Thời gian: O(n²)
        - Không gian phụ: O(1), không tính kết quả trả về
        """
        nums.sort()
        triplets: List[List[int]] = []

        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            if nums[index] > 0:
                break

            left, right = index + 1, len(nums) - 1

            while left < right:
                total = nums[index] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 4, 4], [[-4, 0, 4], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
    ]

    for index, (nums, expected) in enumerate(test_cases, start=1):
        result = solution.threeSum(nums.copy())
        assert result == expected, f"Test {index} failed: expected {expected}, got {result}"
        print(f"Test {index:02d}: PASSED")

    print("All tests passed successfully!")
