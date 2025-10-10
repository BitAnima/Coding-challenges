"""Space Week Day 3: Phone Home
For day three of Space Week, you are given an array of numbers representing distances (in kilometers)
between yourself, satellites, and your home planet in a communication route.
Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

The first value in the array is the distance from your location to the first satellite.
Each subsequent value, except for the last, is the distance to the next satellite.
The last value in the array is the distance from the previous satellite to your home planet.
The message travels at 300,000 km/s.
Each satellite the message passes through adds a 0.5 second transmission delay.
Return a number rounded to 4 decimal places, with trailing zeros removed."""

def send_message(route):
    total_distance = 0
    satellites = len(route)-1

    for kms in route:
        total_distance += kms

    #print(total_distance)
    km_per_second = (total_distance / 300000) + (0.5 * satellites)
    formatted_km_per_second = f"{km_per_second:.4f}".rstrip('0').rstrip('.')
    """To remove trailing zeros. rstrip('0') elimina todos los ceros que están al final de la cadena.
    rstrip('.') elimina el punto decimal si (y solo si) el número terminó en punto después de quitar los ceros
    (por ejemplo, "2." se convierte en "2")."""

    print(formatted_km_per_second)


    return float(formatted_km_per_second)

send_message([300000, 300000]) # 2.5.
send_message([384400, 384400]) # 3.0627.
send_message([54600000, 54600000]) # 364.5.
send_message([1000000, 500000000, 1000000]) # 1674.3333.
send_message([10000, 21339, 50000, 31243, 10000]) # 2.4086.
send_message([802101, 725994, 112808, 3625770, 481239]) # 21.1597.