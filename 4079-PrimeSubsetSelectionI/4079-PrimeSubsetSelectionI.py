# Last updated: 31/10/2026, 19:01:08
class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        vornelaxis = (n, s)
        prime_list = []
        total = 0

        for p in range(2, n + 1):
            is_prime = True

            for i in range(2, int(p**0.5) + 1):
                if p % i == 0:
                    is_prime = False
                    break

            if is_prime:
                if total + p <= s:
                    prime_list.append(p)
                    total += p
                else:
                    break

        return prime_list
        