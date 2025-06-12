from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import os
import sys



def interface_editar_carimbo():


    # return [output1, output2, output3, output4, output5, output6, output7, output8, output10, output11, output12, chosenFolder]


# # folder = selecionar_pasta_PROJETO()  # Variável que armazena o caminho da pasta
# [LCMilePost, rev, HouseKM, project_number, LCMilePostB, revB, HouseKMB, project_numberB, firstProj, text, textB, folder] = interface_editar_carimbo()
# # print(f"{folder}\n{LCMilePost}\n{rev}\n{HouseKM}\n{project_number}\n{LCMilePostB}\n{revB}\n{HouseKMB}\n{project_numberB}\n{firstProj}\n{text}\n{textB}")
#
# midNamesArray = os.listdir(folder)
# print(midNamesArray)
# fullNamesArray = []
# for i in range(len(midNamesArray)):
#     fullNamesArray.append(os.path.join(folder, midNamesArray[i]))
#
# for files in range(len(fullNamesArray)):
#     if firstProj:
#         old_name = fullNamesArray[files]
#         new_name = fullNamesArray[files].replace("J-00000_", f"J-{project_number}_")
#         os.rename(old_name, new_name)
#     else:
#         old_name = fullNamesArray[files]
#         new_name = fullNamesArray[files].replace(f"J-{project_number}_", f"J-{project_numberB}_")
#         os.rename(old_name, new_name)
#
# newMidNamesArray = os.listdir(folder)
# newFullNamesArray = []
# for j in range(len(newMidNamesArray)):
#     newFullNamesArray.append(os.path.join(folder, newMidNamesArray[j]))
#
# # print(newFullNamesArray)
# # print(len(newFullNamesArray))
#
# for newFiles in range(len(newFullNamesArray)):
#     newFullFileName = newFullNamesArray[newFiles]
#
#     with open(newFullFileName, "r", encoding="utf8") as f:
#         conteudo = f.read()
#
#     if firstProj:
#         novo_conteudo = (conteudo.replace("PN KM XXX+XXX", f"PN KM {LCMilePost}")
#                          .replace("KM YYY+YYY",f"KM {HouseKM}")
#                          .replace("  A  ", f"  {rev}  ")
#                          .replace("J-00000 ", f"J-{project_number} ")
#                          .replace("CIDADE", f"{text}"))
#         with open(newFullFileName, 'w', encoding="utf8") as f:
#             f.write(novo_conteudo)
#     else:
#         novo_conteudo = (conteudo.replace(f"PN KM {LCMilePost}", f"PN KM {LCMilePostB}")
#                          .replace(f"KM {HouseKM}",f"KM {HouseKMB}")
#                          .replace(f"  {rev}  ", f"  {revB}  ")
#                          .replace(f"J-{project_number} ", f"J-{project_numberB} ")
#                          .replace(f"{text}", f"{textB}"))
#         with open(newFullFileName, 'w', encoding="utf8") as f:
#             f.write(novo_conteudo)
#
# print("Finalizado")


