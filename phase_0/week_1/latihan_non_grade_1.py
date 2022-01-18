#soal latihan non grade 1 week 1

'''
- Buatlah sebuah list dengan value berupa:
numbers = [951, 402, 984, 651, 360, 69, 408,
319, 601, 485, 980, 507, 725, 547, 544, 615,
83, 165, 141, 501, 263, 617, 865, 575, 219,
390, 984, 592, 236, 105, 942, 941, 386, 462,
47, 418, 907, 344, 236, 375, 823, 566, 597,
978, 328, 615, 953, 345, 399, 162, 758, 219,
918, 237, 412, 566, 826, 248, 866, 950, 626,
949]
- Loop dan print semua angka genap dari list angka diatas
dengan urutan yang sama.
- Jangan mencetak angka apapun yang muncul setelah angka
918 berdasarkan posisi angka tersebut pada list diatas.
- Tampilkan pesan ”Done” setelah looping berakhir.

'''



numbers = [951, 402, 984, 651, 360, 69, 408,
319, 601, 485, 980, 507, 725, 547, 544, 615,
83, 165, 141, 501, 263, 617, 865, 575, 219,
390, 984, 592, 236, 105, 942, 941, 386, 462,
47, 418, 907, 344, 236, 375, 823, 566, 597,
978, 328, 615, 953, 345, 399, 162, 758, 219,
918, 237, 412, 566, 826, 248, 866, 950, 626,
949]


print("Angka Genap : ")
for angka in numbers:
    if angka % 2 == 0: #hanya mencetak angka genap
        if angka == 918:
            break
        print(angka)
print("Done")