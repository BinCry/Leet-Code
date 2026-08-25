from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Bỏ qua các phần tử trùng lặp cho i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Nếu phần tử hiện tại lớn hơn 0, không thể có tổng bằng 0
            if nums[i] > 0:
                break
                
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Bỏ qua các phần tử trùng lặp cho left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Bỏ qua các phần tử trùng lặp cho right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res

# Chạy thử
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.threeSum(nums1)}")
    # Expected: [[-1, -1, 2], [-1, 0, 1]]
    
    # Test case 2
    nums2 = [0, 1, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.threeSum(nums2)}")
    # Expected: []

    # Test case 3
    nums3 = [0, 0, 0]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.threeSum(nums3)}")
    # Expected: [[0, 0, 0]]
