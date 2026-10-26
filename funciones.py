
import tkinter as tk


# BOTÓN CALCULAR Y GRAFICAR
def calcular(entrada_a, entrada_b, entrada_c,
             resolver_ecuacion, dibujar_grafica):

    try:
        # Leer los coeficientes ingresados
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        # Validar que sea una ecuación cuadrática
        if a == 0:
            from tkinter import messagebox
            messagebox.showerror(
                "Dato incorrecto",
                "El coeficiente a no puede ser cero."
            )
            return

        # Llamar a las funciones de los compañeros
        resolver_ecuacion(a, b, c)
        dibujar_grafica(a, b, c)

    except ValueError:
        from tkinter import messagebox
        messagebox.showerror(
            "Error de entrada",
            "Ingresa números válidos en las tres casillas."
        )


# BOTÓN LIMPIAR
def limpiar(entradas, resultados, limpiar_grafica):
    # Vaciar las casillas
    for entrada in entradas:
        entrada.delete(0, tk.END)

    # Restablecer los textos de resultados
    for resultado, texto_inicial in resultados:
        resultado.config(text=texto_inicial)

    # Limpiar la gráfica
    limpiar_grafica()
