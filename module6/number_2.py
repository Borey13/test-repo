import time
import threading


def get_thread(name_thread):
    time.sleep(1)
    print(f'Поток {name_thread}')


start_time = time.time()

for i in range(5):
    get_thread(i + 1)

print(f'Время выполнения последовательного вызова функции {time.time() - start_time}')

print('====================================================================')

start_time = time.time()

threads = [threading.Thread(target=get_thread, args=(i + 1,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f'Время выполнения параллельного вызова функции {time.time() - start_time}')
