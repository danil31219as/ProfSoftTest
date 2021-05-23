def sort_list(array: list) -> None:
    for i in range(len(array)):
        min_i = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_i]:
                min_i = j
        array[min_i], array[i] = array[i], array[min_i]


a = [5, 8, 2, 11, 6, 1, 10]
sort_list(a)
print(a)