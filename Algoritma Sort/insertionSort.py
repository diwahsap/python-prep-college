# insertion sort
def insertionSort(number):
    for i in range(len(number)):
        # select value
        valueToInsert = number[i]
        holePosition = i

        # locate hole position for the element to be inserted
        while holePosition > 0 and number[holePosition - 1] > valueToInsert:
            number[holePosition] = number[holePosition - 1]
            holePosition -= 1

        # insert the number at hole position
        number[holePosition] = valueToInsert
    return number

# print the sorted list
data = [99, 56, 42, 87, 63, 79, 28, 42, 33, 12, 84]
print('Insertion Sort')
print('Data awal: ', data)
insertionSort(data)
print('Data setelah diurutkan: ', data)