
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def graficar():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        if a == 0:
            messagebox.showerror(
                "Error",
                "El valor de a no puede ser cero."
            )
            return

        # Calcular el vertice
        xv = -b / (2 * a)
        yv = a * xv**2 + b * xv + c

        # Calcular el discriminante
        d = b**2 - 4 * a * c

        # Calcular las raices reales
        raices = []

        if d >= 0:
            x1 = (-b + d**0.5) / (2 * a)
            x2 = (-b - d**0.5) / (2 * a)
            raices = [x1, x2]

        # Ajustar el rango del eje X
        puntos_x = [-10, 10, xv]

        for raiz in raices:
            puntos_x.append(raiz)

        x_min = min(puntos_x) - 2
        x_max = max(puntos_x) + 2

        # Calcular los valores de la parabola
        x = np.linspace(x_min, x_max, 400)
        y = a * x**2 + b * x + c

        # Limpiar la grafica anterior
        ax.clear()

        ax.plot(
            x, y,
            label=f"y = {a}x² + {b}x + {c}"
        )

        # Dibujar los ejes cartesianos
        ax.axhline(0, color="black", linewidth=1)
        ax.axvline(0, color="black", linewidth=1)

        # Marcar el vertice
        ax.scatter(
            xv, yv,
            color="red",
            label="Vertice",
            zorder=3
        )

        # Marcar las raices reales
        if d >= 0:
            ax.scatter(
                raices, [0, 0],
                color="green",
                label="Raices reales",
                zorder=3
            )

            texto_raices = (
                f"Raices: {x1:.2f} y {x2:.2f}"
            )
        else:
            texto_raices = "No hay raices reales."

        # Configurar la grafica
        ax.set_xlim(x_min, x_max)
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.set_title("Grafica de la ecuacion cuadratica")
        ax.grid(True)
        ax.legend()

        # Mostrar la grafica en la ventana
        canvas.draw()

        # Mostrar los resultados
        resultado.config(
            text=(
                f"Vertice: ({xv:.2f}, {yv:.2f})\n"
                f"{texto_raices}"
            )
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingresa numeros validos."
        )


# Crear la ventana
ventana = tk.Tk()
ventana.title("Graficador de ecuaciones cuadraticas")
ventana.geometry("850x700")

tk.Label(
    ventana,
    text="ECUACION CUADRATICA: y = ax² + bx + c",
    font=("Arial", 15, "bold")
).pack(pady=10)

# Crear los campos para los coeficientes
marco = tk.Frame(ventana)
marco.pack()

tk.Label(marco, text="Valor de a:").grid(row=0, column=0)
entrada_a = tk.Entry(marco, width=10)
entrada_a.grid(row=0, column=1, padx=5)
entrada_a.insert(0, "1")

tk.Label(marco, text="Valor de b:").grid(row=0, column=2)
entrada_b = tk.Entry(marco, width=10)
entrada_b.grid(row=0, column=3, padx=5)
entrada_b.insert(0, "0")

tk.Label(marco, text="Valor de c:").grid(row=0, column=4)
entrada_c = tk.Entry(marco, width=10)
entrada_c.grid(row=0, column=5, padx=5)
entrada_c.insert(0, "-4")

# Crear el boton
boton = tk.Button(
    ventana,
    text="Graficar ecuacion",
    command=graficar,
    bg="lightblue",
    font=("Arial", 11, "bold")
)
boton.pack(pady=10)

# Mostrar los resultados
resultado = tk.Label(
    ventana,
    text="Los resultados apareceran aqui",
    font=("Arial", 11)
)
resultado.pack()

# Crear la grafica dentro de la ventana
figura, ax = plt.subplots(figsize=(7, 4.5))
canvas = FigureCanvasTkAgg(figura, master=ventana)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Graficar al iniciar
graficar()

# Mantener abierta la ventana
ventana.mainloop()
