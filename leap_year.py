def leap_year(anio: int) -> str:
    es_bisiesto = (anio % 4 == 0) and ((anio % 100 != 0) or (anio % 400 == 0))
    return f"El año {anio} {'es bisiesto' if es_bisiesto else 'no es bisiesto'}"


if __name__ == "__main__":
    anio = int(input("Ingrese un año: "))
    mensaje = leap_year(anio)
    results = [mensaje]
    print(mensaje)
