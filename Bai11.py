from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        LeetCode 11: Container With Most Water (Medium)

        Đề bài:
        Cho một mảng số nguyên `height` có độ dài `n`. Có `n` đường thẳng đứng được vẽ
        sao cho hai điểm đầu mút của đường thẳng thứ `i` là `(i, 0)` và `(i, height[i])`.
        Hãy tìm hai đường thẳng cùng với trục hoành tạo thành một bể chứa sao cho
        bể chứa đó đựng được nhiều nước nhất.
        Trả về lượng nước tối đa mà bể có thể chứa.
        Lưu ý: Bạn không được nghiêng bể chứa.

        Công thức tính diện tích nước:
            Diện tích = (right - left) * min(height[left], height[right])

        Phương pháp tiếp cận: Kỹ thuật Hai Con Trỏ (Two Pointers)
        ---------------------------------------------------------------------------------
        1. Khởi tạo hai con trỏ:
           - `left = 0` (cột đầu tiên bên trái)
           - `right = len(height) - 1` (cột cuối cùng bên phải)
           - `max_water = 0`

        2. Tại mỗi bước:
           - Tính lượng nước giữa hai cột `left` và `right`:
             `current_water = (right - left) * min(height[left], height[right])`
           - Cập nhật `max_water = max(max_water, current_water)`.

        3. Dịch chuyển con trỏ:
           - Chiều cao của bể nước bị giới hạn bởi cột ngắn hơn (`min(height[left], height[right])`).
           - Chiều rộng `(right - left)` luôn giảm đi sau mỗi bước.
           - Vì vậy, nếu giữ lại cột ngắn hơn và di chuyển cột dài hơn, diện tích chắc chắn
             sẽ giảm (hoặc tối đa bằng cột ngắn hơn nhưng với chiều rộng nhỏ hơn).
           - Do đó, cơ hội duy nhất để tìm được diện tích lớn hơn là dịch con trỏ của CỘT NGẮN HƠN
             vào phía trong để hy vọng tìm được một cột cao hơn.
           - Nếu `height[left] < height[right]`: tăng `left` (bỏ qua các cột <= height[left]).
           - Ngược lại: giảm `right` (bỏ qua các cột <= height[right]).

        4. Lặp lại cho đến khi `left >= right`.

        Độ phức tạp:
        - Thời gian: O(N) — mỗi phần tử được xét tối đa một lần khi hai con trỏ di chuyển vào giữa.
        - Không gian: O(1) — chỉ sử dụng các biến con trỏ và biến lưu trữ kết quả.
        """
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            h_left = height[left]
            h_right = height[right]
            width = right - left

            if h_left < h_right:
                current_water = h_left * width
                # Tối ưu hóa: Bỏ qua nhanh các cột liên tiếp có chiều cao <= h_left
                while left < right and height[left] <= h_left:
                    left += 1
            else:
                current_water = h_right * width
                # Tối ưu hóa: Bỏ qua nhanh các cột liên tiếp có chiều cao <= h_right
                while left < right and height[right] <= h_right:
                    right -= 1

            if current_water > max_water:
                max_water = current_water

        return max_water


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Test 1: Ví dụ mẫu 1 từ LeetCode
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        # Test 2: Ví dụ mẫu 2 từ LeetCode (mảng 2 phần tử đơn giản)
        ([1, 1], 1),
        # Test 3: Mảng tăng dần đều
        ([1, 2, 3, 4, 5, 6, 7, 8], 16),
        # Test 4: Mảng giảm dần đều
        ([8, 7, 6, 5, 4, 3, 2, 1], 16),
        # Test 5: Tất cả các cột có cùng chiều cao
        ([5, 5, 5, 5, 5], 20),
        # Test 6: Hai cột cao nhất nằm ở hai đầu
        ([100, 1, 1, 1, 1, 100], 500),
        # Test 7: Cột cao nhất nằm ở giữa (dạng hình chóp)
        ([1, 3, 5, 7, 9, 7, 5, 3, 1], 20),
        # Test 8: Hai phần tử có chiều cao chênh lệch lớn
        ([1, 1000], 1),
        # Test 9: Mảng dạng thung lũng (hai đầu cao, ở giữa thấp)
        ([10, 2, 1, 2, 10], 40),
        # Test 10: Mảng xen kẽ cột cao và thấp
        ([2, 3, 4, 5, 18, 17, 6], 17),
    ]

    print("=" * 65)
    print("Running Tests for LeetCode 11 - Container With Most Water")
    print("=" * 65)

    for index, (height_input, expected) in enumerate(test_cases, start=1):
        result = solution.maxArea(height_input)
        print(f"Test {index:02d}:")
        print(f"  Input:    height = {height_input}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        assert result == expected, f"Test {index} failed: expected {expected}, got {result}"
        print("  Status:   PASSED\n")

    print("=" * 65)
    print("All 10 tests passed successfully!")
    print("=" * 65)
