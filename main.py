import requests
from src import config

def sendSMS(target_numbers,msgBody):
    payload = 'sender_id=FSTSMS&message='+msgBody+\
              '&language=english&route=p&numbers='\
              +target_numbers

    response=requests.request(method='POST',url=config.fastUrl,data=payload,headers=config.defaultHeaders)
    if(response.ok):
        print('Text message sent successfully')
    else:
        print('Failed to send the message')



if(__name__=='__main__'):
    mobNum=input('Please enter the mobile number\n')
    text=input('Enter the SMS Body\n')
    sendSMS(target_numbers=mobNum,msgBody=text)