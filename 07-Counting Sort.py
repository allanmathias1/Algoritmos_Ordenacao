def counting_sort(array):
    max_val = max(array)
    m = max_val + 1
    count = [0] * m

    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array

# Exemplo de uso
unsorted = [4, 2, 2, 8, 3, 3, 1]
print("Sorted array:", counting_sort(unsorted))
