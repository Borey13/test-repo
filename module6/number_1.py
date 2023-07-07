import time
import threading


def get_thread(name_thread):
    time.sleep(1)
    print(f'Поток {name_thread} ')


threads = [threading.Thread(target=get_thread, args=(i + 1,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
