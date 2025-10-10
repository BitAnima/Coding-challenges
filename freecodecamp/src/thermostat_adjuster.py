def adjust_thermostat(temp, target):

    temp = float(temp)
    target = float (target)


    if temp < target:
        return 'heat'
    elif temp > target:
        return 'cool'
    else:
        return 'hold'
    
result = adjust_thermostat(68, 72) #"heat"
print(f"{result}")