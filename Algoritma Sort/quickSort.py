# quick sort
# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as the pivot
    pivot = array[high]

    # pointer for greater elemnts
    i = low - 1

    # traverse through the array
    # compare each element with the pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot, increment i
            i += 1
            # swap the elements
            array[i], array[j] = array[j], array[i]

    # swap the pivot with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # return the position from where partition is done
    return i + 1

# function to perform quick sort
def quickSort(array, low, high):
    if low < high:
        # partition the array
        pi = partition(array, low, high)

        # sort the left side
        quickSort(array, low, pi - 1)

        # sort the right side
        quickSort(array, pi + 1, high)

data = [99, 56, 42, 87, 63, 79, 28, 42, 33, 12, 84]
print('Quick Sort')
print('Data awal: ', data)
size = len(data)
quickSort(data, 0, size - 1)
print('Data setelah diurutkan: ', data)