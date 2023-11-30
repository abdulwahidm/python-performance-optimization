import cProfile

def contoh_fungsi():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Profilisasi fungsi_contoh
cProfile.run('contoh_fungsi()')


"""
Output yang dihasilkan oleh cProfile akan memberikan informasi terperinci 
tentang setiap fungsi dan panggilannya, beserta waktu eksekusi 
yang dihabiskan di dalamnya. Hasilnya mungkin terlihat seperti ini:

         4 function calls in 0.118 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.118    0.118    0.118    0.118 contoh.py:5(contoh_fungsi)
        1    0.000    0.000    0.118    0.118 {built-in method builtins.exec}
        1    0.000    0.000    0.118    0.118 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""