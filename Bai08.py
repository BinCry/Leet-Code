from collections import deque


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        """
        LeetCode 2127: Maximum Employees to Be Invited to a Meeting (Hard)

        Mỗi nhân viên chỉ chọn đúng một người yêu thích, vì vậy mảng `favorite`
        tạo thành một đồ thị hàm: mỗi đỉnh có đúng một cạnh đi ra. Mỗi thành phần
        liên thông của đồ thị sẽ chứa đúng một chu trình.

        Một cách xếp hợp lệ quanh bàn tròn chỉ có thể thuộc một trong hai dạng:

        1. Một chu trình có từ 3 người trở lên.
           Không thể gắn thêm người ngoài chu trình vì mỗi người trong chu trình
           đã cần ngồi cạnh hai người thuộc chu trình.

        2. Một hoặc nhiều chu trình gồm đúng 2 người: a <-> b.
           Mỗi đầu của cặp có thể nối thêm một chuỗi nhân viên dài nhất đi vào nó.
           Các cặp 2 chiều độc lập có thể ghép chung quanh một bàn, nên ta cộng
           kết quả của tất cả các cặp.

        Ta dùng topological sort để loại dần các đỉnh không thuộc chu trình.
        Trong lúc loại, `longest_chain[v]` lưu số người lớn nhất trong một chuỗi
        kết thúc tại v (đã tính cả v). Sau đó, các đỉnh còn bậc vào lớn hơn 0
        chính là những đỉnh nằm trong chu trình.

        Độ phức tạp:
        - Thời gian: O(n)
        - Không gian: O(n)
        """
        n = len(favorite)
        indegree = [0] * n

        for person in favorite:
            indegree[person] += 1

        queue = deque(i for i in range(n) if indegree[i] == 0)
        longest_chain = [1] * n

        # Loại các đỉnh không thuộc chu trình và tính chuỗi đi vào dài nhất.
        while queue:
            person = queue.popleft()
            next_person = favorite[person]

            longest_chain[next_person] = max(
                longest_chain[next_person], longest_chain[person] + 1
            )

            indegree[next_person] -= 1
            if indegree[next_person] == 0:
                queue.append(next_person)

        longest_cycle = 0
        total_two_cycles = 0
        visited = [False] * n

        # Sau topological sort, chỉ các đỉnh thuộc chu trình còn indegree > 0.
        for start in range(n):
            if indegree[start] == 0 or visited[start]:
                continue

            cycle = []
            person = start

            while not visited[person]:
                visited[person] = True
                cycle.append(person)
                person = favorite[person]

            if len(cycle) == 2:
                first, second = cycle
                total_two_cycles += longest_chain[first] + longest_chain[second]
            else:
                longest_cycle = max(longest_cycle, len(cycle))

        return max(longest_cycle, total_two_cycles)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Ví dụ cơ bản: cặp 1 <-> 2 nhận thêm người 3 qua người 0.
        ([2, 2, 1, 2], 3),
        # Một chu trình gồm 3 người.
        ([1, 2, 0], 3),
        # Chu trình dài 4 người; người còn lại không thể gắn vào chu trình lớn.
        ([3, 0, 1, 4, 1], 4),
        # Một cặp 2 chiều, mỗi phía có một chuỗi dài 2 đi vào.
        ([1, 0, 0, 1, 2, 3], 6),
        # Hai cặp 2 chiều độc lập có thể cùng ngồi quanh một bàn.
        ([1, 0, 3, 2], 4),
        # Trường hợp nhỏ nhất theo ràng buộc đề bài.
        ([1, 0], 2),
    ]

    for index, (favorite, expected) in enumerate(test_cases, start=1):
        result = solution.maximumInvitations(favorite)
        print(f"Test {index}: favorite = {favorite}")
        print(f"Output: {result} | Expected: {expected}\n")
        assert result == expected

    print("All tests passed!")
