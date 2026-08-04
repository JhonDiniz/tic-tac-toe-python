import time

class terminal_game():
    def __init__(self, board):
        self.game_on = True
        self.board = board

    def showTable(self):
            tam = len(self.board.table)
            for i in range(tam):
                print("   ", end="")
                for l in range(tam - 1):
                    print(f" {self.board.table[i][l]} |", end="")
                print(f" {self.board.table[i][tam - 1]}")
                if i < tam - 1:
                    print("   -----------")
            print("\n")

    def reset(self):
        for i in range(len(self.board.table)):
            for j in range(len(self.board.table)):
                self.board.table[i][j] = " "

    def interface(self):
            ask = input("O que deseja fazer?\n" \
                        "1 - Jogar Novamete\n" \
                        "2 - Voltar ao Menu\n" \
                        "3 - Sair do Jogo\n")
            while True:
                try:
                    ask = int(ask)
                    if ask < 1 or ask > 3:
                        ask = input("Opção inválida, informe 1, 2 ou 3: ")
                    else:
                        return ask
                except ValueError:
                    ask = input("Opção inválida, informe 1, 2 ou 3: ")
        
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
            symbol_p1 = input("\nInforme o símbolo do Jogador 1 (X / O)\n")
            while symbol_p1.upper() != "X" and symbol_p1.upper() != "O":
                symbol_p1 = input("\nSímbolo inválido, informe X ou O\n")
            if symbol_p1.upper() == "X":
                symbol_p2 = "O"
            else:
                symbol_p2 = "X"
            turn = 1
            turn_limit = len(tabela.table) ** 2 + 1

            while not tabela.winCond() and not turn > turn_limit:
                if self.board.matches % 2 == 0:
                    if turn % 2 == 0:
                        symbol = symbol_p2.upper()
                    else:
                        symbol = symbol_p1.upper()
                else:
                    if turn % 2 == 0:
                        symbol = symbol_p1.upper()
                    else:
                        symbol = symbol_p2.upper()
                player = (turn + self.board.matches + 1) % 2 + 1
                print(f"\nRodada {turn}",
                        f"\nJogador : {player} \n")
                self.showTable()
                pos = input("\nPosição a jogar: ")
                while True:
                    try:
                        pos = int(pos)
                        if pos < 1 or pos > 9:
                            pos = input("\nPosição inválida, informe um número entre 1 e 9: ")
                        elif pos not in self.board.options:
                            pos = input("\nPosição já ocupada, informe outra posição: ")
                        else:
                            self.board.options.remove(pos)
                            break
                    except ValueError:
                        pos = input("\nPosição inválida, informe um número entre 1 e 9: ")
                tabela.play(symbol, pos)
                turn += 1
                if tabela.winCond():
                    print()
                    self.showTable()
                    print(f"O Jogador {player} ganhou!!\n")
                    if self.board.matches % 2 == 0:
                        if turn % 2 == 0:
                            self.board.victories += 1
                        else:
                            self.board.loses += 1
                    else:
                        if turn % 2 == 0:
                            self.board.loses += 1
                        else:
                            self.board.victories += 1
                elif turn == turn_limit:
                    self.showTable()
                    print("Empate!!\n")
                if turn == turn_limit or tabela.winCond():
                    if self.interface() == 1:
                        self.board.reset()
                        turn = 1
                        self.board.matches += 1
                        print(f"\n     Placar\n" \
                            f"Partidas jogadas: {self.board.matches}\n" \
                            f"Jogador 1 | {self.board.victories} X {self.board.loses} | Jogador 2")
                        time.sleep(0.5)
                    elif self.interface() == 2:
                        self.board.reset()
                        turn = 1
                        self.board.matches = 0
                    else:
                        print("Programa Finalizado.")
                        self.game_on = False