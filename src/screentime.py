"""
Screen Time
Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

If any single day has 10 hours or more, it's too much.
If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
If the average of the seven days is greater than or equal to 6 hours, it's too much.
"""
def print_message(result):
    if result == True:
        print(f"\nHas pasado demasiado tiempo delante de una pantalla esta semana.")
    else:
        print(f"\nEsta semana has controlado bastante bien el tiempo que pasas delante de una pantalla. ¡Bien hecho!")

def too_much_screen_time(hours):

    result = False # Es necesario inicializar la función por si ninguna de las condiciones se cumple

    # Creamos una lista de las horas diarias
    day_time_list = []
    for day_time in hours:
        day_time_list.append(day_time)

    # Creamos otra lista para los días de la semana
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    #Creamos un diccionario a partir de las dos listas
    screen_time_dict = dict(zip(week_days, day_time_list))

    """
    El diccionario se podría crear directamente sin necesidad de crear la lista de las horas diarias así:
    def too_much_screen_time(hours):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    screen_time_dict = dict(zip(week_days, hours))
    print(screen_time_dict)
    """
    week_sum = 0
    three_days_avg = 0
    weekly_avg = 1

    for time in screen_time_dict.values(): #Si no se añade .values(), se estarían recorriendo las claves, no los valores del diccionario
               
        if time >= 10:
            result=True
            
        """Si se quisiera iterar tanto por las keys como por los valores, sería así
            for day, time in screen_time_dict.items():
                if time >= 10:
                    result = True
                    """
    
    for i, time in enumerate(hours):  # Así tienes tanto el índice como el valor (hora)
        week_sum += time
        print(f"\n{week_days[i]}: {time} hour(s)") #Como las listas tienen la misma longitud, Python asigna la posición y el valor directamente

        weekly_avg = week_sum / 7
        #print(f"Media semanal: {weekly_avg:.02f}") # :.02f imprime la media con dos decimales (float)

    # Cálculo media de tres días seguidos (sólo si quedan mínimo 3 días)
        if i <= len(hours) - 3:
            three_days_avg = (hours[i] + hours[i+1] + hours[i+2]) / 3
            print(f"Media de 3 días {week_days[i]}, {week_days[i+1]}, {week_days[i+2]}: {three_days_avg:.02f}")
        if three_days_avg >= 8:
            result = True
              
    
    # Tercer requisito: media semanal >= 6
    if weekly_avg >= 6:
        result = True
        
    
    print(f"\nMedia semanal: {weekly_avg:.02f}\n") # :.02f imprime la media con dos decimales (float)

    print_message(result)

    return result

print("\n=================\nSemana 1:")
result = too_much_screen_time([1, 2, 3, 4, 5, 6, 7]) # False.

print("\n=================\nSemana 2:")
too_much_screen_time([7, 8, 8, 4, 2, 2, 3]) # False.

print("\n=================\nSemana 3:")
too_much_screen_time([5, 6, 6, 6, 6, 6, 6]) # False.

print("\n=================\nSemana 4:")
too_much_screen_time([1, 2, 3, 11, 1, 3, 4]) # True.

print("\n=================\nSemana 5:")
too_much_screen_time([1, 2, 3, 10, 2, 1, 0]) # True.

print("\n=================\nSemana 6:")
too_much_screen_time([3, 3, 5, 8, 8, 9, 4]) # True.

print("\n=================\nSemana 7:")
too_much_screen_time([3, 9, 4, 8, 5, 7, 6]) # True.