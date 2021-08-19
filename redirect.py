import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect')

last_response = response.history[-1]
response_count = len(response.history)

print('Количество редиректов:', response_count)
print('Итоговый URL:', last_response.url)
