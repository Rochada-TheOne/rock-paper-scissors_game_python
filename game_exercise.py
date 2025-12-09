import random, sys
print('ROCK, PAPER, SCISSORS')

# Essas variáveis registram a quantidade de vitórias, derrotas e empates
wins = 0
losses = 0
ties = 0

while True:  # Loop principal do jogo
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # Loop da entrada do jogador
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('>')
        if player_move == 'q':
            sys.exit()  # Encerra o programa
        if player_move in ('r', 'p', 's'): # Usando 'in' para simplificar a verificação
            break  # Interrompe o loop da entrada do jogador
        print('Type one of r, p, s, or q.')

    # Exibe a opção que o jogador escolheu
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Exibe a opção que o computador escolheu
    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Exibe e registra a vitória, derrota ou empate
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r': # **Linha Corrigida/Adicionada**
        print('You lose!')
        losses = losses + 1