from collections import deque


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)

        # Trường hợp biên: Đồ thị chỉ có 1 node (không cần bước di chuyển nào)
        if n <= 1:
            return 0

        # Trạng thái mục tiêu: Tất cả n nodes đều đã được thăm (tất cả n bit đều là 1)
        target_mask = (1 << n) - 1

        # Hàng đợi BFS lưu: (node_hien_tai, mask_cac_node_da_tham, so_buoc)
        # Vì có thể bắt đầu từ BẤT KỲ node nào, ta đẩy tất cả các node vào hàng đợi ban đầu
        queue = deque()

        # visited[node][mask]: Đánh dấu trạng thái (node, mask) đã được xét hay chưa
        # Giúp tránh việc duyệt lặp lại cùng một trạng thái với số bước lớn hơn
        visited = [[False] * (1 << n) for _ in range(n)]

        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited[i][mask] = True

        # BFS duyệt theo từng mức khoảng cách
        while queue:
            curr_node, curr_mask, dist = queue.popleft()

            # Nếu đã đi qua tất cả các node, trả về khoảng cách
            # Do BFS duyệt theo thứ tự khoảng cách tăng dần nên kết quả đầu tiên đạt target_mask luôn là ngắn nhất
            if curr_mask == target_mask:
                return dist

            # Duyệt qua tất cả các đỉnh kề với đỉnh hiện tại
            for neighbor in graph[curr_node]:
                next_mask = curr_mask | (1 << neighbor)

                # Nếu trạng thái (neighbor, next_mask) chưa từng xuất hiện
                if not visited[neighbor][next_mask]:
                    visited[neighbor][next_mask] = True
                    queue.append((neighbor, next_mask, dist + 1))

        return 0


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Đồ thị dạng hình sao (Star graph)
    graph1 = [[1, 2, 3], [0], [0], [0]]
    print(f"Test 1: graph = {graph1}")
    print(f"Output: {solution.shortestPathLength(graph1)}")  # Expected: 4 (vd: 1 -> 0 -> 2 -> 0 -> 3)

    # Test case 2: Đồ thị phức tạp có chu trình
    graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    print(f"\nTest 2: graph = {graph2}")
    print(f"Output: {solution.shortestPathLength(graph2)}")  # Expected: 4 (vd: 0 -> 1 -> 4 -> 2 -> 3)

    # Test case 3: Đồ thị chỉ có 1 node (Corner case)
    graph3 = [[]]
    print(f"\nTest 3: graph = {graph3}")
    print(f"Output: {solution.shortestPathLength(graph3)}")  # Expected: 0

    # Test case 4: Đồ thị đường thẳng (Line graph: 0 - 1 - 2)
    graph4 = [[1], [0, 2], [1]]
    print(f"\nTest 4: graph = {graph4}")
    print(f"Output: {solution.shortestPathLength(graph4)}")  # Expected: 2 (0 -> 1 -> 2)

    # Test case 5: Đồ thị vòng (Cycle graph: 0 - 1 - 2 - 3 - 0)
    graph5 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(f"\nTest 5: graph = {graph5}")
    print(f"Output: {solution.shortestPathLength(graph5)}")  # Expected: 3 (0 -> 1 -> 2 -> 3)
