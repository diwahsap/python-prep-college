# selection sort
def selectionSort(number):
    for i in range(len(number)):
        # cari elemen terkecil di list
        imin = i # dianggap elemen terkecil
        for j in range(i+1, len(number)):
            if number[j] < number[imin]:
                imin = j
        # tukar elemen terkecil dengan elemen pertama
        temp = number[i]
        number[i] = number[imin]
        number[imin] = temp
    return number

# cetak
data = [99, 56, 42, 87, 63, 79, 28, 42, 33, 12, 84]
print('Selection Sort')
print('Data awal: ', data)
selectionSort(data)
print('Data setelah diurutkan: ', data)