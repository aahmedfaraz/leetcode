class Robot:
    def __init__(self, width: int, height: int):
        self.w, self.h = width, height
        self.x, self.y = 0, 0
        self.dir = "East"
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        num %= (2 * (self.w - 1) + 2 * (self.h - 1))
        
        for _ in range(num):
            if self.dir == "East" and self.x == self.w - 1: self.dir = "North"
            elif self.dir == "North" and self.y == self.h - 1: self.dir = "West"
            elif self.dir == "West" and self.x == 0: self.dir = "South"
            elif self.dir == "South" and self.y == 0: self.dir = "East"
            
            if self.dir == "East": self.x += 1
            elif self.dir == "North": self.y += 1
            elif self.dir == "West": self.x -= 1
            elif self.dir == "South": self.y -= 1

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.x == 0 and self.y == 0 and not self.moved: return "East"
        if self.x == 0 and self.y == 0 and self.moved: return "South" # Special case
        return self.dir

# Time = O(1)
# Space = O(1)