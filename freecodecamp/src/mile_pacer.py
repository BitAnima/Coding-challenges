"""Mile Pace
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed.


Waiting:1. mile_pace(3, "24:00") should return "08:00".
Waiting:2. mile_pace(1, "06:45") should return "06:45".
Waiting:3. mile_pace(2, "07:00") should return "03:30".
Waiting:4. mile_pace(26.2, "120:35") should return "04:36"."""

def mile_pace(miles, duration):

    print(f"Distancia: {miles}; Tiempo: {duration}")

    #Para calcular el tiempo medio dividimos el string 'duration' y convertimos los caracteres a formato número
    minutos, segundos = duration.split(':')
    min_to_sec = int(minutos) * 60
    seconds = int(segundos)
    segundos_totales = min_to_sec + seconds

    #Después sumamos los segundos de los minutos a los segundos dados en la función
    print(f"{minutos} minutos y {segundos} segundos = {segundos_totales} segundos")

    #La media será el número de segundos totales divididos por el número de kilómetros
    seconds_average_pace = segundos_totales / miles

    #Para los minutos de media sólo necesitamos la parte entera
    min_average_pace = int(seconds_average_pace) // 60

    print(f"Media (en segundos totales): {int(seconds_average_pace):02d}")
    print(f"Media (en minutos): {min_average_pace}")

    #Necesitamos el resto de la media de los segundos entre 60 para saber cuántos segundos quedan que no se hayan repartido en minutos    
    resto = round(seconds_average_pace % 60)
    print(f"Media (en segundos): {resto}\n")

    # Usando f-string con ceros a la izquierda
    formato = f"{int(min_average_pace):02d}:{int(resto):02d}"  # "08:05"
    print(formato)

    average_string = formato

    print(f"El tiempo medio calculado es {formato}\n")
    
    return formato

print(f"\nDebemos calcular el tiempo medio en recorrer cada milla.\n")
mile_pace(3, "24:00")
mile_pace(1, "06:45")
mile_pace(2, "07:00")
mile_pace(26.2, "120:35")