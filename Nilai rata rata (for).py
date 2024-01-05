# Misalkan kita memiliki data nilai siswa dalam bentuk nested list sebagai berikut:
data_nilai = [
    [ "John", 80, 85, 90],
    ["Jane", 70, 75, 80],
    ["Tom", 90, 85, 95]
]

#Menghitung nilai rata-rata setiap siswa
for siswa in data_nilai:
    total_nilai = 0
    for nilai in siswa[1:]:
        total_nilai += nilai
    rata_rata = total_nilai / (len(siswa) - 1)

for nama, rata_rata in Rata_rata_nilai.items():
    print(f"Rata-rata nilai {siswa[0]}: {rata_rata}")