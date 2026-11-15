class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        result = ""
        carry = 0
        a_index = len(a) - 1
        b_index = len(b) - 1

        while a_index >= 0 or b_index >= 0 or carry > 0:
            if a_index >= 0:
                val_a = int(a[a_index])
            else:
                val_a = 0
            if b_index >= 0:
                val_b = int(b[b_index])
            else:
                val_b = 0
            if val_a + val_b + carry == 0:
                result = '0' + result
                carry = 0
            elif val_a + val_b + carry == 1:
                result = '1' + result
                carry = 0
            elif val_a + val_b + carry == 2:
                result = '0' + result
                carry = 1
            elif val_a + val_b + carry == 3:
                result = '1' + result
                carry = 1
            a_index -= 1
            b_index -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))
    print(sol.addBinary("1010", "1011"))
    print("All tests passed successfully!")
