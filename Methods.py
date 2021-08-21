# 1. Делает http-запрос любого типа без параметра method
import requests

response = requests.get(
    'https://playground.learnqa.ru/ajax/api/compare_query_type')  # запрос любого типа без передачи параметра method

print(response.status_code)
print(response.text)

# 2. Делает http-запрос не из списка. Например, HEAD.
import requests

response = requests.head(
    'https://playground.learnqa.ru/ajax/api/compare_query_type')  # запрос любого типа без передачи параметра method

print(response.status_code)
print(response.text)

# 3. Делает запрос с правильным значением method
import requests

response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type',
                        params={"method": "GET"})  # запрос любого типа без передачи параметра method

print(response.status_code)
print(response.text)

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
import requests

all_methods = [{"method": "GET"}, {"method": "PUT"}, {"method": "POST"}, {"method": "DELETE"}]

for method in all_methods:
    print('Проверка', method)
    response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params=method)
    print('GET\n', response.text)
    response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data=method)
    print('POST\n', response.text)
    response = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data=method)
    print('PUT\n', response.text)
    response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data=method)
    print('DELETE\n', response.text)
