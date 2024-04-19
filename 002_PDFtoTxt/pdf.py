import PyPDF2
import tkinter as tk   
from tkinter import filedialog

def extraer_texto(pdf_path):
    texto = ""
    with open(pdf_path, "rb") as archivo_pdf:
        lector_pdf = PyPDF2.PdfFileReader(archivo_pdf)
        num_paginas = lector_pdf.numPages
        for pagina in range(num_paginas):
            texto += lector_pdf.getPage(pagina).extractText()
    archivo_pdf.close()
    return texto

def pdf_a_txt():
    ruta_pdf = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
    if ruta_pdf:
        texto_extraido = extraer_texto(ruta_pdf)
        ruta_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if ruta_guardado:
            with open(ruta_guardado, "w", encoding="utf-8") as archivo_txt:
                archivo_txt.write(texto_extraido)
            tk.messagebox.showinfo("Éxito", "El archivo se ha convertido a texto correctamente.")
            archivo_txt.close()