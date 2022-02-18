# bubble sort
number = list(map(int, input("Masukkan angka: ").split()))
for i in range(len(number)):
    for j in range(len(number) - 1):
        if number[j] > number[j+1]:
            # tukar number[j] dengan number[j+1]
            temp = number[j]
            number[j] = number[j+1]
            number[j+1] = temp
print(number)