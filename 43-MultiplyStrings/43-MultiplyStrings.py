# Last updated: 10/12/2025, 07:42:49
class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                prod = digit1 * digit2
                sum_val = prod + res[i + j + 1]

                res[i + j + 1] = sum_val % 10
                res[i + j] += sum_val // 10

        result = []
        for x in res:
            if not (len(result) == 0 and x == 0):
                result.append(str(x))

        return "".join(result)
