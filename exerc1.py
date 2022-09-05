while True:
    # Input usado para encerrar ou continuar o programa.
    x = str(input('Deseja Cadastrar um Aluno e nota?[S/N]'))

    # Caso o usuario escolha continuar o programa.
    if x.upper() == 'S':

        # Dados de entrada.
        nome = input('Digite o nome do aluno: ')
        nota = float(input('Digite a nota do aluno: '))

        # Confere a nota do aluno e atribui uma string de acordo com a nota
        # a varivel 'conceito'.
        if nota <= 2.9:
            conceito = 'E'
        elif nota <= 4.9:
            conceito = 'D'
        elif nota <= 6.9:
            conceito = 'C'
        elif nota <= 8.9:
            conceito = 'B'
        elif nota <= 10:
            conceito = 'A'
        else:
            print('A nota Digitada é inválida, Digite uma nota entre 0 e 10')    
            continue

    # Apresente as informações finais. Nome, nota e conceito
        print('Nome do aluno: {}'.format(nome))
        print('Nota final: {}'.format(nota))    
        print('O aluno {} tirou nota {} e se enquadra no conceito {}'.format(nome, nota, conceito))

    # Caso o usuario escolha encerrar o programa
    elif x.upper() == 'N':
        # encerra o programa.
        print('Programa Encerrado')
        break

    # Caso o usuario digite algo não previsto
    else:
        # Uma mensagem é apresentada e o código reitera.
        print('Comando inválido')

