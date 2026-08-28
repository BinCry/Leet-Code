from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Chỉ bắt đầu đếm khi `num` là phần tử đầu tiên của một chuỗi liên tiếp
            # (tức là không tồn tại num - 1 trong set)
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Đếm tiếp các số liên tiếp: num + 1, num + 2, ...
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Input: {nums1}")
    print(f"Output: {solution.longestConsecutive(nums1)}") # Expected: 4

    # Test case 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.longestConsecutive(nums2)}") # Expected: 9
