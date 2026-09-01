class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        n = len(stones)

        # Điều kiện cần và đủ để gộp n đống thành 1 đống:
        # Mỗi bước gộp k đống thành 1 đống -> số đống giảm đi (k - 1).
        # Sau m bước: n - m * (k - 1) = 1  =>  (n - 1) % (k - 1) == 0
        if (n - 1) % (k - 1) != 0:
            return -1

        # Mảng cộng dồn prefix sum để tính tổng subarray stones[i..j] trong O(1)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i][j]: Chi phí nhỏ nhất để gộp đoạn stones[i..j] thành số đống ít nhất có thể
        # Nếu (j - i) % (k - 1) == 0: đoạn này có thể gộp về đúng 1 đống
        dp = [[0] * n for _ in range(n)]

        # Duyệt độ dài của đoạn (length từ 2 đến n)
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                # Tách đoạn [i, j] thành [i, p] và [p + 1, j]
                # Vì [i, p] cần gộp thành 1 đống nên p tăng theo bước (k - 1)
                for p in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][p] + dp[p + 1][j])

                # Nếu đoạn [i..j] có thể gộp thành đúng 1 đống (tức là trước bước này nó có k đống)
                # Ta cộng thêm chi phí gộp k đống đó lại = tổng các phần tử từ i đến j
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][n - 1]


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    stones1 = [3, 2, 4, 1]
    k1 = 2
    print(f"Test 1: stones = {stones1}, k = {k1}")
    print(f"Output: {solution.mergeStones(stones1, k1)}")  # Expected: 20

    # Test case 2
    stones2 = [3, 2, 4, 1]
    k2 = 3
    print(f"\nTest 2: stones = {stones2}, k = {k2}")
    print(f"Output: {solution.mergeStones(stones2, k2)}")  # Expected: -1

    # Test case 3
    stones3 = [3, 5, 1, 2, 6]
    k3 = 3
    print(f"\nTest 3: stones = {stones3}, k = {k3}")
    print(f"Output: {solution.mergeStones(stones3, k3)}")  # Expected: 25

    # Test case 4 (Corner case: Chỉ có 1 đống)
    stones4 = [7]
    k4 = 2
    print(f"\nTest 4: stones = {stones4}, k = {k4}")
    print(f"Output: {solution.mergeStones(stones4, k4)}")  # Expected: 0

    # Test case 5 (Corner case: Gộp đúng 1 lần cho cả mảng)
    stones5 = [1, 2, 3]
    k5 = 3
    print(f"\nTest 5: stones = {stones5}, k = {k5}")
    print(f"Output: {solution.mergeStones(stones5, k5)}")  # Expected: 6
