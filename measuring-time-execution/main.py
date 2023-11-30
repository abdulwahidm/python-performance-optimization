import time

print("\nHello...\n")

def long_time():
    x = 0
    for j in range(0, 1_000):
        for i in range(0, 1_000):
            x += 1
    return x        

start = time.time()

long_time()

end = time.time()

print(long_time())

print(end - start)