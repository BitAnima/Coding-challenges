"""24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".
The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359"."""

def to_12(time: str = "2300"):

    hour= int(time[0:2])
    minutes= str(time[2:4])

    formatted_time = ""

    if hour == 0:
        formatted_time = f"12:{minutes} AM"
    elif hour < 12:
        formatted_time = f"{hour}:{str(minutes)} AM"
    else:
        formatted_time = f"{hour-12}:{str(minutes)} PM"

    print(formatted_time)

    return formatted_time

formatted_time = to_12()