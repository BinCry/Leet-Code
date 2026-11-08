from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        LeetCode 16: 3Sum Closest (Medium)

        Tìm tổng của ba phần tử trong `nums` có giá trị gần `target` nhất.
        Đề bài bảo đảm đáp án là duy nhất.

        Sắp xếp mảng, sau đó cố định phần tử đầu tiên. Hai con trỏ duyệt
        phần còn lại: nếu tổng nhỏ hơn target thì tăng con trỏ trái, ngược lại
        giảm con trỏ phải. Mỗi tổng gần target hơn sẽ cập nhật kết quả.

        Độ phức tạp:
        - Thời gian: O(n²)
        - Không gian phụ: O(1), không tính thao tác sắp xếp tại chỗ
        """
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) - 1

            while left < right:
                current_sum = nums[index] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target

        return closest_sum


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([1, 1, 1, 0], -100, 2),
        ([-3, -2, -5, 3, -4], -1, -2),
        ([0, 1, 2], 0, 3),
    ]

    for index, (nums, target, expected) in enumerate(test_cases, start=1):
        result = solution.threeSumClosest(nums.copy(), target)
        assert result == expected, f"Test {index} failed: expected {expected}, got {result}"
        print(f"Test {index:02d}: PASSED")

    print("All tests passed successfully!")
