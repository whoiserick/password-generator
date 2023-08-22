import random
import string
import tkinter as tk

def gerar_senha():
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    caracteres = letras + numeros + simbolos
    tamanho_senha = 12
    senha = ''.join(random.choices(caracteres, k=tamanho_senha))
    
    with open("senha.txt", "a") as arquivo:
        arquivo.write("Senha gerada: " + senha + "\n")
    
    senha_gerada_label.config(text="Senha gerada:")
    senha_text.config(state=tk.NORMAL)
    senha_text.delete("1.0", tk.END)
    senha_text.insert(tk.END, senha)
    senha_text.config(state=tk.DISABLED)

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("300x150")

# Botão para gerar senha
gerar_button = tk.Button(root, text="Gerar Senha", command=gerar_senha)
gerar_button.pack(pady=20)

# Label para exibir a senha gerada
senha_gerada_label = tk.Label(root, text="Senha gerada:")
senha_gerada_label.pack()

# Campo de texto para exibir a senha gerada
senha_text = tk.Text(root, height=1, width=20)
senha_text.config(state=tk.DISABLED)
senha_text.pack()

# Executar a interface
root.mainloop()
