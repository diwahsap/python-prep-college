# selection sort
number = list(map(int, input("Masukkan angka: ").split()))
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
print(number)