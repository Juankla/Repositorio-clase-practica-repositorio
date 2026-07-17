
def resolver_ecuacion():
    # 1. Validar variables
    a = 2  # coeficiente de x
    b = 3  # término independiente

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Error: los coeficientes deben ser numéricos.")
        return

    if (1 - a) == 0:
        print("Error: la ecuación no tiene solución única.")
        return

    # 2. Analizar el proceso
    # x = 2x + 3  ->  x - 2x = 3  ->  -x = 3  ->  x = b / (1 - a)
    x = b / (1 - a)

    # 3. Entregar un resultado
    print(f"El valor de x que resuelve la ecuación es: {x}")

    # Comprobación
    comprobacion = 2 * x + 3
    if comprobacion == x:
        print(f"Comprobación correcta: X = x = {comprobacion}")
    else:
        print("Error en el cálculo")


if __name__ == "__main__":
    resolver_ecuacion()