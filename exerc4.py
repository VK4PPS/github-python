# importações
from operator import itemgetter

# Lista com dicionario onde as informações são armazenadas
estoque = [{'codigo': 0, 'estoque': 0, 'minimo': 0}]

while True:
    print('=-=-= Novo Cadastro no Estoque =-=-=')

    # Input usado para encerrar ou continuar o programa, também atribui o valor que será
    # cadastrado como 'codigo' 
    x = input('Digite o código: ')

    # Caso o usuario escolha continuar o programa
    if x != '0':

        

        
        code = int(x)
        # Dados de entrada.
        suply = input('Digite o estoque: ')
        minimum = input('Digite o minimo: ')

        # Insere os dados de entrada em formato de dicionario na lista 'estoque'
        estoque.append({'codigo': code, 'estoque': suply, 'minimo': minimum})

    # Caso o usuario escolha encerrar o programa
    elif x == '0':
        print('Encerrando programa')

        # Atribui a variavel 'estoqueSorted' a lista 'estoque' organizada em ordem crescente utilizando
        # a chave 'codigo' como base
        estoqueSorted = sorted(estoque, key=itemgetter('codigo'))

        # Itera o 'estoqueSorted' separando cada item em uma linha
        x = 1
        print('codigo | Estoque | Minimo')
        for i in range(len(estoqueSorted)-1):
            print('{}       {}        {}       '.format(estoqueSorted[x]['codigo'], estoqueSorted[x]['estoque'], estoqueSorted[x]['minimo']))
            x += 1

        
        # encerra o programa.
        break

    # Caso o usuario digite algo não previsto
    else:
        print('Comando Inválido \n')
