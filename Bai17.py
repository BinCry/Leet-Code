from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        LeetCode 17: Letter Combinations of a Phone Number (Medium)

        Given a string containing digits from 2 through 9, return every
        possible letter combination represented by a telephone keypad.

        Build each combination with backtracking: at each position, append
        every letter associated with that digit, then continue to the next
        position.

        Complexity:
        - Time: O(4^n * n), where n is the number of digits
        - Extra space: O(n), excluding the returned combinations
        """
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations: List[str] = []
        current: List[str] = []

        def backtrack(index: int) -> None:
            if index == len(digits):
                combinations.append("".join(current))
                return

            for letter in digit_to_letters[digits[index]]:
                current.append(letter)
                backtrack(index + 1)
                current.pop()

        backtrack(0)
        return combinations


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
        ("79", [
            "pw", "px", "py", "pz", "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz",
        ]),
    ]

    for index, (digits, expected) in enumerate(test_cases, start=1):
        result = solution.letterCombinations(digits)
        assert result == expected, f"Test {index} failed: expected {expected}, got {result}"
        print(f"Test {index:02d}: PASSED")

    print("All tests passed successfully!")
