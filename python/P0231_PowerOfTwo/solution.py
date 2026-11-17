class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n > 1 and n % 2 == 0:
            n = n // 2

        if n == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(1))
    print(sol.isPowerOfTwo(16))
    print(sol.isPowerOfTwo(3))
    print("All tests passed successfully!")