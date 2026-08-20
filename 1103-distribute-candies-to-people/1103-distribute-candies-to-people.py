class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        person = [0] * num_people
        i = 0
        amount = 1
        while candies > 0:
            amount = min(amount, candies)
            person[i] += amount
            candies -= amount
            amount += 1
            i += 1
            if i == num_people:
                i = 0
        return person