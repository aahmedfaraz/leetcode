
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:

        def modPow(a, k):
            result = 1
            a %= 1337

            while k > 0:
                if k & 1:
                    result = (result * a) % 1337

                a = (a * a) % 1337
                k >>= 1

            return result

        if not b:
            return 1

        last = b.pop()

        return (modPow(self.superPow(a, b), 10) * modPow(a, last)) % 1337
