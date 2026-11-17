
class Solution:

    def plusOne(self, digits):
        initial_number = ""
        final_number = 0
        result = []

        for element in digits:
            initial_number = initial_number + str(element)

        final_number = int(initial_number) + 1
        final_number = str(final_number)

        for i in range(len(final_number)):
            result.append(int(final_number[i]))

        return result


if __name__ == "__main__":
    sol = Solution()

    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert sol.plusOne([9]) == [1, 0]

    assert sol.plusOne([9, 9]) == [1, 0, 0]
    assert sol.plusOne([1, 9, 9]) == [2, 0, 0]
    assert sol.plusOne([0]) == [1]

    print("All tests passed successfully!")