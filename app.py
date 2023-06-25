from credentials import mobile_number
import requests 
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': "Good Morning",
        'key': 'textbelt'
    })
    print(resp.json())

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)






# 644417dcd20ef29dca57635cf7e23242