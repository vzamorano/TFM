import requests
import json
import re

BASE_URL = 'http://localhost:9200/logs/_search'
POST_URL = 'http://localhost:9200/suspicious/_doc'
regex = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}\sGET\s((\/about)|(\/services)|(\/guides)|(\/contents\/news)|(\/contents\/events)|(\/contents\/social-media)|(\/contact))\s[0-9]{3}'
pattern = re.compile(regex)
response = requests.get(BASE_URL)
if (int(response.status_code) == 200):
    print('Servidor funcionando correctamente.')
    json_response = response.json()
    quantity_of_data = json_response["hits"]["total"]["value"]
    quantity_integer = int(quantity_of_data)
    get_all_url = BASE_URL+f'?size={quantity_of_data}'
    response_all = requests.get(get_all_url)
    json_response_all = response_all.json()
    headers = {
      'Content-Type': 'application/json'
    }
    for number in range(quantity_integer):
        message = json_response_all["hits"]["hits"][number]["_source"]["message"][1]
        question = pattern.match(message)
        if (question is None):
            split_message = message.split()
            payload = '''
                {
                    "mensaje_sospechoso":"%s",
                    "recurso":"%s"
                }
            ''' % (message,split_message[2])
            response_post = requests.post(url = POST_URL, headers = headers, data = payload)
            if (int(response_post.status_code == 201)):
                print('Documento creado Exitosamente')
else:
    print('Servidor no se encuentra funcionando.')