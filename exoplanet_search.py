"""Space Week Day 2: Exoplanet Search
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star.
Determine if the readings have detected an exoplanet using the transit method.
The transit method is when a planet passes in front of a star, reducing its observed luminosity.

Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
Characters 0-9 correspond to luminosity levels 0-9.
Characters A-Z correspond to luminosity levels 10-35.
A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings.
For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less."""

def has_exoplanet(readings):

    sum = 0
    values_list = []

    for character in readings:
        if character.isdigit():
            values_list.append(int(character))
            sum += int(character)
        else:
            value = ord(character) - 55 # El valor de ord('A') es 65, por lo que si se le restan 55 será 10
            values_list.append(value)
            # print(value)
            sum += value

    # print(sum)
    average = sum / len(readings)
    # print(average)

    eighty_percent_of_average = average * 0.80
    print(eighty_percent_of_average)

    for value in values_list:
        if value <= eighty_percent_of_average:
            print("True")
            return True
    print("False")
    return False


has_exoplanet("665544554") # False.
has_exoplanet("FGFFCFFGG") # True.
has_exoplanet("MONOPLONOMONPLNOMPNOMP") # False.
has_exoplanet("FREECODECAMP") # True.
has_exoplanet("9AB98AB9BC98A") # False.
has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") # True.