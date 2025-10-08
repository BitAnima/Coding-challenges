"""2nd Largest
Given an array, return the second largest distinct number."""

def second_largest(arr):
    arrays_ordered_list = []

    for num in arr:
        arrays_ordered_list.append(num)

    arrays_ordered_set = sorted(set(arrays_ordered_list))
    print(arrays_ordered_set[-2])


    return arrays_ordered_set[-2]

    ""Solución de copilot: def second_largest(arr):
        unique_sorted = sorted(set(arr))
        if len(unique_sorted) < 2:
            return None  # o lanza una excepción si prefieres
        return unique_sorted[-2]
    ""

second_largest([1, 2, 3, 4]) # 3.
second_largest([20, 139, 94, 67, 31]) # 94.
second_largest([2, 3, 4, 6, 6]) # 4.
second_largest([10, -17, 55.5, 44, 91, 0]) # 55.5.
second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]) # 0.