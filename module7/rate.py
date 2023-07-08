import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def add_date_and_rate(data):
    date_list = [str(data[i - 2])[6: -5] for i in range(len(data) - 1, 0, -3)]
    rate_list = [float(str(data[i - 1])[4: -5]) for i in range(len(data) - 1, 0, -3)]
    return date_list, rate_list


def graph_usd(data):
    date, rate = add_date_and_rate(data)
    plt.plot(date, rate)
    plt.xlabel('Дата')
    plt.ylabel('Рубли')
    plt.title('Курс USD')
    plt.xticks(rotation=90)
    plt.tick_params(axis='x', which='major', labelsize=7)
    plt.tight_layout()
    plt.show()


page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
rates = soup.find(class_='mfd-table mfd-currency-table')
only_data_rates = rates.find_all('td')
graph_usd(only_data_rates)
