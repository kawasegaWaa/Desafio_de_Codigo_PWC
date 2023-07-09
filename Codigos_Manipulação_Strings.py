# 1º
print("1° Invertendo a ordem das palavras nas frases.")
def reverter_ordem_palavras(frase):
    palavras = frase.split()  # Divide a frase em uma lista de palavras
    palavras_revertidas = palavras[::-1]  # Inverte a ordem das palavras
    frase_revertida = ' '.join(palavras_revertidas)  # Junta as palavras em uma frase novamente
    return frase_revertida

frase_original = input("Digite uma frase: ") # Solicitar ao usuário que digite uma frase

frase_revertida = reverter_ordem_palavras(frase_original) # Chamar a função para reverter a ordem das palavras
print("Frase revertida:", frase_revertida)

# 2°
print("2° Removendo todos os caracteres duplicados.")
def remover_caracteres_duplicados(string):
    caracteres_unicos = []
    for caractere in string:
        if caractere not in caracteres_unicos:
            caracteres_unicos.append(caractere)
    string_sem_duplicados = ''.join(caracteres_unicos)
    return string_sem_duplicados

# Solicitar ao usuário que digite uma string
string_original = input("Digite uma string: ")

# Chamar a função para remover os caracteres duplicados
string_sem_duplicados = remover_caracteres_duplicados(string_original)
print("String sem caracteres duplicados:", string_sem_duplicados)



# 3°
print("3° Encontrando a substring palindroma mais longa na string.")
def encontrar_substring_palindroma(string):
    tamanho = len(string)
    maior_palindromo = ""

    for i in range(tamanho):  # Verificar todas as substrings possíveis
        for j in range(i, tamanho):
            substring = string[i:j+1]

            if substring == substring[::-1] and len(substring) > len(maior_palindromo): # Verificar se a substring é palindrômica
                maior_palindromo = substring
    return maior_palindromo

string_original = input("Digite uma string: ") # Solicitar ao usuário que digite uma string

substring_palindroma = encontrar_substring_palindroma(string_original) # Chamar a função para encontrar a maior substring palindrômica

if substring_palindroma:
    print("Maior substring palindrômica:", substring_palindroma)
else:
    print("Não há substrings palindrômicas na string.")



# 4°
print("4° Colocando em maiúscula a primeira letra de cada frase.")
def maiuscula_primeira_letra_frases(string):
    resultado = ''
    nova_frase = True

    for i in range(len(string)):
        if nova_frase and string[i].isalpha():
            resultado += string[i].upper()
            nova_frase = False
        else:
            resultado += string[i]
            if string[i] == '.':
                nova_frase = True

    return resultado

string_original = input("Digite uma string com frases: ") # Solicitar ao usuário que digite uma string com frases

string_maiuscula = maiuscula_primeira_letra_frases(string_original)
print("String com a primeira letra de cada frase em maiúscula:", string_maiuscula)


# 5°
print("5° Verificação se a string é um anagrama de um palindromo")
from collections import Counter

def verificar_anagrama_palindromo(string):
    contador = Counter(string)
    num_impares = 0

    for count in contador.values():
        if count % 2 != 0:
            num_impares += 1
            if num_impares > 1:
                return False

    return True

string_original = input("Digite uma string: ") # Solicitar ao usuário que digite uma string



if verificar_anagrama_palindromo(string_original): # Chamar a função para verificar se é um anagrama de um palíndromo
    print("A string é um anagrama de um palíndromo.")
else:
    print("A string não é um anagrama de um palíndromo.")



input("Pressione qualquer tecla para sair...") # Solicitar ao usuário que pressione uma tecla antes de encerrar
