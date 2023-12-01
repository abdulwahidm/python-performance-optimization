# main.py

import requests
from linear_search import search_product_by_id_linear
from binary_search import search_product_by_id_binary
from linear_search import Product

# Fungsi untuk mendapatkan data produk dari API
def get_product_data_from_api():
    url = "https://jsonplaceholder.typicode.com/photos"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return []

# Fungsi untuk mengubah data dari API menjadi objek Product
def convert_api_data_to_products(api_data):
    return [Product(item['id'], item['title'], item['url']) for item in api_data]

# Mendapatkan data produk dari API
api_data = get_product_data_from_api()

# Convert data API menjadi objek Product
product_catalog = convert_api_data_to_products(api_data)

# Contoh pencarian produk dengan ID tertentu menggunakan Linear Search
target_product_id = 1502
found_product_linear, time_linear = search_product_by_id_linear(product_catalog, target_product_id)

if found_product_linear:
    print(f"Linear Search: Produk dengan ID {target_product_id} ditemukan: {found_product_linear.name}")
    print(f"Waktu yang dibutuhkan: {time_linear} detik")
else:
    print(f"Linear Search: Produk dengan ID {target_product_id} tidak ditemukan.")
    print(f"Waktu yang dibutuhkan: {time_linear} detik")

# Contoh pencarian produk dengan ID tertentu menggunakan Binary Search
found_product_binary, time_binary = search_product_by_id_binary(product_catalog, target_product_id)

if found_product_binary:
    print(f"\nBinary Search: Produk dengan ID {target_product_id} ditemukan: {found_product_binary.name}")
    print(f"Waktu yang dibutuhkan: {time_binary} detik")
else:
    print(f"\nBinary Search: Produk dengan ID {target_product_id} tidak ditemukan.")
    print(f"Waktu yang dibutuhkan: {time_binary} detik")
