class Solution:
    def maxScoreKDisjointPaths(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:
        """
        LeetCode Custom (Hard): Maximum Score of at Most K Disjoint Paths on a Weighted Tree

        Đề bài:
        Cho một cây vô hướng gồm `n` đỉnh (được đánh số từ 0 đến n - 1) với n - 1 cạnh.
        - Mỗi đỉnh u có giá trị `values[u]` (có thể âm, dương hoặc bằng 0).
        - Mỗi cạnh nối u và v có trọng số `w` (chi phí di chuyển qua cạnh đó).
        
        Một đường đi đơn (simple path) P gồm dãy các đỉnh phân biệt v1 -> v2 -> ... -> vm.
        Điểm số của đường đi P được tính bằng:
            Score(P) = Tổng(values[vi]) - Tổng(w(vi, vi+1))
        (Đường đi chỉ gồm 1 đỉnh v có Score(P) = values[v]).

        Bạn được chọn tối đa `k` đường đi đơn đôi một KHÔNG giao nhau về đỉnh
        (vertex-disjoint, tức mỗi đỉnh thuộc cây xuất hiện trong tối đa 1 đường đi đã chọn).
        Bạn cũng có thể chọn 0 đường đi (khi đó tổng điểm là 0).

        Hãy tìm tổng điểm số lớn nhất có thể đạt được.

        Phương pháp tiếp cận: Quy hoạch động trên Cây (Tree DP) + Tree Knapsack
        -----------------------------------------------------------------------
        Mỗi đường đi đơn trên cây có đúng MỘT đỉnh cao nhất (Topmost / LCA node).
        Tại đỉnh cao nhất u, đường đi đó sẽ được hoàn thành (tính là 1 đường đi trọn vẹn).

        Với mỗi đỉnh u, ta xét các trạng thái tương tác với cây con và đỉnh cha:
        1. `dp0[u][c]`: Tổng điểm lớn nhất trong cây con gốc u với `c` đường đi đã hoàn thành,
           trong đó đỉnh u KHÔNG nối cạnh lên đỉnh cha.
        2. `dp1[u][c]`: Tổng điểm lớn nhất trong cây con gốc u với `c` đường đi đã hoàn thành,
           trong đó đỉnh u ĐANG KẾT NỐI một nhánh đi lên đỉnh cha (đường đi này chưa hoàn thành,
           sẽ được chốt tại một tổ tiên của u).

        Tại mỗi đỉnh u, khi gộp các cây con của các con v (cạnh trọng số w):
        - Đỉnh u có thể nhận 0, 1 hoặc 2 nhánh đi xuống từ các con.
        - Ta duy trì `cur[c][d]`: Điểm lớn nhất khi u đã nối `d` nhánh con (d in {0, 1, 2})
          và có `c` đường đi đã hoàn thành trong các cây con đã xét.
        - Duy trì `unused[c]`: Điểm lớn nhất khi u hoàn toàn không tham gia vào đường đi nào.

        Chuyển trạng thái khi xét thêm một con v:
        - Nếu v không nối lên u: v đóng góp `dp0[v][c_v]`.
        - Nếu v có nối lên u (chỉ khi d < 2): nhánh con này mang lại `dp1[v][c_v] - w`.

        Sau khi duyệt hết các con của u:
        - `dp0[u][c]` = max(unused[c], cur[c-1][0], cur[c-1][1], cur[c-1][2]) (với c >= 1)
          (vì đỉnh u là đỉnh cao nhất của đường đi nên đường đi được hoàn thành tại u: tốn 1 quota).
        - `dp1[u][c]` = max(cur[c][0], cur[c][1])
          (u nối lên cha nên đường đi chưa kết thúc, không tốn quota tại u).

        Tối ưu hóa Tree Knapsack bằng cận kích thước cây con:
        - Tổng số phép tính khi gộp hai cây con kích thước S1 và S2 bị chặn bởi O(S1 * S2).
        - Với việc giới hạn số đường đi tối đa là k, tổng độ phức tạp toàn bài là O(n * k).

        Độ phức tạp:
        - Thời gian: O(n * k)
        - Không gian: O(n * k)
        """
        if n == 0 or k == 0:
            return 0

        # Xây dựng danh sách kề
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Duyệt cây theo thứ tự hậu thứ tự (Post-order traversal) bằng stack
        order = []
        parent = [-1] * n
        stack = [0]
        visited = [False] * n
        visited[0] = True

        while stack:
            u = stack.pop()
            order.append(u)
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)

        order.reverse()  # Thứ tự từ lá lên gốc

        dp0: list[list[float]] = [[] for _ in range(n)]
        dp1: list[list[float]] = [[] for _ in range(n)]
        sub_size = [1] * n
        INF = float("inf")

        for u in order:
            cur_sz = 1
            unused = [0.0] + [-INF] * k
            cur = [[-INF] * 3 for _ in range(k + 1)]
            cur[0][0] = float(values[u])

            for v, w in adj[u]:
                if v == parent[u]:
                    continue

                v_sz = sub_size[v]
                new_sz = cur_sz + v_sz
                max_c = min(k, new_sz)

                next_unused = [-INF] * (max_c + 1)
                next_cur = [[-INF] * 3 for _ in range(max_c + 1)]

                v_dp0 = dp0[v]
                v_dp1 = dp1[v]

                limit_u = min(cur_sz, k)
                limit_v = min(v_sz, k)

                for c_u in range(limit_u + 1):
                    # 1. Cập nhật nhánh u không sử dụng (unused)
                    if unused[c_u] != -INF:
                        for c_v in range(min(limit_v, k - c_u) + 1):
                            val0 = v_dp0[c_v]
                            if val0 != -INF:
                                total = unused[c_u] + val0
                                if total > next_unused[c_u + c_v]:
                                    next_unused[c_u + c_v] = total

                    # 2. Cập nhật nhánh u có tham gia đường đi (cur)
                    for d in range(3):
                        cur_val = cur[c_u][d]
                        if cur_val == -INF:
                            continue

                        for c_v in range(min(limit_v, k - c_u) + 1):
                            val0 = v_dp0[c_v]
                            # Trường hợp con v KHÔNG nối lên u
                            if val0 != -INF:
                                total0 = cur_val + val0
                                if total0 > next_cur[c_u + c_v][d]:
                                    next_cur[c_u + c_v][d] = total0

                            # Trường hợp con v CÓ nối lên u (tăng số nhánh d lên 1)
                            if d < 2:
                                val1 = v_dp1[c_v]
                                if val1 != -INF:
                                    total1 = cur_val + val1 - w
                                    if total1 > next_cur[c_u + c_v][d + 1]:
                                        next_cur[c_u + c_v][d + 1] = total1

                unused = next_unused
                cur = next_cur
                cur_sz = new_sz

            sub_size[u] = cur_sz
            limit_c = min(k, cur_sz)

            res0 = [-INF] * (limit_c + 1)
            res1 = [-INF] * (limit_c + 1)

            for c in range(limit_c + 1):
                # Trạng thái 0: u không nối lên cha
                best0 = unused[c]
                if c >= 1:
                    best0 = max(best0, cur[c - 1][0], cur[c - 1][1], cur[c - 1][2])
                res0[c] = best0

                # Trạng thái 1: u nối lên cha (đường đi chưa chốt, giữ nguyên c)
                res1[c] = max(cur[c][0], cur[c][1])

            dp0[u] = res0
            dp1[u] = res1

        # Kết quả tại gốc (đỉnh 0) không có cạnh lên cha, lấy max trên mọi số lượng đường đi c <= k
        max_total_score = 0.0
        for score in dp0[0]:
            if score > max_total_score:
                max_total_score = score

        return int(max_total_score)


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Cây đơn giản gồm 4 đỉnh, so sánh k = 1 và k = 2
    # Cây: 0 -(2)- 1, 0 -(1)- 2, 2 -(3)- 3
    # values = [10, 8, 15, 6]
    n1 = 4
    edges1 = [[0, 1, 2], [0, 2, 1], [2, 3, 3]]
    values1 = [10, 8, 15, 6]
    k1 = 2
    # Với k = 2, chọn 2 đường rời:
    # Đường 1: 1 -> 0 -> 2 (điểm = 8 + 10 + 15 - 2 - 1 = 30)
    # Đường 2: 3 (điểm = 6)
    # Tổng điểm = 30 + 6 = 36.
    print(f"Test 1: n = {n1}, values = {values1}, k = {k1}")
    output1 = solution.maxScoreKDisjointPaths(n1, edges1, values1, k1)
    print(f"Output: {output1} | Expected: 36\n")
    assert output1 == 36

    # Test case 2: Cây hình sao (Star graph), k = 1 (tìm đường kính trọng số lớn nhất)
    n2 = 5
    edges2 = [[0, 1, 1], [0, 2, 1], [0, 3, 5], [0, 4, 1]]
    values2 = [5, 10, 12, 20, 8]
    k2 = 1
    # Đường đi tối ưu là 3 -> 0 -> 2: 20 + 5 + 12 - (5 + 1) = 31
    print(f"Test 2: n = {n2}, values = {values2}, k = {k2}")
    output2 = solution.maxScoreKDisjointPaths(n2, edges2, values2, k2)
    print(f"Output: {output2} | Expected: 31\n")
    assert output2 == 31

    # Test case 3: Đường thẳng (Line graph) với nút âm ở giữa ngăn cách
    # 0 -(1)- 1 -(10)- 2 -(1)- 3
    # values = [20, 20, -50, 30]
    n3 = 4
    edges3 = [[0, 1, 1], [1, 2, 10], [2, 3, 1]]
    values3 = [20, 20, -50, 30]
    k3 = 2
    # Với k = 2, ta không đi qua nút 2 (-50) và cạnh trọng số 10.
    # Chọn 2 đường rời: Đường 1 (0 -> 1: 20 + 20 - 1 = 39) và Đường 2 (3: 30), tổng = 69.
    print(f"Test 3: n = {n3}, values = {values3}, k = {k3}")
    output3 = solution.maxScoreKDisjointPaths(n3, edges3, values3, k3)
    print(f"Output: {output3} | Expected: 69\n")
    assert output3 == 69

    # Test case 4: Cây toàn giá trị âm hoặc k = 0 (Corner case: chọn 0 đường đi)
    n4 = 3
    edges4 = [[0, 1, 5], [1, 2, 5]]
    values4 = [-10, -20, -30]
    k4 = 2
    print(f"Test 4: n = {n4}, values = {values4}, k = {k4}")
    output4 = solution.maxScoreKDisjointPaths(n4, edges4, values4, k4)
    print(f"Output: {output4} | Expected: 0\n")
    assert output4 == 0

    # Test case 5: Cây chỉ có đúng 1 đỉnh (Single node corner case)
    n5 = 1
    edges5 = []
    values5 = [100]
    k5 = 1
    print(f"Test 5: n = {n5}, values = {values5}, k = {k5}")
    output5 = solution.maxScoreKDisjointPaths(n5, edges5, values5, k5)
    print(f"Output: {output5} | Expected: 100\n")
    assert output5 == 100

    # Test case 6: Cây phân nhánh với k = 3
    # Cây: 0-(2)-1, 0-(2)-2, 1-(1)-3, 1-(1)-4, 2-(1)-5
    # values: [4, 10, 8, 15, 12, 7]
    n6 = 6
    edges6 = [[0, 1, 2], [0, 2, 2], [1, 3, 1], [1, 4, 1], [2, 5, 1]]
    values6 = [4, 10, 8, 15, 12, 7]
    k6 = 3
    # Lựa chọn 3 đường rời:
    # 1. Đường 3 -> 1 -> 4: 15 + 10 + 12 - 1 - 1 = 35
    # 2. Đường 2 -> 5: 8 + 7 - 1 = 14
    # 3. Đường 0: 4
    # Tổng = 35 + 14 + 4 = 53
    print(f"Test 6: n = {n6}, values = {values6}, k = {k6}")
    output6 = solution.maxScoreKDisjointPaths(n6, edges6, values6, k6)
    print(f"Output: {output6} | Expected: 53\n")
    assert output6 == 53

    print("All tests passed successfully!")
