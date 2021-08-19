import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
parsing_text = json.loads(json_text)
key = 'messages'
if key in parsing_text:
    message = parsing_text[key]
    print(message[1])
else:
    print(f"Ключа {key} в JSON нет")