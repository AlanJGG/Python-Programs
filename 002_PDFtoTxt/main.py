import tkinter as tk
from pdf import pdf_a_txt
from screeninfo import get_monitors

ventana = tk.Tk()
ventana.title("Convertir PDF a TXT")

screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calcula la posición central de la ventana
window_width = 300
window_height = 50
x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2

# Configura la geometría de la ventana para centrarla en la pantalla
ventana.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo PDF", command=pdf_a_txt)
boton_seleccionar.pack(pady=10)

ventana.mainloop()