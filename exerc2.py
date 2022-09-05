def instantEmail(nome, sobrenome):
    # cria uma string composta pela primeira letra da variavel 'nome'
    # a variavel sobrenome e a string '@algoritmos.com.br'.
    email = nome[0]+sobrenome+'@algoritmos.com.br'

    #retorna a variavel 'email' em minusculo
    return email.lower()


# Algoritmo principal.
# Dados de entrada.
name = input('Digite o seu primeiro nome: ')
surname = input('Digite o seu sobrenome: ')


# Junta as duas strings de entrada para criar um nome completo.
nomecompleto = name+' '+surname


# Chama a função instantEmail para criar um email usando os dados de entrada
# e depois escreve isso para o usuário.

print("Sra {}, seu email é {}".format(nomecompleto, instantEmail(name, surname+'17')))