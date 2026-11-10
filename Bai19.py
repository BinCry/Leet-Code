from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        LeetCode 19: Remove Nth Node From End of List (Medium)

        Use a dummy node and two pointers. Move ``fast`` n + 1 steps ahead,
        then move both pointers together. ``slow.next`` is the node to remove
        when ``fast`` reaches the end.

        Complexity:
        - Time: O(L), where L is the linked-list length
        - Extra space: O(1)
        """
        dummy = ListNode(0, head)
        fast: Optional[ListNode] = dummy
        slow: Optional[ListNode] = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    values: list[int] = []

    while head:
        values.append(head.val)
        head = head.next

    return values


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ]

    for index, (values, n, expected) in enumerate(test_cases, start=1):
        result = solution.removeNthFromEnd(build_linked_list(values), n)
        result_values = linked_list_to_list(result)
        assert result_values == expected, (
            f"Test {index} failed: expected {expected}, got {result_values}"
        )
        print(f"Test {index:02d}: PASSED")

    print("All tests passed successfully!")
