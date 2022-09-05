# importação
import random

# Cria a lista.
listaDoSorteio = []

while True:
    print('Digite 1 para cadastrar participantes \nDigite 2 para fazer o sorteio')
    # Input usado para encerrar ou continuar o programa.
    x = input()

    # Caso o usuario escolha continuar o programa.
    if x == '1':
        # Dados de Entrada.
        nome = input('Nome do Participante: ')
        valor = float(input('Valor Doado: '))
        # Descobre quantas vezes o nome deve ser
        # inserido na lista.
        reps =  int(valor/10)

        # Insere o valor da variavel 'nome' na lista x vezes.
        for x in range(reps):
            listaDoSorteio.append(nome)

    # Caso o usuario escolha encerrar o programa.
    elif x == '2':
        break

    # Caso o usuario digite algo não previsto.
    else:
        print('Comando Desconhecido')

#   Escreve a lista.
print('{}\n'.format(listaDoSorteio))

#   Embaralha a lista.
random.shuffle(listaDoSorteio)

#   Escolhe um nome aleatório da lista e escreve.
print('O ganhador é: {}'.format(random.choice(listaDoSorteio)))


