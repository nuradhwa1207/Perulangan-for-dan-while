data_mahasiswa = {
    'mahasiswa1': {
        'nama': 'Nur Adhwa zahratul Aini',
        'usia': 18,
        'jurusan': 'Teknik Elektro'
    },
    'mahasiswa2': {
        'nama': 'Nur Annisa Ramadhani',
        'usia': 19,
        'jurusan': 'Matematika' 
    },
    'mahasiswa3': {
        'nama': 'Divana',
        'usia': 19,
        'jurusan': 'Teknik Lingkungan'
    }
}

# Mengakses data dalam nested dictionary
for mahasiswa, info in data_mahasiswa.items(): 
    data = f"{mahasiswa}: Nama: {info['nama']}, Usia: {info['usia']} tahun, Jurusan: {info['jurusan']}"
    print(data)