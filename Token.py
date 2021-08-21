import requests
import time

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
print(response.text)

parsed_response = response.json()
new_response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=parsed_response)
print(new_response.text)

time.sleep(parsed_response["seconds"])
new_response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=parsed_response)
print(new_response.text)
