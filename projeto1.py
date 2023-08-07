import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos") # list  of  arquivos
lista_arquivos.sort() #ordenar la list
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}") #append adicional

merger.write("PDF Final.pdf")