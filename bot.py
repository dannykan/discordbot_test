import websocket, json, pprint

SOCKET = "wss://stream.binance.com:9443/ws/solusdt@kline_1m"

closes = []

def on_open(ws):
    print("opened connection")

def on_close(ws):
    print("closed connection")

# def on_error(ws):
#     print()

def on_message(ws, message):
    global closes
    print("received message")
    json_message = json.loads(message)
    pprint.pprint(json_message)
    
    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']
    
    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()