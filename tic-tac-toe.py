from terminal import terminal_game
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

    def play(self, symb, pos):
        x = (pos-1) // len(self.table)
        y = (pos-1) % len(self.table)
        if self.table[x][y] == " ":
            self.table[x][y] = symb

    def winCond(self):
        cond = False
        for i in range(len(self.winList)):
            var = " "
            for n in self.winList[i]:
                test = self.table[n[0]][n[1]]
                if test == " ":
                    var = " "
                    break
                elif var == " ":
                    var = test
                else:
                    if var != test:
                        var = " "
                        break
            if var != " ":
                cond = True
                return cond
        return False



#---------------------------------------------------------------------------------------#

tabela = board()
game = terminal_game(tabela)
game.start()
    