from terminal_1v1 import terminal_game
from terminal_AI_Easy import terminal_AI_random
from terminal_AI_Medium import terminal_AI_smart
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
        self.victories = 0
        self.loses = 0
        self.matches = 0
        self.voltar = 0

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

    def reset(self):
        for i in range(len(self.table)):
            for j in range(len(self.table)):
                self.table[i][j] = " "
        self.options = [1,2,3,4,5,6,7,8,9]


#---------------------------------------------------------------------------------------#

tabela = board()
while not tabela.voltar:
    tabela.voltar = 0
    game_choose = int(input("Informe o modo de jogo:\n" \
    "1 - Jogador X Jogador\n" \
    "2 - Jogador X IA\n"))
    if game_choose == 1:
        game = terminal_game(tabela)
    else:
        dif_level = int(input("\nEscolha a dificuldade:\n" \
        "1 - Fácil\n2 - Médio\n3 - Difícil\n"))
        if dif_level == 1:
            game = terminal_AI_random(tabela)
        elif dif_level == 2:
            game = terminal_AI_smart(tabela)
    game.start()
    