def zero(num: int, years: list):
    prueba = []
    if num == len(years):
        for year in years:
            if -3000 <= year <= 3000:
                if year >= 1:
                    prueba.append(year-1)
                else:
                    prueba.append(year)
            else:
                return 'error'
        return prueba
    else:
        return 'error'

if __name__ == "__main__":
    # Recoger datos de la terminal
    num = int(input())
    years_input = []
    for i in range(num):
        year = int(input())  # Pedir cada año
        years_input.append(year)  # Añadir el año a la lista

    # Llamada a la función y mostrar el resultado
    resultado = zero(num, years_input)
    for res in resultado:
        print(res)


