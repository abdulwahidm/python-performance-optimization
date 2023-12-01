# main.py

from linear_search import search_product_by_id_linear
from binary_search import search_product_by_id_binary
from linear_search import Product

# Misalkan kita memiliki katalog produk dalam bentuk daftar
product_catalog = [
    Product(1001, "Laptop", 1200),
    Product(1502, "Smartphone", 800),
    Product(2005, "Headphones", 150),
    # ... (daftar produk lainnya)
]

# Contoh pencarian produk dengan ID tertentu 
target_product_id = 1502

# Menggunakan Linear Search
found_product_linear, time_linear = search_product_by_id_linear(product_catalog, target_product_id)

if found_product_linear:
    print(f"Linear Search: Produk dengan ID {target_product_id} ditemukan: {found_product_linear.name} (Harga: ${found_product_linear.price})")
    print(f"Waktu yang dibutuhkan: {time_linear} detik")
else:
    print(f"Linear Search: Produk dengan ID {target_product_id} tidak ditemukan.")
    print(f"Waktu yang dibutuhkan: {time_linear} detik")

# Contoh pencarian produk dengan ID tertentu menggunakan Binary Search
found_product_binary, time_binary = search_product_by_id_binary(product_catalog, target_product_id)

if found_product_binary:
    print(f"\nBinary Search: Produk dengan ID {target_product_id} ditemukan: {found_product_binary.name} (Harga: ${found_product_binary.price})")
    print(f"Waktu yang dibutuhkan: {time_binary} detik")
else:
    print(f"\nBinary Search: Produk dengan ID {target_product_id} tidak ditemukan.")
    print(f"Waktu yang dibutuhkan: {time_binary} detik")
