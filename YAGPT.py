import requests
from consts import API_Key, Folder_ID, PROMPT #Импорт ключей и промпта для нейросети из файла
from func import clean_result

def load_tasks(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

#Промпты нейросети
def  get_response(history):
    prompt = {
        'modelUri':'gpt://'+Folder_ID+'/yandexgpt-lite/rc',
        'completionOptions':{
            'stream': False,
            'temperature': 0.6,
            'maxTokens':3000
            },

        'messages':[
            {'role' : 'system',
            'text' : PROMPT},
        ]
    }
    prompt['messages'].extend(history)
    url='https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    headers = {
        'Content-Type' : 'application/json',
        'Authorization': 'Api-Key '+API_Key
    }

    response = requests.post(url, headers=headers, json=prompt)
    result=response.text
    result=clean_result(result) #Использование функции clean_result для очистки текста нейросети от лишних символов
     
    return result
