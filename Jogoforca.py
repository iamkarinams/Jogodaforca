import random #Importando random para utilizar a função 'choice'

def jogar_forca():
    palavras = [ #Escolhendo as palavras e suas dicas, você pode escolher o que quiser
        {'palavra': 'estrela', 'dica': 'Existem diversas que podem ser vistas durante a noite'},
        {'palavra': 'morango', 'dica': 'Fruta vermelha'},
        {'palavra': 'lapis', 'dica': 'Usado para escrever mas pode ser apagado'},
        {'palavra': 'aurum', 'dica': 'Ouro em latim'},
        {'palavra': 'batom', 'dica': 'Item de maquiagem utilizado na boca'}
    ] 
    palavra_escolhida = random.choice(palavras) # Seleciona uma palavra aleatória da lista
    palavra_secreta = palavra_escolhida['palavra'] # Seleciona a palavra 
    dica = palavra_escolhida['dica'] # Seleciona a dica da palavra 
    letras_descobertas = ['_'] * len(palavra_secreta) # Cria um _ para cada letra da palavra
    tentativas = 6 # Número máximo de tentativas
    letras_erradas = [] # Armazena as letras incorretas já utilizadas pelo usuário

    print('Jogo da Forca!')
    print('A palavra tem', len(palavra_secreta), 'letras.')
    print('Dica:', dica)

    while True: #Inicio do loop principal
        print('\nPalavra:', ' '.join(letras_descobertas)) # Exibe a palavra com as letras descobertas até o momento
        print('Letras erradas:', ', '.join(letras_erradas)) # Exibe as letras erradas já tentadas
        print('Tentativas restantes:', tentativas)

        letra = input('Digite uma letra: ').lower() # Recebe uma letra do usuário
        if len(letra) != 1: #Verifica se o usuário adicionou apenas uma letra
            print('Digite apenas uma letra por vez.')
            continue

        if letra in letras_erradas or letra in letras_descobertas:
            print('Você já tentou essa letra. Tente outra.')
            continue

        if letra in palavra_secreta:
            # A letra está na palavra secreta, atualiza as letras_descobertas
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_descobertas[i] = letra
        else:
            # A letra não está na palavra secreta
            letras_erradas.append(letra)
            tentativas -= 1

        if letras_descobertas == list(palavra_secreta): #Verifica se o usuário acertou todas as letras
            print('\nParabéns! Você adivinhou a palavra:', palavra_secreta)
            break

        if tentativas == 0:
            print('\nVocê perdeu! A palavra secreta era:', palavra_secreta)
            break

jogar_forca()
