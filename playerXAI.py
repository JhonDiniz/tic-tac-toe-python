import time

from terminal import terminal

class playerXAI(terminal):
    def __init__(self, difficulty):
        super().__init__()
        self.difficulty = difficulty

    def start(self):
        self.instructions()
        while self.game_on:

            # Escolha do X ou O do jogador
            while True:
                try:   
                    symbol_p = input("\nInforme o símbolo do Jogador (X / O)\n")
                    if symbol_p.upper() != "X" and symbol_p.upper() != "O":
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print("\nSímbolo inválido, informe X ou O!\n")
            if symbol_p.upper() == "X":
                symbol_AI = "O"
            else:
                symbol_AI = "X"

            # Inicio do jogo
            turn = 1
            turn_limit = len(self.board.table) ** 2 

            # Verificação de vitória ou empate
            while not self.winCondition() and not turn > turn_limit:
                    
                    # Decisão de quem começa jogando
                    if self.matches % 2 == 0:
                        if turn % 2 == 1:
                            symbol = symbol_p.upper()
                        else:
                            symbol = symbol_AI
                    else:
                        if turn % 2 == 0:
                            symbol = symbol_p.upper()
                        else:
                            symbol = symbol_AI
                    player_turn = (turn + self.matches) % 2

                    #Cálculo de quem está jogando
                    if player_turn:
                        whose_turn = "o Jogador"
                    else:
                        whose_turn = "a IA"

                    # Representação do turno e do jogador atual
                    print(f"\n{turn}° Rodada",
                          f"\nTurno d{whose_turn}")

                    # Validação da jogada do player
                    if player_turn:
                        pos = self.askMovement()
                    # Escolha da jogada da IA com base na dificuldade
                    else:
                        if self.difficulty == 1:
                            pos = self.randomMovement()
                        elif self.difficulty == 2:
                            continue #desenvolvendo
                        else:
                            continue #desenvolvendo
                        self.thinking()

                    # Execução da Jogada
                    self.board.playMovement(symbol, pos)
                    turn += 1
                    self.showTable()

                    # Verificação de vitória ou empate
                    if self.winCondition():
                        print(f"{whose_turn} ganhou!!\n")
                        if whose_turn == "o Jogador":
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
                        self.matches += 1
                        turn = 1
                        print(f"\nPartidas jogadas: {self.matches}\n" \
                        f"Jogador | {self.victories} X {self.loses} | IA")
                        time.sleep(1.5)
                    elif decision == 2:
                        self.resetGame()
                        return True
                    else:
                        print("Programa Finalizado.")
                        return False