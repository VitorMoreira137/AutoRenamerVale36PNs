import tkinter as tk
from tkinter import filedialog


def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(title="Selecione um arquivo")
    print(f"Arquivo selecionado: {caminho_arquivo}")
    return caminho_arquivo  # Retorna o caminho do arquivo


def criar_interface():
    janela = tk.Tk()
    janela.title("Selecionar Arquivo")

    botao = tk.Button(janela, text="Escolher Arquivo", command=lambda: var.set(selecionar_arquivo()))
    botao.pack(pady=20)

    var = tk.StringVar()

    janela.mainloop()
    return var.get()  # Retorna o caminho após o fechamento da janela


# Chamando a função para criar a interface
caminho_selecionado = criar_interface()
print(f"Caminho retornado: {caminho_selecionado}")