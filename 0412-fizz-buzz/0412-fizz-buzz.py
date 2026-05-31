class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            curr = ""
            if i % 3 == 0:
                curr = "Fizz"
            if i % 5 == 0:
                curr += "Buzz"
            if not curr:
                curr = f'{i}'
            answer.append(curr)
        return answer