from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Khởi tạo một defaultdict với giá trị mặc định là list
        # Điều này giúp ta không cần kiểm tra key đã tồn tại hay chưa
        ans = collections.defaultdict(list)
        
        for s in strs:
            # Sắp xếp các ký tự trong chuỗi để tạo ra một key chung cho các chuỗi là anagram
            # tuple() được sử dụng vì list không thể làm key trong dictionary (không hashable)
            key = tuple(sorted(s))
            ans[key].append(s)
            
        # Trả về danh sách các nhóm
        return list(ans.values())

if __name__ == "__main__":
    solution = Solution()
    # Test case ví dụ
    print("Input: [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]")
    print("Output:", solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
