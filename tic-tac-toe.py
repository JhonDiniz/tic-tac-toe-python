from playerXplayer import playerXplayer
from playerXAI import playerXAI

#---------------------------------------------------------------------------------------#
running = True
while running:
    game_choose = int(input("Informe o modo de jogo:\n" \
    "1 - Jogador X Jogador\n" \
    "2 - Jogador X IA\n"))
    if game_choose == 1:
        game = playerXplayer()
    else:
        difficulty_choose = int(input("Informe a dificuldade da IA:\n" \
            "1 - Fácil\n" \
            "2 - Médio\n" \
            "3 - Difícil\n"))
        game = playerXAI(difficulty_choose)
    if game.start():
        running = True
    else:
        running = False
    