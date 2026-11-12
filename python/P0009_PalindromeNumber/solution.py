class Solution(object):
    def is_palindrome(self, x):
        """
        :param x: int
        :return: bool
        """
        x = str(x)
        is_a_palindrome = True
        k = 0
        max_test = len(x)-1
        while is_a_palindrome and k < max_test:
            if x[k] == x[max_test]:
                k += 1
                max_test -= 1
            else:
                is_a_palindrome = False
        return is_a_palindrome


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_palindrome(121))
    print(sol.is_palindrome(1221))
    print(sol.is_palindrome(1))
    print(sol.is_palindrome(-1221))
    print(sol.is_palindrome(10))




