class Solution:
    def trap(self, height: list[int]) -> int:
        """
        LeetCode 42: Trapping Rain Water (Hard)

        Thuật toán 2 Con trỏ (Two Pointers):
        - Lượng nước đọng tại một vị trí i được xác định bởi:
            water[i] = max(0, min(max_left, max_right) - height[i])
        - Thay vì dùng mảng tiền tố O(N) bộ nhớ để tìm max_left và max_right,
          ta có thể dùng 2 con trỏ `left` và `right` xuất phát từ hai đầu:
            + Duy trì `left_max` và `right_max`.
            + Nếu `left_max < right_max`: Đỉnh chặn bên trái nhỏ hơn đỉnh chặn bên phải,
              nghĩa là lượng nước tại `left` chắc chắn bị giới hạn bởi `left_max`
              (dù bên phải có cao hơn bao nhiêu đi nữa).
              => Ta tính được nước tại `left` = left_max - height[left], sau đó tăng `left`.
            + Ngược lại: Lượng nước tại `right` bị giới hạn bởi `right_max`.
              => Ta tính được nước tại `right` = right_max - height[right], sau đó giảm `right`.

        Độ phức tạp:
        - Thời gian: O(N) - duyệt qua mảng đúng 1 lần.
        - Không gian: O(1) - chỉ dùng các biến con trỏ.
        """
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Ví dụ cơ bản trong LeetCode
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Test 1: height = {height1}")
    print(f"Output: {solution.trap(height1)}")  # Expected: 6

    # Test case 2: Cột cao ở 2 đầu tạo thành bể lớn
    height2 = [4, 2, 0, 3, 2, 5]
    print(f"\nTest 2: height = {height2}")
    print(f"Output: {solution.trap(height2)}")  # Expected: 9

    # Test case 3: Dãy tăng dần hoặc giảm dần (không giữ được nước)
    height3 = [1, 2, 3, 4, 5]
    print(f"\nTest 3: height = {height3}")
    print(f"Output: {solution.trap(height3)}")  # Expected: 0

    # Test case 4: Dạng hình chữ V (giữ nước ở giữa)
    height4 = [5, 1, 5]
    print(f"\nTest 4: height = {height4}")
    print(f"Output: {solution.trap(height4)}")  # Expected: 4

    # Test case 5: Mảng rỗng hoặc ít hơn 3 phần tử (Corner cases)
    height5 = [2, 1]
    print(f"\nTest 5: height = {height5}")
    print(f"Output: {solution.trap(height5)}")  # Expected: 0
