class board():
    def __init__(self):
        self.table = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]
        self.winList = [
             ((0,0),(0,1),(0,2)),
             ((1,0),(1,1),(1,2)),
             ((2,0),(2,1),(2,2)),
             ((0,0),(1,0),(2,0)),
             ((0,1),(1,1),(2,1)),
             ((0,2),(1,2),(2,2)),
             ((0,0),(1,1),(2,2)),
             ((0,2),(1,1),(2,0))
        ]
        self.options = [1,2,3,4,5,6,7,8,9]

    def playMovement(self, symb, pos):
        x = (pos-1) // len(self.table)
        y = (pos-1) % len(self.table)
        self.table[x][y] = symb
        self.options.remove(pos)

    def resetTable(self):
        for i in range(len(self.table)):
            for j in range(len(self.table)):
                self.table[i][j] = " "
        self.options = [1,2,3,4,5,6,7,8,9]