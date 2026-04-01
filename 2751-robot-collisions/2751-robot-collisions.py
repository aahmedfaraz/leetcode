class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)])

        robosToRight = []  # stack: (index, health)
        survivors = []

        for pos, hth, drc, i in robots:
            if drc == "R":
                robosToRight.append((i, hth))
            else:
                while robosToRight and hth > 0:
                    idx, nextRoboHealth = robosToRight[-1]

                    if nextRoboHealth > hth:
                        robosToRight[-1] = (idx, nextRoboHealth - 1)
                        hth = 0
                    elif nextRoboHealth < hth:
                        robosToRight.pop()
                        hth -= 1
                    else:  # equal
                        robosToRight.pop()
                        hth = 0
                        break

                if hth > 0:
                    survivors.append((i, hth))

        # add remaining right-moving robots
        survivors.extend(robosToRight)

        # sort by original index
        survivors.sort()

        return [h for _, h in survivors]

# Time = O(n log n)
# Space = O(n)