import telebot
import requests
from requests import get
import time

while True:
    r = requests.get('https://api.covalenthq.com/v1/137/address/0xd7bf5ee56759a13361191b4ab67b1c62f4c3251b/balances_v2/', auth=('ckey_752419bd5332448ca4c0322dc88', ''))
    q=r.json()

    datalist=q["data"]["items"]

    SICKLE_BALANCE = int([x['balance'] for x in datalist if x['contract_ticker_symbol'] == 'SICKLE'][0])
    WMATIC_BALANCE = int([x['balance'] for x in datalist if x['contract_ticker_symbol'] == 'WMATIC'][0])
    MATIC_QUOTE = ([x['quote_rate'] for x in datalist if x['contract_ticker_symbol'] == 'MATIC'][0])

    SICKLE_PRICE = WMATIC_BALANCE/SICKLE_BALANCE
    SICKLE_PRICE_USD = SICKLE_PRICE*MATIC_QUOTE

    bot = telebot.TeleBot("1999986203:AAHUeWnkKPuRkDZmllttrktPfnDve5Eh3L0")

    @bot.message_handler(commands=['price'])
    def send_welcome(message):
        bot.reply_to(message, "Sickle Price is " + str("{:.2f}".format(SICKLE_PRICE)) + " SICKLE/WMATIC that is " + str("{:.2f}".format(SICKLE_PRICE_USD)) + " USD")
        

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    bot.polling()

    time.sleep(60)