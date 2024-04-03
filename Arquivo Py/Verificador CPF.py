while True:
    print('Bem vindo ao Verificador CPF, o programa irá adivinhar os dois números verificadores do seu CPF. Ou seja, os dois números depois do hífen.')
    entrada = input('Digite o seu CPF sem os pontos e SEM DIGITAR OS NÚMEROS DEPOIS DO HÍFEN: ')
    CPF = list(map(int,entrada))
    num1 = (CPF[0] * 10 + CPF[1] * 9 + CPF[2] * 8 + CPF[3] * 7 + CPF[4] * 6 + CPF[5] * 5 + CPF[6] * 4 + CPF[7] * 3 + CPF[8] * 2) % 11

    resultado1 = 11 - num1

    if resultado1 >= 10:
        resultado1 = 0

    CPF.append(resultado1)

    num2 = (CPF[0] * 11 + CPF[1] * 10 + CPF[2] * 9 + CPF[3] * 8 + CPF[4] * 7 + CPF[5] * 6 + CPF[6] * 5 + CPF[7] * 4 + CPF[8] * 3 + CPF[9] * 2) % 11
    
    resultado2 = 11 - num2
    
    if resultado2 >= 10:
        resultado2 = 0

    CPF.append(resultado2)

    print(f'O sistema verificou seu CPF. O resultado foi: {CPF[0]}{CPF[1]}{CPF[2]}.{CPF[3]}{CPF[4]}{CPF[5]}.{CPF[6]}{CPF[7]}{CPF[8]}-{CPF[9]}{CPF[10]}.')
    
    if CPF[8] == 0:
        print('O sistema também calculou que seu CPF é do Rio Grande do Sul.')

    elif CPF[8] == 1:
        print('O sistema também calculou que seu CPF é do Distrito Federal, ou de Goiás, ou do Mato Grosso do Sul, ou de Tocantins.')

    elif CPF[8] == 2:
        print('O sistema também calculou que seu CPF é do Pará, ou do Amazonas, ou do Acre, ou do Amapá, ou de Rondônia, ou de Roraima.')

    elif CPF[8] == 3:
        print('O sistema também calculou que seu CPF é de Ceará, ou do Maranhão, ou do Piauí.')

    elif CPF[8] == 4:
        print('O sistema também calculou que seu CPF é de Pernambuco, ou do Rio Grande Do Norte, ou da Paraíba, ou de Alagoas.')

    elif CPF[8] == 5:
        print('O sistema também calculou que seu CPF é da Bahia ou de Sergipe.')

    elif CPF[8] == 6:
        print('O sistema também calculou que seu CPF é de Minas Gerais.')

    elif CPF[8] == 7:
        print('O sistema também calculou que seu CPF é do Rio de Janeiro ou do Espírito Santo.')

    elif CPF[8] == 8:
        print('O sistema também calculou que seu CPF é de São Paulo.')

    elif CPF[8] == 9:
        print('O sistema também calculou que seu CPF é do Paraná ou de Santa Catarina.')
    
    pergunta = input('Deseja testar outro CPF? Digite Y para sim e N para não, em letras maiúsculas: ')
    if pergunta == 'Y':
        continue
    elif pergunta == 'N':
        print('Obrigado por usar meu programa!')
        break

input('Pressione qualquer tecla para fechar: ')