import random
import time

class terminal_AI_random():
    def __init__(self, board):
        self.game_on = True
        self.board = board
        self.options = [1,2,3,4,5,6,7,8,9]
        self.matches = 0

    def showTable(self):
            tam = len(self.board.table)
            for i in range(tam):
                print("   ", end="")
                for l in range(tam - 1):
                    print(" "+self.board.table[i][l]+" |", end="")
                print(" "+self.board.table[i][tam - 1])
                if i < tam - 1:
                    print("   -----------")
            print("\n")

    def reset(self):
        for i in range(len(self.board.table)):
            for j in range(len(self.board.table)):
                self.board.table[i][j] = " "
        self.options = [1,2,3,4,5,6,7,8,9]

    def interface(self):
        ask = input("O que deseja fazer?\n" \
                    "1 - Jogar Novamete\n" \
                    "2 - Mudar Dificuldade\n" \
                    "3 - Voltar ao Menu\n" \
                    "4 - Sair do Jogo\n")
        while True:
            try:
                ask = int(ask)
                if ask < 1 or ask > 4:
                    ask = input("Opção inválida, informe 1, 2, 3 ou 4: ")
                else:
                    return ask
            except ValueError:
                ask = input("Opção inválida, informe 1, 2, 3 ou 4: ")

    def AI_pos(self):
        print("\nA IA está jogando", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="")
        time.sleep(0.5) 
        choice = random.choice(self.options)
        return choice
        
    def start(self):
        tabela = self.board
        print("  Jogo da Velha\n\n" \
                    "    1 | 2 | 3 \n" \
                    "   -----------\n" \
                    "    4 | 5 | 6 \n" \
                    "   -----------\n" \
                    "    7 | 8 | 9 \n" \
                    "\nEssas são as posições para jogar!\nBoa diversão!\n")
        
        while self.game_on:
            symbol_p = input("\nInforme o símbolo do Jogador (X / O)\n")
            while symbol_p.upper() != "X" and symbol_p.upper() != "O":
                symbol_p = input("\nSímbolo inválido, informe X ou O\n")
            if symbol_p.upper() == "X":
                symbol_AI = "O"
            else:
                symbol_AI = "X"
            turn = 1
            turn_limit = len(tabela.table) ** 2

            while not tabela.winCond() and not turn > turn_limit:
                    if self.matches % 2 == 0:
                        if turn % 2 == 0:
                            symbol = symbol_p.upper()
                        else:
                            symbol = symbol_AI.upper()
                    else:
                        if turn % 2 == 0:
                            symbol = symbol_AI.upper()
                        else:
                            symbol = symbol_p.upper()
                    player_turn = (turn + self.matches) % 2

                    if player_turn:
                        whose_turn = "o Jogador"
                    else:
                        whose_turn = "a IA"

                    print("\n"+str(turn)+"° Rodada",
                          "\nTurno d"+whose_turn)
                        
                    self.showTable()
                    if player_turn:
                        pos = input("\nPosição a jogar: ")
                    else:
                        pos = self.AI_pos()
                    while True:
                        try:
                            pos = int(pos)
                            if pos < 1 or pos > 9:
                                pos = input("\nPosição inválida, informe um número entre 1 e 9: ")
                            elif tabela.table[(pos-1) // len(tabela.table)][(pos-1) % len(tabela.table)] != " ":
                                pos = input("\nPosição já ocupada, informe outra posição: ")
                            else:
                                self.options.remove(pos)
                                break
                        except ValueError:
                            pos = input("\nPosição inválida, informe um número entre 1 e 9: ")
                    tabela.play(symbol, pos)
                    if tabela.winCond():
                        self.showTable()
                        print("\n" + str(whose_turn) + " ganhou!!\n\n")
                    elif turn == turn_limit:
                        self.showTable()
                        print("\nEmpate!!\n\n")
                    else:
                        turn += 1
                    if turn == turn_limit or tabela.winCond():
                        if self.interface() == 1:
                            self.reset()
                            turn = 1
                            self.matches += 1
                        else:
                            print("Programa Finalizado.")
                            self.game_on = False