
import tkinter as tk
from tkinter import messagebox

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import ecuacion
import graficadora



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ecuaciones Cuadraticas")
ventana.geometry("1050x750")
ventana.configure(bg="#F4F7FB")

# Titulo
titulo = tk.Label(
    ventana,
    text="CALCULADORA DE ECUACIONES CUADRATICAS",
    font=("Arial", 18, "bold"),
    bg="#F4F7FB",
    fg="#243B64"
)
titulo.pack(pady=15)

subtitulo = tk.Label(
    ventana,
    text="Resuelve y grafica: ax² + bx + c = 0",
    font=("Arial", 12),
    bg="#F4F7FB",
    fg="#52627A"
)
subtitulo.pack(pady=5)

# Panel de coeficientes
marco_entradas = tk.Frame(ventana, bg="#FFFFFF", padx=15, pady=12)
marco_entradas.pack(pady=10)

tk.Label(
    marco_entradas, text="Coeficiente a:",
    bg="#FFFFFF", fg="#243B64"
).grid(row=0, column=0, padx=8, pady=5)

entrada_a = tk.Entry(marco_entradas, width=10, justify="center")
entrada_a.grid(row=0, column=1, padx=8, pady=5)
entrada_a.insert(0, "")

tk.Label(
    marco_entradas, text="Coeficiente b:",
    bg="#FFFFFF", fg="#243B64"
).grid(row=0, column=2, padx=8, pady=5)

entrada_b = tk.Entry(marco_entradas, width=10, justify="center")
entrada_b.grid(row=0, column=3, padx=8, pady=5)
entrada_b.insert(0, "")

tk.Label(
    marco_entradas, text="Coeficiente c:",
    bg="#FFFFFF", fg="#243B64"
).grid(row=0, column=4, padx=8, pady=5)

entrada_c = tk.Entry(marco_entradas, width=10, justify="center")
entrada_c.grid(row=0, column=5, padx=8, pady=5)
entrada_c.insert(0, "")


def calcular():
    try:
        # Leer los coeficientes
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        # Validar que sea una ecuacion cuadratica
        if a == 0:
            messagebox.showerror(
                "Error",
                "El coeficiente a no puede ser cero."
            )
            return

        # Utilizar las funciones de ecuacion.py
        delta = ecuacion.calcular_discriminante(a, b, c)
        caso = ecuacion.analizar_casos_discriminante(a, b, c)
        raices = ecuacion.calcular_raices(a, b, c)
        datos_vertice = ecuacion.calcular_vertice_y_eje(a, b, c)

        vertice = datos_vertice["vertice"]
        eje = datos_vertice["eje_simetria"]

        # Mostrar resultados
        resultado_delta.config(
            text=f"Discriminante: {delta:.2f}"
        )

        resultado_caso.config(text=caso)

        
        
        if delta >= 0:
            resultado_raices.config(
                text=f"Raíz 1: {raices[0].real:.2f}\n"
                     f"Raíz 2: {raices[1].real:.2f}"
            )
        else:
            resultado_raices.config(
                text=f"Raíz 1: {raices[0]:.2f}\n"
                     f"Raíz 2: {raices[1]:.2f}"
            )


        resultado_vertice.config(
            text=f"Vertice: ({vertice[0]:.2f}, {vertice[1]:.2f})"
        )

        resultado_eje.config(
            text=f"Eje de simetria: x = {eje:.2f}"
        )

        # Actualizar la grafica
        graficadora.graficar(a, b, c, ax, canvas)

    
    except ValueError:
        messagebox.showerror(
            "Entrada no válida",
            "Por favor, ingresa números válidos en los tres coeficientes."
        )


# Botones
marco_botones = tk.Frame(ventana, bg="#F4F7FB")
marco_botones.pack(pady=8)


boton_calcular = tk.Button(
    marco_botones,
    text="Calcular y graficar",
    command=calcular,
    bg="#DCE5F2",
    fg="#243B64",
    font=("Arial", 11, "bold"),
    padx=12,
    pady=6
)
boton_calcular.pack(side="left", padx=8)


def limpiar():
    entrada_a.delete(0, tk.END)
    entrada_b.delete(0, tk.END)
    entrada_c.delete(0, tk.END)

    resultado_delta.config(text="Discriminante: pendiente")
    resultado_caso.config(text="Tipo de raíces: pendiente")
    resultado_raices.config(text="Raíces: pendiente")
    resultado_vertice.config(text="Vértice: pendiente")
    resultado_eje.config(text="Eje de simetría: pendiente")

    ax.clear()
    ax.set_title("Gráfica de la ecuación cuadrática")
    ax.grid(True)
    canvas.draw()


boton_limpiar = tk.Button(
    marco_botones,
    text="Limpiar",
    command=limpiar,
    bg="#DCE5F2",
    fg="#243B64",
    font=("Arial", 11, "bold"),
    padx=12,
    pady=6
)
boton_limpiar.pack(side="left", padx=8)



# Panel principal para resultados y grafica
marco_contenido = tk.Frame(ventana, bg="#F4F7FB")
marco_contenido.pack(fill="both", expand=True, padx=15, pady=10)

# Panel de resultados
marco_resultados = tk.LabelFrame(
    marco_contenido,
    text="Resultados matematicos",
    font=("Arial", 11, "bold"),
    bg="#FFFFFF",
    fg="#243B64",
    padx=12,
    pady=12
)
marco_resultados.pack(side="left", fill="both", padx=8, pady=5)

resultado_delta = tk.Label(
    marco_resultados,
    text="Discriminante: pendiente",
    bg="#FFFFFF",
    fg="#243B64",
    justify="left",
    wraplength=280
)
resultado_delta.pack(anchor="w", pady=8)

resultado_caso = tk.Label(
    marco_resultados,
    text="Tipo de raíces: pendiente",
    bg="#FFFFFF",
    fg="#243B64",
    justify="left",
    wraplength=280
)
resultado_caso.pack(anchor="w", pady=8)

resultado_raices = tk.Label(
    marco_resultados,
    text="Raíces: pendiente",
    bg="#FFFFFF",
    fg="#243B64",
    justify="left",
    wraplength=280
)
resultado_raices.pack(anchor="w", pady=8)

resultado_vertice = tk.Label(
    marco_resultados,
    text="Vértice: pendiente",
    bg="#FFFFFF",
    fg="#243B64",
    justify="left"
)
resultado_vertice.pack(anchor="w", pady=8)

resultado_eje = tk.Label(
    marco_resultados,
    text="Eje de simetría: pendiente",
    bg="#FFFFFF",
    fg="#243B64",
    justify="left"
)
resultado_eje.pack(anchor="w", pady=8)

# Panel de la grafica
marco_grafica = tk.LabelFrame(
    marco_contenido,
    text="Grafica de la parabola",
    font=("Arial", 11, "bold"),
    bg="#FFFFFF",
    fg="#243B64"
)
marco_grafica.pack(
    side="left", fill="both", expand=True, padx=8, pady=5
)

figura = Figure(figsize=(6, 4.5), dpi=100)
ax = figura.add_subplot(111)

canvas = FigureCanvasTkAgg(figura, master=marco_grafica)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Mantener abierta la ventana
ventana.mainloop()

