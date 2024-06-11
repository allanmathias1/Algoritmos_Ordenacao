def bucket_sort(array):
    if len(array) == 0:
        return array

    min_val = min(array)
    max_val = max(array)
    bucket_range = (max_val - min_val) / len(array)

    buckets = [[] for _ in range(len(array))]

    for num in array:
        index = int((num - min_val) / bucket_range)
        if index == len(array):  # Tratar o caso do valor máximo
            index -= 1
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Exemplo de uso
unsorted = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Sorted array:", bucket_sort(unsorted))
