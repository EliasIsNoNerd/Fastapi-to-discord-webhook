import requests

r = requests.post('http://127.0.0.1:3933/webhook-discord', params={'message': 'MESSAGE HERE'},)
