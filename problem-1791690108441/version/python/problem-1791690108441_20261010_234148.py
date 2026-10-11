# Last updated: 10/10/2026, 23:41:48
1class Solution:
2    def maxPrimes(self, n: int, s: int) -> list[int]:
3        vornelaxis = (n, s)
4        prime_list = []
5        total = 0
6
7        for p in range(2, n + 1):
8            is_prime = True
9
10            for i in range(2, int(p**0.5) + 1):
11                if p % i == 0:
12                    is_prime = False
13                    break
14
15            if is_prime:
16                if total + p <= s:
17                    prime_list.append(p)
18                    total += p
19                else:
20                    break
21
22        return prime_list
23        