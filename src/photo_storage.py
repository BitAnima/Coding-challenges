"""
Photo Storage
Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB),
return the number of photos the hard drive can store using the following constraints:

1 gigabyte equals 1000 megabytes.
Return the number of whole photos the drive can store.
"""
import math


def number_of_photos(photo_size_mb, drive_size_gb):
    number_of_photos = math.floor((drive_size_gb / photo_size_mb) * 1000)
    """Para que el resultado se devuelva el número entero más pequeño que no exceda la capacidad,
     lo ideal es usar math.floor() en lugar de round(). Esto garantiza que nunca se cuente una foto que no cabe completamente."""

    return print(f"{number_of_photos}")

number_of_photos(1, 1) # 1000.
number_of_photos(2, 1) # 500.
number_of_photos(4, 256) # 64000.
number_of_photos(3.5, 750) # 214285.
number_of_photos(3.5, 5.5) # 1571.
