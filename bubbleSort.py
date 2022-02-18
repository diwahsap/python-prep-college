# bubble sort
number = list(map(int, input("Masukkan angka: ").split()))
def bubbleSort(number):
    for i in range(len(number)):
        for j in range(len(number)):
            if number[j+1] < number[j]:
                # tukar number[j] dengan number[j+1]
                temp = number[j]
                number[j] = number[j+1]
                number[j+1] = temp
    return number
print(bubbleSort(number))
