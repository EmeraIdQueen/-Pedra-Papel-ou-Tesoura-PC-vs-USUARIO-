from random import choice

acoes_permitidas = ['pedra', 'papel', 'tesoura']
ponto_AI_1 = 0
ponto_Usuario = 0
n = 0 
#contador que controla o número de rodadas jogadas
ultimo_movimento_AI = ''
#evita que a IA repita o último movimento


#estilo das fontes
amarelo = '\033[33m'
original = '\033[0;0m'
negrito = '\033[1m'

#funções que executam o sistema de pontuação e mostram na tela os resultados
def ponto_ai_1():
    global ponto_AI_1
    print(amarelo + 'Ponto da AI 1\n'+ original)
    ponto_AI_1 += 1

def ponto_usuario():
    global ponto_Usuario
    print(amarelo + 'Ponto do Usuario\n'+ original)
    ponto_Usuario += 1



while n < 3:
    #3 rodadas melhor de 3
    movimento_AI_1 = str(choice(acoes_permitidas))
    while movimento_AI_1 == ultimo_movimento_AI:
        movimento_AI_1 = str(choice(acoes_permitidas))
        #isso aqui serve pra se o movimento que ela escolher for igual ela escolhe dnv

    ultimo_movimento_AI = movimento_AI_1
    movimento_Usuario = input('Escolha qual opcao (pedra, papel, tesoura): ')
    movimento_Usuario = movimento_Usuario.lower()
    #transforma em minusculo o comando do usuário

    while movimento_Usuario not in acoes_permitidas:
        movimento_Usuario = input('Escolha qual opcao (pedra, papel, tesoura): ')
        movimento_Usuario = movimento_Usuario.lower()
        #isso serve pra caso o usuário não escrever um movimentoi válido

       
    print(f'AI escolheu {movimento_AI_1}\nUsuario escolheu {movimento_Usuario}')
    if movimento_AI_1 == movimento_Usuario:
        print(amarelo + 'Empatou\n' + original)

    #resultado programado dos jogos para a AI
    elif movimento_AI_1 == 'pedra' and movimento_Usuario == 'tesoura':
        ponto_ai_1()
    elif movimento_AI_1 == 'tesoura' and movimento_Usuario == 'papel':
        ponto_ai_1()
    elif movimento_AI_1 == 'papel' and movimento_Usuario == 'pedra':
        ponto_ai_1()
    
    #resultado programado dos jogos para o usuário
    elif movimento_Usuario == 'pedra' and movimento_AI_1 == 'tesoura':
        ponto_usuario()
    elif movimento_Usuario == 'tesoura' and movimento_AI_1 == 'papel':
        ponto_usuario()
    elif movimento_Usuario == 'papel' and movimento_AI_1 == 'pedra':
        ponto_usuario()

    n += 1
    #adiciona mais 1 ao contador para chegar a 3 e encerrar a partida

#Isso serve pra mostrar o resultado final do jogo
print(negrito + amarelo + 'Pontuacao final' + original)
print(f'AI fez {ponto_AI_1}\nUsuario fez {ponto_Usuario}')