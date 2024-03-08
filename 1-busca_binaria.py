def buscaBinaria(lista, numeroEscolhido): #A busca binária consiste em procurar elementos ordenados sempre diminuindo o número de tentativas pela metade, por exemplo se são 50 números ele tenta o 25, caso número estivesse na primeira metade, a próxima tentativa seria o 13, pois ele sempre tenta o do meio, caso fosse a segunda metade seria o 37
    inicio = 0
    fim = len(lista) - 1
    contador = 0
    while True:
        meio = (inicio + fim) // 2 # faz o elemento central ser sempre inteiro
        tentativa = lista[meio]
        contador += 1
        if numeroEscolhido == tentativa:
            print(f'A posição do número é {meio} e precisou de {contador}')
            break
        if numeroEscolhido > tentativa:
            inicio = meio
        else:
            fim = meio

minha_lista = [1,2,3,4]
#Como são 4 elementos faz log₂4 = 2, então caso tente qualquer número será no máximo 2
buscaBinaria(minha_lista, 4)
#Como busca binária é O(Log n)