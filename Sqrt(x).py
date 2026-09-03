class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid <= x // mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

# Local testing (LeetCode par ye part nahi likhna)
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))   # 2
    print(sol.mySqrt(8))   # 2
    print(sol.mySqrt(15))  # 3
    print(sol.mySqrt(0))   # 0
    print(sol.mySqrt(1))   # 1