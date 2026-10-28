
import numpy as np


def graficar(a, b, c, ax, canvas):
    if a == 0:
        raise ValueError("El valor de a no puede ser cero.")

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
    puntos_x.extend(raices)

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

    # Configurar la grafica
    ax.set_xlim(x_min, x_max)
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title("Grafica de la ecuacion cuadratica")
    ax.grid(True)
    ax.legend()

    # Actualizar el dibujo
    canvas.draw()



#Codigo adaptado para la interfaz grafica 
#No se hicieron cambios radicales, solo se adapto para implementar la funcion a la ventana
#Paso las pruebas de humo