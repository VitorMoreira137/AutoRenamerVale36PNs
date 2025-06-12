from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import os
import sys



def interface_editar_carimbo():
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)  # código para fazer a imagem ser aceita no executavel
        # no terminal na hora de riar o .exe digite: pyinstaller --onefile -w  --add-data "logo-wbt.ico;." AutoRenamerv4.0.py

    def selecionar_pasta_PROJETO():
        global caminho_pasta
        caminho_pasta = filedialog.askdirectory()  # Abre o explorador de arquivos para armazenar o caminho das pasta desejada na variável
        caminho_pasta_convertido = ''.join(caminho_pasta)  # CONVERSÃO DA STRING
        return caminho_pasta_convertido

    janela = ctk.CTk()  # Cria uma janela
    janela.iconbitmap(resource_path("logo-wbt.ico"))
    janela.title('Edição de Carimbos - VALE EFVM')  # Atribui um título
    janela.geometry('750x400')  # Define as dimensões da janela
    # janela.wm_attributes('-topmost', 1)  # ATRIBUIR MINHA JANELA PARA SOBREPOR OS ELEMENTOS DA TELA

    var1 = ctk.StringVar()  # Armazena o que usuário digitar
    var2 = ctk.StringVar()
    var3 = ctk.StringVar()
    var4 = ctk.StringVar()
    var5 = ctk.StringVar()
    var1B = ctk.StringVar()
    var2B = ctk.StringVar()
    var3B = ctk.StringVar()
    var4B = ctk.StringVar()
    var5B = ctk.StringVar()
    var6 = ctk.IntVar()
    var7 = ctk.StringVar()

    def desabilitar_controle():

        if var6.get() == 3:
            EA1.configure(state=NORMAL, fg_color="white")
            EA2.configure(state=NORMAL, fg_color="white")
            EA3.configure(state=NORMAL, fg_color="white")
            EA4.configure(state=NORMAL, fg_color="white")
            EA5.configure(state=NORMAL, fg_color="white")
            EB1.configure(state=DISABLED, fg_color="grey")
            EB2.configure(state=DISABLED, fg_color="grey")
            EB3.configure(state=DISABLED, fg_color="grey")
            EB4.configure(state=DISABLED, fg_color="grey")
            EB5.configure(state=DISABLED, fg_color="grey")

        elif var6.get() == 4:
            EA1.configure(state=NORMAL, fg_color="white")
            EA2.configure(state=NORMAL, fg_color="white")
            EA2.delete(0, END)  # apaga o conteudo do CTkEntry EA2
            EA3.configure(state=NORMAL, fg_color="white")
            EA4.configure(state=NORMAL, fg_color="white")
            EA5.configure(state=NORMAL, fg_color="white")
            EB1.configure(state=NORMAL, fg_color="white")
            EB2.configure(state=NORMAL, fg_color="white")
            EB3.configure(state=NORMAL, fg_color="white")
            EB4.configure(state=NORMAL, fg_color="white")
            EB5.configure(state=NORMAL, fg_color="white")

    def firstProjectChecker():
        if var6.get() == 3:
            return TRUE
        elif var6.get() == 4:
            return FALSE

    B0 = ctk.CTkButton(janela, text="Selecionar Pasta 📁", width=70, command=lambda: var7.set(selecionar_pasta_PROJETO()))
    B0.grid(row=0, column=0, sticky=ctk.W, padx=10, pady=10)

    R0 = ctk.CTkRadioButton(janela, text="Emissão Inicial", variable=var6, value=3, command=lambda: [desabilitar_controle(), firstProjectChecker()])
    R0.grid(row=1, column=0)

    R1 = ctk.CTkRadioButton(janela, text="Emissão Existente", variable=var6, value=4, command=lambda: [desabilitar_controle(), firstProjectChecker()])
    R1.grid(row=1, column=1)

    ctk.CTkLabel(janela, text="EMISSÃO ATUAL", text_color="#4287f5").grid(row=2, column=1, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    ctk.CTkLabel(janela, text="EMISSÃO FUTURA", text_color="#4287f5").grid(row=2, column=3)  # Cria um CTkLabel

    ctk.CTkLabel(janela, text="KM da PN:").grid(row=3, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EA1 = ctk.CTkEntry(janela, textvariable=var1, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EA1.grid(row=3, column=1, sticky=ctk.W)

    ctk.CTkLabel(janela, text="Revisão do Projeto:").grid(row=4, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EA2 = ctk.CTkEntry(janela, textvariable=var2, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EA2.insert(0, "A")  # placeholder 0A
    EA2.grid(row=4, column=1, sticky=ctk.W)

    ctk.CTkLabel(janela, text="KM do Ativo:").grid(row=5, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EA3 = ctk.CTkEntry(janela, textvariable=var3, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EA3.grid(row=5, column=1, sticky=ctk.W)

    ctk.CTkLabel(janela, text="Número de Projeto:").grid(row=6, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EA4 = ctk.CTkEntry(janela, textvariable=var4, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EA4.grid(row=6, column=1, sticky=ctk.W)

    ctk.CTkLabel(janela, text="Renomear Texto:").grid(row=7, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EA5 = ctk.CTkEntry(janela, textvariable=var5, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EA5.grid(row=7, column=1, sticky=ctk.W)

    ctk.CTkLabel(janela, text="KM da PN:").grid(row=3, column=2, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EB1 = ctk.CTkEntry(janela, textvariable=var1B, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EB1.grid(row=3, column=3, sticky=ctk.W)

    ctk.CTkLabel(janela, text="Revisão do Projeto:").grid(row=4, column=2, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EB2 = ctk.CTkEntry(janela, textvariable=var2B, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EB2.grid(row=4, column=3, sticky=ctk.W)

    ctk.CTkLabel(janela, text="KM do Ativo:").grid(row=5, column=2, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EB3 = ctk.CTkEntry(janela, textvariable=var3B, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EB3.grid(row=5, column=3, sticky=ctk.W)

    ctk.CTkLabel(janela, text="Número de Projeto:").grid(row=6, column=2, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EB4 = ctk.CTkEntry(janela, textvariable=var4B, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EB4.grid(row=6, column=3, sticky=ctk.W)

    ctk.CTkLabel(janela, text="Renomear Texto:").grid(row=7, column=2, sticky=ctk.W, padx=25)  # Cria um CTkLabel
    EB5 = ctk.CTkEntry(janela, textvariable=var5B, width=200, fg_color="white", text_color="blue")  # cria um input box e salva o que o usuário digitou
    EB5.grid(row=7, column=3, sticky=ctk.W)

    EA1.configure(state=DISABLED, fg_color="grey")
    EA2.configure(state=DISABLED, fg_color="grey")
    EA3.configure(state=DISABLED, fg_color="grey")
    EA4.configure(state=DISABLED, fg_color="grey")
    EA5.configure(state=DISABLED, fg_color="grey")
    EB1.configure(state=DISABLED, fg_color="grey")
    EB2.configure(state=DISABLED, fg_color="grey")
    EB3.configure(state=DISABLED, fg_color="grey")
    EB4.configure(state=DISABLED, fg_color="grey")
    EB5.configure(state=DISABLED, fg_color="grey")

    B1 = ctk.CTkButton(janela, text="RENOMEAR", width=70, command=janela.destroy)
    B1.grid(row=8, column=1, sticky=ctk.W, pady=4)

    janela.mainloop()  # Mantém a janela aparecendo

    output1 = var1.get().upper()
    output2 = var2.get().upper()
    output3 = var3.get().upper()
    output4 = var4.get().upper()
    output5 = var1B.get().upper()
    output6 = var2B.get().upper()
    output7 = var3B.get().upper()
    output8 = var4B.get().upper()
    output10 = firstProjectChecker()
    output11 = var5.get().upper()
    output12 = var5B.get().upper()
    chosenFolder = var7.get()


    return [output1, output2, output3, output4, output5, output6, output7, output8, output10, output11, output12, chosenFolder]


# folder = selecionar_pasta_PROJETO()  # Variável que armazena o caminho da pasta
[LCMilePost, rev, HouseKM, project_number, LCMilePostB, revB, HouseKMB, project_numberB, firstProj, text, textB, folder] = interface_editar_carimbo()
# print(f"{folder}\n{LCMilePost}\n{rev}\n{HouseKM}\n{project_number}\n{LCMilePostB}\n{revB}\n{HouseKMB}\n{project_numberB}\n{firstProj}\n{text}\n{textB}")

midNamesArray = os.listdir(folder)
print(midNamesArray)
fullNamesArray = []
for i in range(len(midNamesArray)):
    fullNamesArray.append(os.path.join(folder, midNamesArray[i]))

for files in range(len(fullNamesArray)):
    if firstProj:
        old_name = fullNamesArray[files]
        new_name = fullNamesArray[files].replace("J-00000_", f"J-{project_number}_")
        os.rename(old_name, new_name)
    else:
        old_name = fullNamesArray[files]
        new_name = fullNamesArray[files].replace(f"J-{project_number}_", f"J-{project_numberB}_")
        os.rename(old_name, new_name)

newMidNamesArray = os.listdir(folder)
newFullNamesArray = []
for j in range(len(newMidNamesArray)):
    newFullNamesArray.append(os.path.join(folder, newMidNamesArray[j]))

# print(newFullNamesArray)
# print(len(newFullNamesArray))

for newFiles in range(len(newFullNamesArray)):
    newFullFileName = newFullNamesArray[newFiles]

    with open(newFullFileName, "r", encoding="utf8") as f:
        conteudo = f.read()

    if firstProj:
        novo_conteudo = (conteudo.replace("PN KM XXX+XXX", f"PN KM {LCMilePost}")
                         .replace("KM YYY+YYY",f"KM {HouseKM}")
                         .replace("  A  ", f"  {rev}  ")
                         .replace("J-00000 ", f"J-{project_number} ")
                         .replace("CIDADE", f"{text}"))
        with open(newFullFileName, 'w', encoding="utf8") as f:
            f.write(novo_conteudo)
    else:
        novo_conteudo = (conteudo.replace(f"PN KM {LCMilePost}", f"PN KM {LCMilePostB}")
                         .replace(f"KM {HouseKM}",f"KM {HouseKMB}")
                         .replace(f"  {rev}  ", f"  {revB}  ")
                         .replace(f"J-{project_number} ", f"J-{project_numberB} ")
                         .replace(f"{text}", f"{textB}"))
        with open(newFullFileName, 'w', encoding="utf8") as f:
            f.write(novo_conteudo)

print("Finalizado")


