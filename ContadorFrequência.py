# Contar quantas vezes uma palavra está aparecendo na lista

ListaPalavras = [
    "Jogo",
    "jogo",
    "jogo",
    "Mercado",
    "Carrinho",
    "Sacola",
    "Mercado"
]

PalavrasMin = [ListaMin.lower() for ListaMin in ListaPalavras] # transformar todas as palavras em minúsculo

def contador():
    cont = {} # vai guardar as palavras dentro de um objeto
    for palavras in PalavrasMin: # Loop que vai percorrer a lista e guardas as palavras em palavras
        if palavras in cont: # se a palavra estiver no contador
            cont[palavras] += 1 # vai somar um
        else: # se não
            cont[palavras] = 1 # adiciona uma unidade

    print(cont) # vai printar o contador (se fosse usado um return aqui, teríamos que declarar uma var com essa função, para o resultado ser mostrado no console)

contador() # como a função invoca o resultado com um print, e não com um return, é invoca-lá