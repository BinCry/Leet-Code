from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        LeetCode 14: Longest Common Prefix (Easy)

        Đề bài:
        Viết một hàm để tìm chuỗi tiền tố chung dài nhất (Longest Common Prefix)
        trong một mảng các chuỗi `strs`.
        Nếu không có tiền tố chung nào, trả về một chuỗi rỗng `""`.

        Ví dụ 1:
        - Input: strs = ["flower", "flow", "flight"]
        - Output: "fl"

        Ví dụ 2:
        - Input: strs = ["dog", "racecar", "car"]
        - Output: ""
        - Giải thích: Không có tiền tố chung giữa các chuỗi đầu vào.

        Ràng buộc:
        - 1 <= strs.length <= 200
        - 0 <= strs[i].length <= 200
        - strs[i] chỉ chứa các chữ cái tiếng Anh in thường nếu không rỗng.

        Phương pháp tiếp cận: Quét theo chiều dọc (Vertical Scanning)
        ---------------------------------------------------------------------------------
        1. Nếu danh sách chuỗi `strs` rỗng, trả về `""`.
        2. Lấy chuỗi đầu tiên `strs[0]` làm chuỗi tham chiếu.
        3. Duyệt qua từng chỉ số ký tự `i` của `strs[0]` từ `0` đến `len(strs[0]) - 1`:
           - Ký tự cần so sánh là `char = strs[0][i]`.
           - Duyệt qua các chuỗi còn lại `strs[1:]`:
             + Nếu chỉ số `i` đã chạm đến độ dài của chuỗi hiện tại (`i == len(s)`),
               hoặc ký tự tại vị trí `i` khác với `char` (`s[i] != char`):
               -> Tiền tố chung dài nhất kết thúc tại đây, trả về phần tiền tố `strs[0][:i]`.
        4. Nếu hoàn thành toàn bộ vòng lặp mà không gặp sự khác biệt nào,
           toàn bộ `strs[0]` chính là tiền tố chung, trả về `strs[0]`.

        Độ phức tạp:
        - Thời gian: O(S) — trong đó S là tổng số ký tự trong tất cả các chuỗi.
          Trong trường hợp tốt nhất (ký tự đầu tiên đã khác nhau), thuật toán chỉ mất O(n) với n là số chuỗi.
        - Không gian: O(1) — không dùng thêm bộ nhớ phụ trợ (ngoại trừ chuỗi kết quả trả về).
        """
        if not strs:
            return ""

        # Chuỗi đầu tiên làm mốc so sánh
        first_str = strs[0]

        for i, char in enumerate(first_str):
            for s in strs[1:]:
                # Nếu chuỗi s có độ dài nhỏ hơn hoặc bằng i, hoặc ký tự tại vị trí i khác char
                if i == len(s) or s[i] != char:
                    return first_str[:i]

        return first_str


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Test 1: Ví dụ mẫu 1 từ LeetCode
        (["flower", "flow", "flight"], "fl"),
        # Test 2: Ví dụ mẫu 2 từ LeetCode (không có tiền tố chung)
        (["dog", "racecar", "car"], ""),
        # Test 3: Mảng chỉ có 1 phần tử
        (["interspecies"], "interspecies"),
        # Test 4: Tất cả các chuỗi đều giống hệt nhau
        (["test", "test", "test"], "test"),
        # Test 5: Tiền tố chung là một phần của các từ
        (["leets", "leetcode", "leet", "leeds"], "lee"),
        # Test 6: Mảng chứa chuỗi rỗng ở đầu
        (["", "b"], ""),
        # Test 7: Mảng chứa toàn chuỗi rỗng
        (["", ""], ""),
        # Test 8: Các chuỗi đơn ký tự khớp nhau
        (["a", "a", "a"], "a"),
        # Test 9: Các chuỗi đơn ký tự không khớp
        (["a", "b"], ""),
        # Test 10: Chuỗi thứ hai ngắn hơn và là tiền tố của chuỗi thứ nhất
        (["ab", "a"], "a"),
        # Test 11: Khớp tiền tố 1 ký tự
        (["cir", "car"], "c"),
        # Test 12: Chuỗi đầu tiên dài nhưng không có tiền tố chung với các từ sau
        (["reflower", "flow", "flight"], ""),
        # Test 13: Mảng nhiều phần tử có tiền tố dài
        (["prefix_test_1", "prefix_test_2", "prefix_test_3", "prefix_special"], "prefix_"),
    ]

    print("=" * 65)
    print("Running Tests for LeetCode 14 - Longest Common Prefix")
    print("=" * 65)

    for index, (strs_input, expected) in enumerate(test_cases, start=1):
        result = solution.longestCommonPrefix(strs_input)
        print(f"Test {index:02d}:")
        print(f"  Input:    strs = {strs_input}")
        print(f"  Output:   '{result}'")
        print(f"  Expected: '{expected}'")
        assert result == expected, f"Test {index} failed: expected '{expected}', got '{result}'"
        print("  Status:   PASSED\n")

    print("=" * 65)
    print("All tests passed successfully!")
    print("=" * 65)
