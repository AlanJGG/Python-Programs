import PyPDF2
import tkinter as tk   
from tkinter import filedialog, messagebox

def extraer_texto(pdf_path):
    texto = ""
    with open(pdf_path, "rb") as archivo_pdf:
        lector_pdf = PyPDF2.PdfReader(archivo_pdf)
        num_paginas = len(lector_pdf.pages)
        for pagina in range(num_paginas):
            texto += lector_pdf.pages[pagina].extract_text()
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
            
            messagebox.showinfo("Éxito", "El archivo PDF se ha convertido a texto correctamente.")