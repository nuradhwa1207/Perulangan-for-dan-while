# mencari nilai maksimum dari suatu daftar angka, a

def cari_nilai_maksimum(daftar_angka):
    # Inisialisasi nilai maksimum
    nilai_maksimum = daftar_angka[0]

    # Gunakan perulangan while untuk mencari nilai maksimum
    i = 1
    while i < len(daftar_angka):
        if daftar_angka[i] > nilai_maksimum:
            nilai_maksimum = daftar_angka[i]
        i += 1

    return nilai_maksimum

angka_list = [12, 45, 67, 89, 34, 56, 23]

hasil = cari_nilai_maksimum(angka_list)
print(f"Nilai maksimum dari daftar angka adalah: {hasil}")