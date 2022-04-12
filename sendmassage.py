import requests 

token = '5192716609:AAE6aU1jJNXxSXdle7oWTZTiRS2pb-JW9U8'
chat_id = '@DWDWDWAS'
text = 'TEST from PY'

def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    
    req = requests.post(method, data = {
                                        'chat_id': chat_id,
                                        'text': text})
    
sendTelegram()