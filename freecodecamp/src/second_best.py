"""
Second Best
Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

The second most expensive laptop if it is within your budget, or
The most expensive laptop that is within your budget, or
0 if no laptops are within your budget.
Duplicate prices should be ignored.
"""

def get_laptop_cost(laptops, budget):
  
  print(f"\nDatos originales:\n- Precios: {laptops}\n- Presupuesto: {budget}")
  lista_precios_ordenada = sorted(set(laptops))
  print(f"Lista de precios ordenada: {lista_precios_ordenada}")
  
  precios_filtrados = sorted({price for price in laptops if price <= budget}, reverse=True)
  print(f"El precio de los productos que puedes permitirte es: {precios_filtrados}")
  

  result = 0
  
  if all(price > budget for price in laptops): #0 if no laptops are within your budget
        result = 0
        print(f"No puedes permitirte ninguno de estos productos")
        return result
  
  elif any(price > budget for price in laptops): #The most expensive laptop that is within your budget
       result = precios_filtrados[0]
       print(f"El precio del producto que puedes comprar es: {result}")
       return result
  
  if lista_precios_ordenada[1] <= budget: #The second most expensive laptop if it is within your budget
        result = precios_filtrados[1]
        print(f"El precio del producto que puedes comprar es: {result}")
        return result

  #return laptops

get_laptop_cost([1500, 2000, 1800, 1400], 1900) # 1800
get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900) # 1800
get_laptop_cost([2099, 1599, 1899, 1499], 2200) # 1899
get_laptop_cost([2099, 1599, 1899, 1499], 1000) # 0
get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450) # 1400