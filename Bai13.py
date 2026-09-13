class Solution:
    def romanToInt(self, s: str) -> int:
        """
        LeetCode 13: Roman to Integer (Easy)

        Đề bài:
        Chữ số La Mã được biểu diễn bởi bảy ký hiệu khác nhau:
        Ký hiệu       Giá trị
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

        Quy tắc:
        - Thông thường chữ số La Mã được viết từ lớn nhất đến nhỏ nhất từ trái sang phải.
        - Tuy nhiên, trong 6 trường hợp dạng trừ (Subtractive Form):
          + `I` đứng trước `V` (5) và `X` (10) để tạo thành 4 và 9.
          + `X` đứng trước `L` (50) và `C` (100) để tạo thành 40 và 90.
          + `C` đứng trước `D` (500) và `M` (1000) để tạo thành 400 và 900.

        Cho một chuỗi số La Mã `s`, hãy chuyển đổi nó thành một số nguyên.

        Phương pháp tiếp cận: Duyệt tuyến tính (Linear Scan / Greedy)
        ---------------------------------------------------------------------------------
        1. Tạo bảng ánh xạ (dictionary) từ ký tự La Mã sang giá trị số nguyên tương ứng.
        2. Duyệt qua từng ký tự trong chuỗi từ trái sang phải:
           - So sánh giá trị của ký tự hiện tại `s[i]` với ký tự kế tiếp `s[i + 1]`:
             + Nếu giá trị hiện tại nhỏ hơn giá trị kế tiếp (trường hợp dạng trừ):
               ta trừ giá trị hiện tại vào tổng tích luỹ (`total -= roman_map[s[i]]`).
             + Ngược lại (trường hợp cộng thông thường):
               ta cộng giá trị hiện tại vào tổng tích luỹ (`total += roman_map[s[i]]`).
        3. Ký tự cuối cùng luôn được cộng vào tổng.
        4. Trả về kết quả `total`.

        Độ phức tạp:
        - Thời gian: O(n) — Duyệt qua chuỗi `s` một lần. Do độ dài `s <= 15` (cho các số La Mã <= 3999), thời gian thực thi là O(1).
        - Không gian: O(1) — Bảng ánh xạ có kích thước cố định gồm 7 phần tử.
        """
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        n = len(s)

        for i in range(n):
            current_val = roman_map[s[i]]
            # Nếu ký tự kế tiếp có giá trị lớn hơn ký tự hiện tại -> thực hiện phép trừ
            if i + 1 < n and current_val < roman_map[s[i + 1]]:
                total -= current_val
            else:
                total += current_val

        return total


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Test 1: Ví dụ mẫu 1 từ LeetCode
        ("III", 3),
        # Test 2: Ví dụ mẫu 2 từ LeetCode
        ("LVIII", 58),
        # Test 3: Ví dụ mẫu 3 từ LeetCode
        ("MCMXCIV", 1994),
        # Test 4: Số nhỏ nhất
        ("I", 1),
        # Test 5: Số lớn nhất theo phạm vi đề bài (3999)
        ("MMMCMXCIX", 3999),
        # Test 6: Các trường hợp dạng trừ (Subtractive forms)
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        # Test 7: Số kết hợp lặp lại nhiều ký tự
        ("MMMDCCCLXXXVIII", 3888),
        # Test 8: Số tròn trăm/nghìn
        ("M", 1000),
        ("MM", 2000),
        ("MMM", 3000),
        # Test 9: Số chứa nhiều số 4
        ("CDXLIV", 444),
        # Test 10: Số chứa nhiều số 9
        ("CMXCIX", 999),
    ]

    print("=" * 65)
    print("Running Tests for LeetCode 13 - Roman to Integer")
    print("=" * 65)

    for index, (s_input, expected) in enumerate(test_cases, start=1):
        result = solution.romanToInt(s_input)
        print(f"Test {index:02d}:")
        print(f"  Input:    s = '{s_input}'")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        assert result == expected, f"Test {index} failed: expected {expected}, got {result}"
        print("  Status:   PASSED\n")

    print("=" * 65)
    print("All tests passed successfully!")
    print("=" * 65)
