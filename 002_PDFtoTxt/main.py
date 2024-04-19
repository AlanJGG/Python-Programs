import tkinter as tk
from pdf import pdf_a_txt

ventana = tk.Tk()

ventana.title("Convertir PDF a TXT")

boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo PDF", command=pdf_a_txt)
boton_seleccionar.pack(pady=10)

ventana.mainloop()