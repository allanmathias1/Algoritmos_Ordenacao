def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Exemplo de uso
unsorted = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(unsorted))
