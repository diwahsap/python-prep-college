# bubble sort
def bubbleSort(number):
    for i in range(len(number)):
        for j in range(len(number) - 1):
            if number[j] > number[j+1]:
                # tukar number[j] dengan number[j+1]
                temp = number[j]
                number[j] = number[j+1]
                number[j+1] = temp
    return number

# print
data = [99, 56, 42, 87, 63, 79, 28, 42, 33, 12, 84]
print('Bubble Sort')
print('Data awal: ', data)
bubbleSort(data)
print('Data setelah diurutkan: ', data)