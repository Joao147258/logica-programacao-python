# 3. Contador de Frequência Dada uma string, retorne um dicionário com a contagem de cada caractere presente nela. * **Foco:** Estrutura de dados Dicionário (Hash Map).

def contador_frequencia(palavra):
    # Dicionário vazio, para guardar a contagem
    contagem = {}

    for letra in palavra:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

texto = "Programacao"
resultado = contador_frequencia(texto)

print(resultado)

