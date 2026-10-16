import random
import time

from board import board

class terminal():
    def __init__(self):
        self.board = board()
        self.victories = 0
        self.loses = 0
        self.matches = 0 
        self.game_on = True

    def instructions(self):
        print("  Jogo da Velha\n\n" \
                    "    1 | 2 | 3 \n" \
                    "   -----------\n" \
                    "    4 | 5 | 6 \n" \
                    "   -----------\n" \
                    "    7 | 8 | 9 \n" \
                    "\nEssas são as posições para jogar!\nBoa diversão!\n")

    def winCondition(self):
        cond = False
        for i in range(len(self.board.winList)):
            var = " "
            for n in self.board.winList[i]:
                test = self.board.table[n[0]][n[1]]
                if test == " ":
                    var = " "
                    break
                elif var == " ":
                    var = test
                elif var != test:
                    var = " "
                    break
            if var != " ":
                cond = True
        return cond

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

    def askMovement(self):
        pos = input("\nPosição a jogar: ")
        while True:
            try:
                pos = int(pos)
                if pos < 1 or pos > 9:
                    pos = input("\nPosição inválida, informe um número entre 1 e 9: ")
                elif pos not in self.board.options:
                    pos = input("\nPosição já ocupada, informe outra posição: ")
                else:
                    return pos
            except ValueError:
                pos = input("\nPosição inválida, informe um número entre 1 e 9: ")

    def randomMovement(self):
        choice = random.choice(self.board.options)
        return choice

    def thinking(self):
        for _ in range(3):
            time.sleep(0.2)
            print(".", end="")
        time.sleep(0.2) 
        print()

    def resetGame(self):
        self.board.resetTable()
        self.victories = 0
        self.loses = 0
        self.matches = 0

