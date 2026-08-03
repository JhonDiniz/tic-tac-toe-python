game_on = True

class table():
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
             
    def showTable(self):
        for i in range(3):
            print("   ", end="")
            for l in range(2):
                print(" "+self.table[i][l]+" |", end="")
            print(" "+self.table[i][2])
            if i < 2:
                print("   -----------")
        print("\n")

    def play(self, symb, pos):
        x = (pos-1) // 3
        y = (pos-1) % 3
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

while game_on:
    tabela = table()
    print("  Jogo da Velha\n\n" \
    "    1 | 2 | 3 \n" \
    "   -----------\n" \
    "    4 | 5 | 6 \n" \
    "   -----------\n" \
    "    7 | 8 | 9 \n" \
    "\nEssas são as posições para jogar!\n")
    symbol_p1 = str(input("\nInforme o símbolo do Player 1 (X / O)\n"))
    if symbol_p1.upper() == "X":
        symbol_p2 = "O"
    else:
        symbol_p2 = "X"
    round = 1

    while not tabela.winCond():
        if round % 2 == 0:
            symbol = symbol_p2.upper()
        else:
            symbol = symbol_p1.upper()
        player = (round+1)%2+1
        print("\nRodada "+str(round),
              "\nJogador : "+str(player) + "\n")
        tabela.showTable()
        pos = int(input("\nPosição a jogar: "))
        tabela.play(symbol, pos)

        if tabela.winCond():
            print("O Jogador "+str(player)+" ganhou!!\n\n")
        else:
            round+=1