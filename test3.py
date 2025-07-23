import requests
def send_to_telebot():
    bot_token = '8021793572:AAHgJru99rMWEVLeHSq_aFx4WDvtQFhMwfM'
    chat_id = '731248346'
    message = 'Мое сообщение'
    requests.get(f'https://api.teltegram.org/bot{bot_token}/sendMessage&cgat_id={chat_id}&text={message}')
