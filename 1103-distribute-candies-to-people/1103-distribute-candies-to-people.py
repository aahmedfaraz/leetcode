class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        person = [0] * num_people
        start = 1
        while candies > 0:
            j = 0
            for i in range(start, start + num_people):
                person[j] += min(i, candies)
                j += 1
                candies -= i
                if candies <= 0:
                    return person
            start += num_people
        return person