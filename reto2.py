from datetime import datetime


def christmas(num: int, dates: list):
    prueba = []
    if num == len(dates):
        for date in dates:
            formated_date = datetime.strptime(date, '%d %m')
            prueba.append(formated_date)
        respuesta = []
        for date in prueba:
            if date.day == 25 and date.month == 12:
                respuesta.append('SÍ')
            else:
                respuesta.append('NO')
        return respuesta
            
if __name__ == "__main__":
    # Recoger datos de la terminal
    num = int(input())
    dates_input = []
    for i in range(num):
        date = input()  # Pedir cada año
        dates_input.append(date)  # Añadir el año a la lista

    # Llamada a la función y mostrar el resultado
    resultado = christmas(num, dates_input)
    for res in resultado:
        print(res)