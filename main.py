from time import sleep # Biblioteca responsável para dar algum tempo no projeto
import os # Biblioteca responsável por limpar o terminal no projeto

def logo():
    '''
    Função responsável por imprimir a logotipo.
    '''

    os.system('cls') # Comando para limpar terminal
    print('\n'*15)
    print('''
                                                                 \33[1;36m     _    _         _ \33[1;34m ______             \33[1;31m/|\33[0;30m
                                                                 \33[1;36m    | |  | |       (_)\33[1;34m|  ____|           \33[1;31m(_)\33[0;30m
                                                                 \33[1;36m    | |  | | _ __   _ \33[1;34m| |__   __ _   ___  _  ___   __ _
                                                                 \33[1;36m    | |  | || '_ \ | |\33[1;34m|  __| / _` | / __|| |/ __| / _` |
                                                                 \33[1;36m    | |__| || | | || |\33[1;34m| |   | (_| || (__ | |\__ \| (_| |
                                                                 \33[1;36m     \____/ |_| |_||_|\33[1;34m|_|    \__,_| \___||_||___/ \__,_|
    \33[0m''')

def tela_inicial():
    '''
    Função responsável por imprimir a tela inicial.
    '''

    logo()
    print()
    sleep(0.5)

    print('Bem-vindo ao sistema de Ouvidoria da Unifacisa'.center(190))
    print()
    print('1 - LOGIN'.center(190))
    print('2 - CADASTRO'.center(190))
    print('3 - SAIR'.center(190))

def tela_cadastro():
    '''
    Função responsável por imprimir a tela de cadastro, onde será armazenado
    todas as informações cadastradas na lista 'usuarios'.
    '''

    logo()
    print()
    sleep(0.5)

    print('Criar uma conta'.center(190))
    print()

    while True:  # Comando para permitir que seja digitado apenas letras sem espaços.
        nome = input('Digite seu primeiro nome: ').capitalize()
        if nome.isalpha() and ' ' not in nome:
            break
        else:
            print('\33[31mErro...\33[0m', end='')

    while True: # Comando para permitir que seja digitado um e-mail com formatação correta usando '@' e '.'.
        validacao_local = 0
        email = input('Digite seu e-mail: ')
        if '@' in email and '.' in email[email.index('@'):]:
            for usuario in usuarios:
                if email == usuario['email']:
                    print('\33[31mE-mail já cadastrado. Tente novamente.\33[0m')
                    validacao_local = 1
            if validacao_local == 0:
                break
        else:
            print('\33[31mErro, insira um e-mail válido. \33[4mexemplo@exemplo.com\33[0m')

    while True:  # Comando para não permitir que seja digitado espaços.
        senha = input('Digite uma senha: ')
        if ' ' in senha:
            print('\33[31mTente novamente, a senha não pode conter espaços...\33[0m', end='')
        else:
            break

    print('\33[32m')
    print('Cadastro efetuado com sucesso.'.center(190))
    print('\33[0m')
    sleep(2)

    usuarios.append({ # Comando para armazenar um dicionário com as chaves e valores dentro da lista 'usuarios' usando a função append.
        'nome': nome,
        'email': email,
        'senha': senha,
        'reclamacoes': [],
        'sugestoes': [],
        'elogios': []
    })

def tela_login():
    '''
    Função responsável por imprimir a tela de login, onde será solicitado
    todas as informações cadastradas na lista 'usuarios'.
    '''

    global validacao, usuario_atual # Comando para que a função tela_login use a variável 'validacao' global, caso contrário iria ser gerado uma variável local com o mesmo nome.

    logo()
    print()
    sleep(0.5)

    print('Fazer login'.center(190))
    print()

    while True:
        loginEmail = input('Digite seu e-mail: ')
        loginSenha = input('Digite sua senha: ')

        usuario_encontrado = False # Variável para armazenar a informação se o usuario será encontrado ou não dentro da lista 'usuarios'.

        for conta in usuarios:  # Localizar e-mail e senha dentro da lista 'usuarios'
            if conta['email'] == loginEmail:
                if conta['senha'] == loginSenha:
                    usuario_encontrado = True
                    validacao = 1
                    break

        if usuario_encontrado == True: # Usuário foi encontrado na lista 'usuarios' e poderá fazer login.
            print('\33[32m')
            print('Login efetuado com sucesso.'.center(190))
            print('\33[0m')
            for index, usuario in enumerate(usuarios):
                if usuario['email'] == loginEmail:
                    usuario_atual = index
            sleep(2)
            break

        if usuario_encontrado == False: # Usuário não foi encontrado na lista 'usuarios' e terá que realizar uma nova tentativa.
            print('\33[31m')
            print('E-mail ou senha incorretos.'.center(190))
            print('\33[0m')
            sleep(2)
            break

def menu():
    '''
    Função responsável por imprimir a tela de menu, onde poderá ser selecionado
    qual tipo de solicitação deseja fazer.
    '''

    global usuarios, usuario_atual

    while True:

        logo()
        print()
        sleep(0.5)

        print('Bem-Vindo {}!'.format(usuarios[usuario_atual]['nome']).center(190))
        print()

        print('O que deseja fazer?'.center(190))
        print()
        print('1 - CRIAR'.center(190))
        print('2 - LISTAR'.center(190))
        print('3 - ATUALIZAR'.center(190))
        print('4 - DELETAR'.center(190))
        print('5 - VOLTAR'.center(190))

        opcao = input()

        if opcao == '1':
            tela_Criar()
        elif opcao == '2':
            tela_Listar()
        elif opcao == '3':
            tela_Atualizar()
        elif opcao == '4':
            tela_Deletar()
        elif opcao == '5':
            print()
            print('Voltando...'.center(190))
            sleep(2)
            break
        else:
            print('\33[31m')
            print('Opção inválida.'.center(190))
            print('\33[0m')
            sleep(2)

def tela_Criar():
    '''
    Função responsável por imprimir a tela de criação, onde poderá registrar alguma reclamação, sugestão ou elogio.
    '''

    global protocolo

    while True:

        logo()
        print()
        sleep(0.5)

        print('Qual o tipo do registro?'.center(190))
        print()
        print('1 - REGISTRAR RECLAMAÇÃO'.center(190))
        print('2 - REGISTRAR ELOGIO'.center(190))
        print('3 - REGISTRAR SUGESTÃO'.center(190))
        print('4 - VOLTAR PARA O MENU'.center(190))

        opcao = input()

        if opcao == '1':
            protocolo += 1
            print('Sua reclamação será registrada no protocolo {}'.format(protocolo))
            titulo = input('Escreva um título para sua reclamação: ')
            texto = input('Escreva a reclamação: ')

            usuarios[usuario_atual]['reclamacoes'].append({ # Comando para armazenar uma reclamação
                'protocolo': str(protocolo),
                'titulo': titulo,
                'texto': texto
            })
            print('\33[32m')
            print('Reclamação cadastrada com sucesso. Voltando para o menu.'.center(190))
            print('\33[0m')
            sleep(3)
            break

        elif opcao == '2':
            protocolo += 1
            print('Seu elogio será registrado no protocolo {}'.format(protocolo))
            titulo = input('Digite um título para seu elogio: ')
            texto = input('Digite seu elogio: ')

            usuarios[usuario_atual]['elogios'].append({ # Comando para armazenar um elogio
                'protocolo': str(protocolo),
                'titulo': titulo,
                'texto': texto
            })
            print('\33[32m')
            print('Elogio cadastrado com sucesso. Voltando para o menu'.center(190))
            print('\33[0m')
            sleep(3)
            break

        elif opcao == '3':
            protocolo += 1
            print('Sua sugestão será registrada no protocolo {}'.format(protocolo))
            titulo = input('Escreva um titulo para sua sugestão: ')
            texto = input('Escreva sua sugestão: ')

            usuarios[usuario_atual]['sugestoes'].append({ # Comando para armazenar uma sugestão
                'protocolo': str(protocolo),
                'titulo': titulo,
                'texto': texto
            })
            print('\33[32m')
            print('Sugestão cadastrada com sucesso. Voltando para o menu'.center(190))
            print('\33[0m')
            sleep(3)
            break

        elif opcao == '4':
            print()
            print('Voltando para o menu...'.center(190))
            sleep(2)
            break
        
        else:
            print('\33[31m')
            print('Opção inválida.'.center(190))
            print('\33[0m')
            sleep(2)

def tela_Listar():
    '''
    Função responsável por imprimir a tela de listagem, onde poderá visualizar todos os registros.
    '''

    global protocolo, usuario_atual

    while True:

        logo()
        print()
        sleep(0.5)

        print('O que deseja listar?'.center(190))
        print()
        print('1 - LISTAR RECLAMAÇÃO'.center(190))
        print('2 - LISTAR ELOGIO'.center(190))
        print('3 - LISTAR SUGESTÃO'.center(190))
        print('4 - VOLTAR PARA O MENU'.center(190))

        opcao = input()

        if opcao == '1':
            tipo = 'reclamacoes'
            genero = ['AS', 'SUAS']
        elif opcao == '2':
            tipo = 'elogios'
            genero = ['OS', 'SEUS']
        elif opcao == '3':
            tipo = 'sugestoes'
            genero = ['AS', 'SUAS']
        elif opcao == '4':
            print()
            print('Voltando para o menu...'.center(190))
            sleep(2)
            break
        else:
            print('\33[31m')
            print('Opção inválida.'.center(190))
            print('\33[0m')
            sleep(2)
            continue

        while True:
            sleep(0.5)
            separador()
            print('1 - LISTAR TOD{} {} {}'.format(genero[0], genero[0], tipo.upper()).center(190))
            print('2 - LISTAR {} {}'.format(genero[1], tipo.upper()).center(190))
            print('3 - LISTAR POR PROTOCOLO'.center(190))
            print('4 - VOLTAR'.center(190))

            opcao = input()
            sleep(1)

            if opcao == '1':
                separador()
                print('TOD{} {} {}'.format(
                    genero[0], genero[0], tipo.upper()).center(190))
                for user in usuarios: # Comando para listar todos os registros dentro de cada usuário.
                    for register in user[tipo]:
                        separador()
                        print('\33[1mProtocolo: ', register['protocolo'])
                        print('Título: ', register['titulo'])
                        print(register['texto'],'\33[0m')
                if not usuarios[usuario_atual][tipo]:
                    print()
                    print('Não há registros seus de {}.'.format(tipo))

            elif opcao == '2':
                separador()
                print('TOD{} {} {}'.format(
                    genero[0], genero[1], tipo.upper()).center(190))
                for register in usuarios[usuario_atual][tipo]: # Comando para listar todos os registros dentro de um específico usuário.
                    separador()
                    print('\33[1mProtocolo: ', register['protocolo'])
                    print('Título: ', register['titulo'])
                    print('{}\33[0m'.format(register['texto']))
                if not usuarios[usuario_atual][tipo]:
                    print()
                    print('Não há registros seus de {}.'.format(tipo))

            elif opcao == '3':
                while True:
                    localizacao = 0
                    separador()
                    protocolo_localizar = input(('Digite o protocolo: '))
                    print()
                    print('Localizando...')
                    sleep(2)
                    for user in usuarios: # Comando para listar o registro de acordo com o protocolo.
                        for register in user[tipo]:
                            if protocolo_localizar == register['protocolo']:
                                separador()
                                print('\33[1mProtocolo: {}'.format(register['protocolo']))
                                print('Título: {}'.format(register['titulo']))
                                print('{}\33[0m'.format(register['texto']))
                                localizacao = 1
                                break

                    if localizacao == 0:
                        separador()
                        print('\33[31m')
                        print('Protocolo não localizado.'.center(190))
                        print('\33[0m')
                        sleep(2)

                        while True:
                            print('Deseja tentar novamente? [S/N]'.center(190))
                            confirmacao = input().upper()
                            if confirmacao == 'S':
                                break
                            elif confirmacao == 'N':
                                break
                            else:
                                print('Opção inválida... Tente novamente')

                    if localizacao == 1 or confirmacao == 'N':
                        break

            elif opcao == '4':
                print()
                print('Voltando...'.center(190))
                sleep(2)
                break

            else:
                print('\33[31m')
                print('Opção inválida.'.center(190))
                print('\33[0m')
                sleep(2)


            print()
            opcao = input('0 - VOLTAR ')

def tela_Atualizar():
    '''
    Função responsável por imprimir a tela de atualização, onde poderá atualizar algum registro.
    '''
    
    global protocolo, usuario_atual

    while True:

        logo()
        print()
        sleep(0.5)

        print('O que deseja atualizar?'.center(190))
        print()
        print('1 - ATUALIZAR RECLAMAÇÃO'.center(190))
        print('2 - ATUALIZAR ELOGIO'.center(190))
        print('3 - ATUALIZAR SUGESTÃO'.center(190))
        print('4 - VOLTAR PARA O MENU'.center(190))

        opcao = input()

        if opcao == '1':
            tipo = 'reclamacoes'
        elif opcao == '2':
            tipo = 'elogios'
        elif opcao == '3':
            tipo = 'sugestoes'
        elif opcao == '4':
            print()
            print('Voltando para o menu...'.center(190))
            sleep(2)
            break
        else:
            print('\33[31m')
            print('Opção inválida.'.center(190))
            print('\33[0m')
            sleep(2)
            continue

        while True:
            separador()
            sleep(0.5)
            
            if not usuarios[usuario_atual][tipo]:
                print('Não há registros de {}.'.format(tipo).center(190))
                sleep(2)
                break

            print('Quais {} deseja atualizar?'.format(tipo).center(190))
            for cont, register in enumerate(usuarios[usuario_atual][tipo]): # Comando para enumerar todos os registros para selecionar e possibilitar a atualização.
                separador()
                print('#{}'.format(cont))
                print('\33[1mProtocolo: ', register['protocolo'])
                print('Título: ', register['titulo'])
                print(register['texto'],'\33[0m')
            separador()
            opcao = int(input('Digite o número: '))
            separador()
            if opcao < len(usuarios[usuario_atual][tipo]):
                print('\33[1mProtocolo: ',
                      usuarios[usuario_atual][tipo][opcao]['protocolo'])
                usuarios[usuario_atual][tipo][opcao]['titulo'] = input(
                    'Digite o novo título: ')
                usuarios[usuario_atual][tipo][opcao]['texto'] = input(
                    'Digite o novo texto: ')
                print('\33[32m')
                print('Atualizado com sucesso.'.center(190))
                print('\33[0m')
                sleep(2)
                break

            else:
                sleep(1)
                print('\33[31m')
                print('Opção inválida.'.center(190))
                print('\33[0m')
                sleep(2)

def tela_Deletar():
    '''
    Função responsável por imprimir a tela de deletar, onde poderá remover algum registro.
    '''

    global protocolo, usuario_atual

    while True:

        logo()
        print()
        sleep(0.5)

        print('O que deseja deletar?'.center(190))
        print()
        print('1 - DELETAR RECLAMAÇÃO'.center(190))
        print('2 - DELETAR ELOGIO'.center(190))
        print('3 - DELETAR SUGESTÃO'.center(190))
        print('4 - VOLTAR PARA O MENU'.center(190))

        opcao = input()

        if opcao == '1':
            tipo = 'reclamacoes'
            genero = ['AS', 'SUAS']
        elif opcao == '2':
            tipo = 'elogios'
            genero = ['OS', 'SEUS']
        elif opcao == '3':
            tipo = 'sugestoes'
            genero = ['AS', 'SUAS']
        elif opcao == '4':
            print()
            print('Voltando para o menu...'.center(190))
            sleep(2)
            break
        else:
            print('\33[31m')
            print('Opção inválida.'.center(190))
            print('\33[0m')
            sleep(2)
            continue

        while True:
            separador()
            sleep(0.5)
            if not usuarios[usuario_atual][tipo]:
                print('Não há registros de {}.'.format(tipo).center(190))
                sleep(2)
                break
            print('Quais {} deseja deletar?'.format(tipo).center(190))
            for cont, register in enumerate(usuarios[usuario_atual][tipo]): # Comando para enumerar todos os registros para selecionar e possibilitar a remoção.
                separador()
                print('#{}'.format(cont))
                print('\33[1mProtocolo: ', register['protocolo'])
                print('Título: ', register['titulo'])
                print(register['texto'],'\33[0m')
            separador()
            print('#{}'.format(len(usuarios[usuario_atual][tipo]))) # Comando para possibilitar a remoção de todos os registros.
            print('TOD{} {} {}'.format(genero[0], genero[0], tipo.upper()))
            separador()
            opcao = int(input('Digite o número: '))
            separador()
            if opcao <= len(usuarios[usuario_atual][tipo]):
                if opcao == len(usuarios[usuario_atual][tipo]):
                    while True:
                        confirmacao = input('Tem certeza que deseja deletar tod{} {} {}? [S/N]'.format(
                            genero[0], genero[0], tipo).upper()).upper()
                        if confirmacao == 'S':
                            usuarios[usuario_atual][tipo] = []
                            print('\33[32m')
                            print('Deletado com sucesso.'.center(190))
                            print('\33[0m')
                            sleep(2)
                            break
                        elif confirmacao == 'N':
                            print('Operação cancelada.'.center(190))
                            sleep(2)
                            break
                        else:
                            sleep(1)
                            print('\33[31m')
                            print('Opção inválida.'.center(190))
                            print('\33[0m')
                            sleep(2)
                else:
                    usuarios[usuario_atual][tipo].pop(opcao)
                    print('\33[32m')
                    print('Deletado com sucesso.'.center(190))
                    print('\33[0m')
            else:
                sleep(1)
                print('\33[31m')
                print('Número não localizado.'.center(190))
                print('\33[0m')
                sleep(2)

            print()
            opcao = input('0 - VOLTAR ')
            break

def separador():
    '''
    Função responsável por imprimir espaços e traços afim de manter a organização do sistema.
    '''

    print()
    print("-="*95)
    print()

'''Usuarios = [
    {
        'nome' = 'Nome', 'email' = 'Email', 'senha' = 'Senha',

        'reclamacoes' = [{
            'protocolo' = 'Protocolo', 'titulo' = 'Titulo', 'texto' = 'Texto'
        }],

        'sugestoes' = [{
            'protocolo' = 'Protocolo', 'titulo' = 'Titulo', 'texto' = 'Texto'
        }],
        
        'elogios' = [{'protocolo' = 'Protocolo', 'titulo' = 'Titulo', 'texto' = 'Texto'
        }]
    }'''


# Programa principal

usuarios = []  # Todos os dados armazenados

usuarios.append({  # inserir usuário admin
    'nome': 'Admin',
    'email': 'test@admin.com',
    'senha': 'admin',
    'reclamacoes': [
        {
            'protocolo': '21054091',
            'titulo': 'Atraso na publicação das notas',
            'texto': 'As notas das provas estão sendo divulgadas com muito atraso, prejudicando o planejamento dos alunos.'
        },
        {
            'protocolo': '21054092',
            'titulo': 'Falta de manutenção nos laboratórios',
            'texto': 'Os equipamentos dos laboratórios de informática estão desatualizados e com defeitos, dificultando as aulas práticas.'
        },
        {
            'protocolo': '21054093',
            'titulo': 'Biblioteca com poucos exemplares',
            'texto': 'A biblioteca tem poucos exemplares dos livros recomendados pelos professores, o que dificulta os estudos.'
        }
    ],
    'sugestoes': [
        {
            'protocolo': '21054094',
            'titulo': 'Mais palestras extracurriculares',
            'texto': 'Seria interessante promover mais palestras com profissionais da área para complementar o aprendizado dos alunos.'
        },
        {
            'protocolo': '21054095',
            'titulo': 'Aumento do horário de funcionamento da biblioteca',
            'texto': 'Sugiro aumentar o horário de funcionamento da biblioteca, especialmente durante os períodos de prova.'
        },
        {
            'protocolo': '21054096',
            'titulo': 'Melhoria no sistema de agendamento de aulas práticas',
            'texto': 'O sistema de agendamento de aulas práticas poderia ser melhorado para evitar conflitos e sobreposições de horários.'
        }
    ],
    'elogios': [
        {
            'protocolo': '21054097',
            'titulo': 'Ótima infraestrutura',
            'texto': 'A infraestrutura da faculdade é excelente, proporcionando um ambiente adequado para os estudos e atividades.'
        },
        {
            'protocolo': '21054098',
            'titulo': 'Professores qualificados',
            'texto': 'Os professores são altamente qualificados e comprometidos com o ensino, o que tem sido essencial para a minha formação.'
        },
        {
            'protocolo': '21054099',
            'titulo': 'Atendimento da secretaria',
            'texto': 'O atendimento da secretaria é rápido e eficiente, sempre solucionando os problemas dos alunos com agilidade.'
        }
    ]
})

protocolo = 21054099

while True:
    # Variável que permite identificar qual o usuário que está logado.
    usuario_atual = None
    opcao = ''
    validacao = 0
    tela_inicial()
    opcao = input()
    if opcao == '1':
        tela_login()
        if validacao == 1:
            menu()

    elif opcao == '2':
        tela_cadastro()

    elif opcao == '3':
        logo()
        separador()
        print('Encerrando o programa...'.center(190))
        separador()
        break

    else:
        print('\33[31m')
        print('Opção inválida.'.center(190))
        print('\33[0m')
        sleep(2)
