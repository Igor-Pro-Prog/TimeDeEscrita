#jogo de velocidade de digitação

from random import choice
from string import ascii_lowercase
from time import time

#cria as funções para o jogo
def get_random_string():
    return ''.join(choice(ascii_lowercase) for i in range(5))

def get_user_input():
    return input('Type the string: ')

def print_time(t):
    print('Your time: %.2f seconds' % t)

def main():
    #cria o loop do jogo
    while True:
        #cria a string aleatória
        random_string = get_random_string()
        print('Random string: %s' % random_string)
        #pega o tempo inicial
        start = time()
        #pega a entrada do usuário
        user_input = get_user_input()
        #pega o tempo final
        end = time()
        #calcula o tempo
        elapsed = end - start
        #imprime o tempo
        print_time(elapsed)
        #verifica se o usuário acertou
        if user_input == random_string:
            print('BOA!')
        else:
            print('ERRADO!')
        #pergunta se o usuário quer jogar novamente
        play_again = input('Deseja Jogar Novamente? [Y/n] ')
        if play_again.lower() != 'y':
            break

if __name__ == '__main__':
    main()
