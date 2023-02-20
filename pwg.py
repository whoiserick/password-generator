import random
import string

# Definir os caracteres possíveis para cada tipo
letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

# Concatenar os tipos de caracteres em uma única string
caracteres = letras + numeros + simbolos

# Definir o tamanho da senha
tamanho_senha = 12

# Gerar a senha aleatória
senha = ''.join(random.choices(caracteres, k=tamanho_senha))

# Salvar a senha em um arquivo .txt
with open("senhas.txt", "a") as arquivo:
    arquivo.write("Senha gerada: " + senha + "\n")

# Exibir a senha gerada
print("Senha gerada:", senha)