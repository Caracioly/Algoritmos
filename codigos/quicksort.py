def quickSort(array):
    if len(array) < 2:
        return array
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quickSort(menores) + [pivo] + quickSort(maiores)


print(f"quicksort: {quickSort([33, 15, 10, 5, 2, 3])}")
