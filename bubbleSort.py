# bubble sort
number = list(map(int, input("Masukkan angka: ").split()))
def bubbleSort(number):
    for i in range(len(number)):
        for j in range(len(number) - 1):
            if number[j] > number[j+1]:
                # tukar number[j] dengan number[j+1]
                number[j] = number[j+1]
                number[j+1] = number[j]
    return number
print(bubbleSort(number))
