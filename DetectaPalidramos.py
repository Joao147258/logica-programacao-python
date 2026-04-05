# Criar um Script que detécta se uma palavra é palíndroma

palavra = "radar"
palavra_inv = palavra[::-1]

if palavra_inv == palavra:
    print("palíndroma")
else:
    print("Não palíndroma")


def Verifica_palavras(palavra):
    palavra_formatada = palavra.lower().strip() #converte a palavra em tudo mínusculo e tira os espaços
    palavra_invertida = palavra_formatada[::-1]  #inverte a palavra

    # Bloco da analise
    if palavra_invertida == palavra_formatada:
        return "Palíndroma detectada" # Como é uma função que eu vou invocar com variável para printar o resultado, usei o return ao invez do print
    else:
        return "Não palíndroma"

entrada_user = input("Digite uma palavra \n")

resultado = Verifica_palavras(entrada_user)
print(resultado)