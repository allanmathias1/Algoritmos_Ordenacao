def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Exemplo de uso
unsorted = [64, 25, 12, 22, 11]
print("Sorted array:", selectionSort(unsorted))
