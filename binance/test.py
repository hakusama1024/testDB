from binance.client import Client
from binance.websockets import BinanceSocketManager
from time import sleep
import os

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']
client = Client(api_key, api_secret)

klines = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")
print(klines)


def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
                # do something

#bm = BinanceSocketManager(client)
#bm.start_trade_socket('BNBBTC', process_message)
#bm.start()
