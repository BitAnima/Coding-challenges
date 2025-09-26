"""Caught Speeding
Given an array of numbers representing the speed at which vehicles were observed traveling,
and a number representing the speed limit, return an array with two items,
the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0]."""

def speeding(speeds, limit):

    vehicles_speeding = 0
    vehicles_speed_beyond_limit = []
    sum_speed_beyond_limit = 0

    for i, vehicle_speed in enumerate(speeds):
        if vehicle_speed > limit:
            print(f"Vehicle speed {i+1} is too high ({vehicle_speed})")
            vehicles_speeding += 1
            vehicle_speed_beyond_limit = vehicle_speed - limit
            print(
            f"Number of vehicles speeding: {vehicles_speeding}; Vehicle speed beyond limit: {vehicle_speed_beyond_limit}")
            vehicles_speed_beyond_limit.append(vehicle_speed_beyond_limit)
        else:
            print(f"Vehicle speed {i+1} within speed limit.")


    for exceeding_speed in vehicles_speed_beyond_limit:
        sum_speed_beyond_limit += exceeding_speed

    if vehicles_speeding == 0:
        print("No vehicles speeding")
        result = [0, 0]
        print(result)
    else:
        print(f"Sum of exceeding_speed: {sum_speed_beyond_limit}")
        average_beyond_speed_limit = sum_speed_beyond_limit/vehicles_speeding
        print(f"Average exceeding_speed: {average_beyond_speed_limit}")
        result = [vehicles_speeding, average_beyond_speed_limit]
        print(result)

    return result

speeding([50, 60, 55], 60) # [0, 0].
speeding([58, 50, 60, 55], 55) # [2, 4].
speeding([61, 81, 74, 88, 65, 71, 68], 70) # [4, 8.5].
speeding([100, 105, 95, 102], 100) # [2, 3.5].
speeding([40, 45, 44, 50, 112, 39], 55) # [1, 57].