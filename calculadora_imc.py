# Calculadora de Índice de Masa Corporal (IMC)
def main():
    print("Bienvenido a la Calculadora de IMC")
    print("Este programa calcula tu Índice de Masa Corporal.\n")

    try:
        # Solicitar al usuario el peso y la altura
        peso = float(input("Introduce tu peso en kilogramos (kg): "))
        altura = float(input("Introduce tu altura en metros (m): "))

        # Validar que los valores sean positivos
        if peso <= 0 or altura <= 0:
            print("Por favor, introduce valores mayores a cero.")
            return

        # Calcular el IMC
        imc = peso / (altura ** 2)

        # Mostrar el resultado
        print(f"\nTu IMC es: {imc:.2f}")

        # Interpretación del IMC
        if imc < 18.5:
            print("Interpretación: Bajo peso")
        elif 18.5 <= imc < 24.9:
            print("Interpretación: Peso normal")
        elif 25 <= imc < 29.9:
            print("Interpretación: Sobrepeso")
        else:
            print("Interpretación: Obesidad")
    except ValueError:
        print("Error: Por favor, introduce valores numéricos válidos.")

# Ejecutar la calculadora
if __name__ == "__main__":
    main()