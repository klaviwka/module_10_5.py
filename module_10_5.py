import time
from multiprocessing import Pool

def read_info(name):
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for file_name in filenames:
        read_info(file_name)
    linear_duration = time.time() - start_time
    print(f"{linear_duration:.6f} (линейный)")

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_duration = time.time() - start_time
    print(f"{multiprocessing_duration:.6f} (многопроцессный)")
