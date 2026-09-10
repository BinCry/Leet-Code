from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        LeetCode 76: Minimum Window Substring (Hard)

        Đề bài:
        Cho hai chuỗi `s` và `t` với độ dài lần lượt là `m` và `n`. Hãy tìm chuỗi con
        có độ dài nhỏ nhất trong `s` sao cho nó chứa tất cả các ký tự của `t`
        (bao gồm cả số lần xuất hiện lặp lại của từng ký tự).
        Nếu không có chuỗi con nào thỏa mãn, trả về chuỗi rỗng `""`.

        Phương pháp tiếp cận: Cửa sổ trượt (Sliding Window) + Bảng tần số (Frequency Map)
        ---------------------------------------------------------------------------------
        1. Sử dụng một Counter (hoặc Hash Map) `target_counts` để lưu tần số xuất hiện
           của mỗi ký tự trong chuỗi `t`.
           - `required`: số lượng ký tự phân biệt trong `t` cần thỏa mãn.

        2. Duy trì một cửa sổ `[left, right]` trên chuỗi `s`:
           - Mở rộng con trỏ `right` sang phải, thêm ký tự `s[right]` vào cửa sổ hiện tại
             (`window_counts`).
           - Khi tần số của `s[right]` trong cửa sổ đạt đúng tần số yêu cầu trong `t`,
             tăng biến đếm `formed` lên 1.

        3. Khi cửa sổ hiện tại đã hợp lệ (`formed == required`):
           - Cập nhật vị trí và độ dài cửa sổ nhỏ nhất tìm được `(best_len, best_start)`.
           - Thử thu nhỏ cửa sổ bằng cách dịch con trỏ `left` sang phải:
             + Giảm tần số của `s[left]` trong `window_counts`.
             + Nếu tần số của `s[left]` nhỏ hơn tần số yêu cầu trong `target_counts`,
               giảm biến đếm `formed` đi 1 (cửa sổ không còn hợp lệ nữa).
             + Tăng `left` lên 1 và lặp lại việc co cửa sổ nếu vẫn còn hợp lệ.

        4. Lặp lại cho đến khi con trỏ `right` duyệt hết chuỗi `s`.
        5. Trả về chuỗi con bắt đầu từ `best_start` với độ dài `best_len` (nếu tìm thấy).

        Độ phức tạp:
        - Thời gian: O(|s| + |t|)
          + Đếm tần số chuỗi t: O(|t|).
          + Mỗi ký tự trong chuỗi s được con trỏ right duyệt qua đúng 1 lần và con trỏ
            left duyệt qua tối đa 1 lần: O(|s|).
        - Không gian: O(|s| + |t|) hoặc O(k) với k là số ký tự phân biệt (tối đa 52/128 ký tự ASCII).
        """
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        required = len(target_counts)

        window_counts: dict[str, int] = {}
        formed = 0

        left = 0
        min_len = float("inf")
        best_range = (0, 0)

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            while left <= right and formed == required:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    best_range = (left, right)

                remove_char = s[left]
                window_counts[remove_char] -= 1
                if (
                    remove_char in target_counts
                    and window_counts[remove_char] < target_counts[remove_char]
                ):
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[best_range[0] : best_range[1] + 1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Test 1: Ví dụ mẫu cơ bản
        ("ADOBECODEBANC", "ABC", "BANC"),
        # Test 2: Chuỗi 1 ký tự khớp hoàn toàn
        ("a", "a", "a"),
        # Test 3: Ký tự cần tìm lặp lại nhiều hơn số ký tự có trong s
        ("a", "aa", ""),
        # Test 4: Khớp toàn bộ chuỗi
        ("ab", "ba", "ab"),
        # Test 5: Chuỗi t có các ký tự trùng lặp
        ("aaflslflldkalskaaa", "aaa", "aaa"),
        # Test 6: Kết quả nằm ở đầu chuỗi
        ("abcde", "ab", "ab"),
        # Test 7: Kết quả nằm ở cuối chuỗi
        ("xyzabc", "abc", "abc"),
        # Test 8: Độ dài chuỗi s nhỏ hơn chuỗi t
        ("abc", "abcd", ""),
        # Test 9: Tất cả ký tự giống nhau
        ("aaaaaaa", "aa", "aa"),
        # Test 10: Ký tự phân biệt hoa thường
        ("aAbBcC", "ABC", "AbBcC"),
    ]

    print("=" * 60)
    print("Running Tests for LeetCode 76 - Minimum Window Substring")
    print("=" * 60)

    for index, (s, t, expected) in enumerate(test_cases, start=1):
        result = solution.minWindow(s, t)
        print(f"Test {index:02d}:")
        print(f"  Input:    s = {s!r}, t = {t!r}")
        print(f"  Output:   {result!r}")
        print(f"  Expected: {expected!r}")
        assert result == expected, f"Test {index} failed: expected {expected!r}, got {result!r}"
        print("  Status:   PASSED\n")

    print("=" * 60)
    print("All 10 tests passed successfully!")
    print("=" * 60)
