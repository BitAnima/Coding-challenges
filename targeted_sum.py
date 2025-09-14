"""
Targeted Sum
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

The returned array should have the indices in ascending order."""

def find_target(arr, target):

    for i, element in enumerate(arr):
        #print(f"{i}, {element}")
        complemento = target - element
        for j, element2 in enumerate(arr):
            if i < j and element2==complemento: #i<j para evitar que se repita el resultado dos veces
                print(f"{element} + {complemento} = {target}")
                print(f"{i}, {j}")
                return [i, j]
    return 'Target not found'


        
"""elif any(price > budget for price in laptops): #The most expensive laptop that is within your budget
       result = precios_filtrados[0]
       print(f"El precio del producto que puedes comprar es: {result}")
       return result
"""
   

find_target([2, 7, 11, 15], 9) # [0, 1].
find_target([3, 2, 4, 5], 6) # [1, 2].
find_target([1, 3, 5, 6, 7, 8], 15) # [4, 5].
find_target([1, 3, 5, 7], 14) # 'Target not found'.