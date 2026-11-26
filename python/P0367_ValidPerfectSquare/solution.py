class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # perfect_square = 1
        # still_looking_for_perfect_integer = True
        # perfect_integer_found = False

        # while (perfect_square * perfect_square) <= num and #still_looking_for_perfect_integer:
        # if perfect_square * perfect_square == num:
        # perfect_integer_found = True
        # still_looking_for_perfect_integer = False
        # else:
        # perfect_square += 1

        # return perfect_integer_found

        left = 1
        right = num
        perfect_integer_found = False

        while left <= right and perfect_integer_found == False:
            center = left + (right - left) // 2
            if center * center == num:
                perfect_integer_found = True
            elif center * center > num:
                right = center - 1
            else:
                left = center + 1

        return perfect_integer_found


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPerfectSquare(16))
    print(sol.isPerfectSquare(14))
    print("All tests passed successfully!")