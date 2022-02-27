import random

jogador = int(input('''Escolha uma opção para jogar: 

[0] Pedra
[1] Papel
[2] Tesoura

Digite a sua escolha: '''))

computador = random.randint(0,2)

if computador  == 0:
    print('O computador escolheu: Pedra')
    if jogador == 0:
        print('Temos um Empate')
    elif jogador == 1:
        print('Jogador perdeu')
    elif jogador == 2:
        print('O computador venceu!') 
    else:
        print('Operação inválida')

elif computador == 1:
    print('O computador escolheu: Papel')
    if jogador == 0:
        print('O computador perdeu')
    elif jogador == 1:
        print('Temos um empate')
    elif jogador == 2:
        print('O jogador venceu!')
    else:
        print('Operação inválida')

elif computador == 2:
    print('O computador ecolheu: Tesoura')
    if jogador == 0:
        print('O jogador venceu!!')
    elif jogador == 1:
        print('O computador venceu')
    elif jogador == 2:
        print('Temos um empate')
    else:
        print('Operação inválida')
else:
    ('Operação inválida')