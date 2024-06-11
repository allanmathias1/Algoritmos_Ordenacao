def counting_sort_for_radix(array, exp):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = array[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = array[i] // exp
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        array[i] = output[i]

def radix_sort(array):
    max_val = max(array)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(array, exp)
        exp *= 10

    return array

# Exemplo de uso
unsorted = [170, 45, 75, 90, 802, 24, 2, 66]
print("Sorted array:", radix_sort(unsorted))