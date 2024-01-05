
# Contoh data penjualan
data_penjualan = {
    'Toko A': {
        'Produk X': [100, 120, 130],
        'Produk Y': [50, 60, 70],
    },
    'Toko B': {
        'Produk X': [80, 90, 100],
        'Produk Y': [30, 40, 50],
    },
}

# Mengakses data dalam nested dictionary
for Toko, info in data_penjualan.items():
    print(f"Toko {Toko}: Produk X: {info['Produk X']}, Produk Y: {info['Produk Y']}")
