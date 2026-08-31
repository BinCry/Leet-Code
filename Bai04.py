class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # HashMap lưu ký tự và vị trí (index) gần nhất mà nó xuất hiện
        char_map = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # Nếu ký tự đã xuất hiện và nằm trong cửa sổ hiện tại (index >= left)
            # Dịch chuyển con trỏ left sang bên phải vị trí xuất hiện trước đó
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            # Cập nhật vị trí index mới nhất của ký tự
            char_map[char] = right

            # Tính độ dài cửa sổ hiện tại và cập nhật max_len
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "abcabcbb"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s1)}")  # Expected: 3

    # Test case 2
    s2 = "bbbbb"
    print(f"\nInput: s = \"{s2}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s2)}")  # Expected: 1

    # Test case 3
    s3 = "pwwkew"
    print(f"\nInput: s = \"{s3}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s3)}")  # Expected: 3

    # Test case 4 (Corner case: abba)
    s4 = "abba"
    print(f"\nInput: s = \"{s4}\"")
    print(f"Output: {solution.lengthOfLongestSubstring(s4)}")  # Expected: 2
