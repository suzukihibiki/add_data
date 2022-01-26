import time
from memory_profiler import profile
@profile
def add_data():
    start = time.time()
    a = [i for i in range(100000)]
    print(a[-1])
    end = time.time()
    print(end - start)
add_data()