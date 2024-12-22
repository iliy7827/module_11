import requests
from pprint import pprint

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

"""
Использование модуля requests.
Получить данные о курсах валют с сайта на текущую дату и записать 
полученные данные в переменную r в формате json.
"""

r = requests.get(URL)
json_flag = False
if r.ok:
    try:
        r = r.json()
    except requests.exceptions.JSONDecodeError as e:
        print('Содержимое ответа не в формате json.', 'От источника был получен следующий ответ:',
              r, sep='\n')
    else:
        json_flag = True
pprint(r['Valute'])