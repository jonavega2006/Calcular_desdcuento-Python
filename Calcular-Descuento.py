def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final


def main():
    # Pedir al usuario el monto total en dólares
    try:
        monto_total = float(input("Introduce el monto total de la compra en dólares ($): "))

        # Preguntar si desea el descuento por defecto o ingresar otro porcentaje
        opcion = input("¿Quieres el descuento por defecto de 10% o ingresar otro porcentaje? (sí/no): ").strip().lower()

        if opcion == "no":
            porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))
        else:
            porcentaje_descuento = 10  # Descuento por defecto

        # Llamar a la función para calcular el descuento
        descuento, monto_final = calcular_descuento(monto_total, porcentaje_descuento)

        # Mostrar los resultados en dólares
        print(f"\nEl descuento es: ${descuento:.2f} dólares.")
        print(f"El monto final a pagar es: ${monto_final:.2f} dólares.")

    except ValueError:
        print("Error: Debes ingresar un número válido.")


if __name__ == "__main__":
    main()
