import threading
import time
import requests


def get_html(link):
    response = requests.get(link)
    print(link, response)


links = ['https://www.foreca.ru', 'https://www.google.com', 'https://www.youtube.com',
         'https://brunoyam.com', 'https://yandex.ru']

start_time = time.time()

for link in links:
    get_html(link)

print(f'Время выполнения последовательного вызова функции {time.time() - start_time}')
print('===================================================================')

start_time = time.time()

threads = [threading.Thread(target=get_html, args=(link,)) for link in links]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f'Время выполнения параллельного вызова функции {time.time() - start_time}')
