class Solution:
    def isValid(self, s: str) -> bool:
        """
        LeetCode 20: Valid Parentheses (Easy)

        Keep opening brackets in a stack. Every closing bracket must match the
        most recent opening bracket; otherwise the string is invalid.

        Complexity:
        - Time: O(n)
        - Extra space: O(n)
        """
        matching_opening_bracket = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []

        for character in s:
            if character in matching_opening_bracket:
                if not stack or stack.pop() != matching_opening_bracket[character]:
                    return False
            else:
                stack.append(character)

        return not stack


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
    ]

    for index, (parentheses, expected) in enumerate(test_cases, start=1):
        result = solution.isValid(parentheses)
        assert result == expected, f"Test {index} failed: expected {expected}, got {result}"
        print(f"Test {index:02d}: PASSED")

    print("All tests passed successfully!")
