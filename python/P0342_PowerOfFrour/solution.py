class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n > 1 and n % 4 == 0:
            n = n // 4

        if n == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfFour(16))
    print(sol.isPowerOfFour(5))
    print(sol.isPowerOfFour(1))
    print("All tests passed successfully!")