from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    from telethon.sync import TelegramClient,events
    import configparser
    from telethon import utils

    #config = configparser.ConfigParser()
    #config.read("config-sample.ini")
    # Setting configuration values
    #api_id = config['Telegram']['api_id']
    #api_hash = config['Telegram']['api_hash']

    api_id='1586339'
    api_hash='52dcf6e77d0dab47c918261e7532d6b1'

    phone='+919324285477'
    username='subodh2604'

    api_hash = str(api_hash)

    #phone = config['Telegram']['phone']
    #username = config['Telegram']['username']

    with TelegramClient(username,api_id,api_hash) as client:
        messages=client.get_messages('https://t.me/botcurrent',limit=10000)
        print("messages no: ",len(messages))
        count=0
        required_files=0
        exception_count=0
        for msg in messages:
            count+=1
            try:
                pdf_name=msg.media.document.attributes[0].file_name
            except:
                exception_count+=1
                continue
            
            client.download_media(msg)
    
    #vivek info
    #api_id=1564169
    #api_hash=932f6545cdc73ab259a5cf3c0d9ef557

    #subodh info
    #api_id = 1586339
    #api_hash = 52dcf6e77d0dab47c918261e7532d6b1


    
    return HttpResponse("files downloading")
