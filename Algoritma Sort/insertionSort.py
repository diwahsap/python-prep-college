# selection sort
number = list(map(int, input("Masukkan angka: ").split()))
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

# print the sorted list
print(number)
