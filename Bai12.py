class Solution:
    def intToRoman(self, num: int) -> str:
        """
        LeetCode 12: Integer to Roman (Medium)

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

        Các quy tắc đặc biệt (dạng trừ - Subtractive Form):
        - `I` đứng trước `V` (5) và `X` (10) để tạo thành 4 và 9.
        - `X` đứng trước `L` (50) và `C` (100) để tạo thành 40 và 90.
        - `C` đứng trước `D` (500) và `M` (1000) để tạo thành 400 và 900.

        Cho một số nguyên `num` nằm trong khoảng [1, 3999], hãy chuyển đổi nó thành số La Mã tương ứng.

        Phương pháp tiếp cận: Tham lam (Greedy Approach)
        ---------------------------------------------------------------------------------
        1. Xây dựng danh sách các cặp (giá trị, ký hiệu La Mã) theo thứ tự giảm dần từ lớn nhất đến nhỏ nhất:
           (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
           (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
           (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
           (1, "I")

        2. Duyệt qua từng cặp (value, symbol):
           - Kiểm tra xem `num` có thể chứa bao nhiêu lần `value` bằng phép chia nguyên: `count = num // value`.
           - Nếu `count > 0`:
             + Nối `symbol * count` vào chuỗi kết quả.
             + Cập nhật lại số dư: `num %= value`.
           - Nếu `num == 0`: ta có thể kết thúc sớm.

        3. Trả về chuỗi kết quả hoàn chỉnh.

        Độ phức tạp:
        - Thời gian: O(1) — Do giá trị đầu vào bị giới hạn từ 1 đến 3999, số lần lặp tối đa là cố định (13 bước).
        - Không gian: O(1) — Bảng ánh xạ có kích thước cố định và chuỗi kết quả có độ dài tối đa 15 ký tự (ví dụ: 3888 -> "MMMDCCCLXXXVIII").
        """
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        roman_parts = []
        for value, symbol in value_symbols:
            if num == 0:
                break
            count, num = divmod(num, value)
            if count > 0:
                roman_parts.append(symbol * count)

        return "".join(roman_parts)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Test 1: Ví dụ mẫu 1 từ LeetCode
        (3749, "MMMDCCXLIX"),
        # Test 2: Ví dụ mẫu 2 từ LeetCode
        (58, "LVIII"),
        # Test 3: Ví dụ mẫu 3 từ LeetCode
        (1994, "MCMXCIV"),
        # Test 4: Số nhỏ nhất
        (1, "I"),
        # Test 5: Số lớn nhất theo ràng buộc đề bài (3999)
        (3999, "MMMCMXCIX"),
        # Test 6: Các trường hợp dạng trừ (Subtractive forms)
        (4, "IV"),
        (9, "IX"),
        (40, "XL"),
        (90, "XC"),
        (400, "CD"),
        (900, "CM"),
        # Test 7: Kết hợp lặp lại nhiều ký tự đặc biệt
        (3888, "MMMDCCCLXXXVIII"),
        # Test 8: Số tròn trăm/nghìn
        (1000, "M"),
        (2000, "MM"),
        (3000, "MMM"),
        # Test 9: Số chứa nhiều số 4
        (444, "CDXLIV"),
        # Test 10: Số chứa nhiều số 9
        (999, "CMXCIX"),
    ]

    print("=" * 65)
    print("Running Tests for LeetCode 12 - Integer to Roman")
    print("=" * 65)

    for index, (num_input, expected) in enumerate(test_cases, start=1):
        result = solution.intToRoman(num_input)
        print(f"Test {index:02d}:")
        print(f"  Input:    num = {num_input}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        assert result == expected, f"Test {index} failed: expected {expected}, got {result}"
        print("  Status:   PASSED\n")

    print("=" * 65)
    print("All tests passed successfully!")
    print("=" * 65)
