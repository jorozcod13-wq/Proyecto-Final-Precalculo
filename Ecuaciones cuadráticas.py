import cmath

def calcular_discriminante(a: float, b: float, c: float) -> float:
    return (b ** 2) - (4 * a * c)

def analizar_casos_discriminante(a: float, b: float, c: float) -> str:
    delta = calcular_discriminante(a, b, c)

    if delta > 0:
        return f"Caso 1: Delta = {delta} > 0 (Dos raíces reales y distintas)"
    elif delta == 0:
        return f"Caso 2: Delta = {delta} = 0 (Una raíz real doble)"
    else:
        return f"Caso 3: Delta = {delta} < 0 (Dos raíces complejas conjugadas)"

def calcular_raices(a: float, b: float, c: float) -> tuple:
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero en una ecuación cuadrática.")

    delta = calcular_discriminante(a, b, c)
    raiz_delta = cmath.sqrt(delta)

    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

    return (x1, x2)


def calcular_vertice_y_eje(a: float, b: float, c: float) -> dict:
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero.")

    h = -b / (2 * a)
    k = (4 * a * c - b ** 2) / (4 * a)

    return {
        "eje_simetria": h,
        "vertice": (h, k)
    }


if __name__ == "__main__":
    print("==================================================")
    print("   PRECÁLCULO: ANALIZADOR DE ECUACIONES CUADRÁTICAS")
    print("==================================================\n")

    try:
        print("Ingrese los coeficientes de la forma estándar: ax^2 + bx + c = 0")
        a = float(input("Ingrese el coeficiente a (a != 0): "))

        if a == 0:
            print("\n[Error]: Si a = 0, la ecuación deja de ser cuadrática.")
        else:
            b = float(input("Ingrese el coeficiente b: "))
            c = float(input("Ingrese el coeficiente c: "))

            print(f"\n________________________________________________")
            print(f"Ecuación analizada: {a}x^2 + ({b})x + {c} = 0")
            print(f"__________________________________________________")

            print(f"• {analizar_casos_discriminante(a, b, c)}")
            
            raices = calcular_raices(a, b, c)
            print(f"• Raíces (Soluciones):")
            print(f"  - x1 = {raices[0]}")
            print(f"  - x2 = {raices[1]}")

            parabola = calcular_vertice_y_eje(a, b, c)
            print(f"• Eje de simetría: x = {parabola['eje_simetria']}")
            print(f"• Vértice (h, k): {parabola['vertice']}")
            print(f"_____________________________________________________")

    except ValueError:
        print("\n[Error]: Debe ingresar valores numéricos válidos (números enteros o decimales).")