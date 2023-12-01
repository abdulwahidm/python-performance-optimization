# Contoh penggunaan algoritma pencarian dalam proyek e-commerce

import time

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

# Misalkan kita memiliki katalog produk dalam bentuk daftar
product_catalog = [
    Product(1001, "Laptop", 1200),
    Product(1502, "Smartphone", 800),
    Product(2005, "Headphones", 150),
    # ... (daftar produk lainnya)
]

def search_product_by_id_linear(arr, target_id):
    # Implementasi linear search
    start_time = time.time()

    for product in arr:
        if product.product_id == target_id:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return product, elapsed_time

    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, elapsed_time

def search_product_by_id_binary(arr, target_id):
    # Implementasi binary search
    start_time = time.time()

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_product = arr[mid]

        if mid_product.product_id == target_id:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return mid_product, elapsed_time
        elif mid_product.product_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    return None, elapsed_time

# Contoh pencarian produk dengan ID tertentu menggunakan Linear Search
target_product_id = 1502
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
  