import time

from terminal import terminal

class playerXplayer(terminal):
    def __init__(self):
        super().__init__()
        
    def start(self):
        self.instructions()
        while self.game_on:

            # Escolha do X ou O dos jogadores
            while True:
                try:
                    symbol_p1 = input("\nInforme o símbolo do Jogador 1 (X / O)\n")
                    if symbol_p1.upper() != "X" and symbol_p1.upper() != "O":
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("\nSímbolo inválido, informe X ou O!\n")
            if symbol_p1.upper() == "X":
                symbol_p2 = "O"
            else:
                symbol_p2 = "X"

            # Inicio do jogo
            turn = 1
            turn_limit = len(self.board.table) ** 2

            # Verificação de vitória ou empate
            while not self.winCondition() and not turn > turn_limit:

                # Decisão de quem começa jogando
                if self.matches % 2 == 0:
                    if turn % 2 == 0:
                        symbol = symbol_p2.upper()
                    else:
                        symbol = symbol_p1.upper()
                else:
                    if turn % 2 == 0:
                        symbol = symbol_p1.upper()
                    else:
                        symbol = symbol_p2.upper()

                # Cálculo do player atual
                player = (turn % 2) + (self.matches % 2) 
                if player == 0:
                    player = 2

                # Representação do turno e do jogador atual
                print(f"\nRodada {turn}",
                        f"\nJogador : {player} \n")
                self.showTable()

                # Validação da jogada 
                self.board.playMovement(symbol, self.askMovement())
                turn += 1
                self.showTable()

                # Verificação de vitória ou empate
                if self.winCondition():
                    print(f"O Jogador {player} ganhou!!\n")
                    if player == 1:
                        self.victories += 1
                    else:
                        self.loses += 1
                elif turn > turn_limit:
                    print("Empate!!\n")
                else:
                    continue

                # Interface de decisão do jogador
                decision = self.interface()
                if decision == 1:
                    self.board.resetTable()
                    turn = 1
                    self.matches += 1
                    print(f"\n     Placar\n" \
                        f"Partidas jogadas: {self.matches}\n" \
                        f"Jogador 1 | {self.victories} X {self.loses} | Jogador 2")
                    time.sleep(1.5)
                elif decision == 2:
                    self.resetGame()
                    return True
                else:
                    print("Programa Finalizado.")
                    return False