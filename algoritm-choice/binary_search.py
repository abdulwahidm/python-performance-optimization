# binary_search.py

import time

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

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
