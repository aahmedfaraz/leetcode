class Solution:
    def minimumDeletions(self, s: str) -> int:
        # thought process
        # 0 1 2 3 4 5 6 7 8 9 10 11
        # a a b a b a a |b| b b a  a
        #                i

        # n = 12, a = 7, b = 5

        # get totals
        n = len(s)
        total_a = s.count("a")
        total_b = n - total_a

        # loop through all characters, 
        # considering each character as the border between left and right side
        curr_a_count = 0
        min_deletion = float('inf')
        for i in range(n):
            # get totals on left and right
            a_on_left = curr_a_count
            a_on_right = total_a - a_on_left
            b_on_left = i - a_on_left
            b_on_right = total_b - b_on_left

            # make sure border character is excluded
            if s[i] == "a":
                a_on_right -= 1
                curr_a_count += 1 # also keep tracking count of "a" for next border
            else:
                b_on_right -= 1

            # calculate deletion required as per current border
            curr_deletion = b_on_left + a_on_right

            # track the min deletion count
            min_deletion = min(min_deletion, curr_deletion)

        # return min deletion
        return min_deletion