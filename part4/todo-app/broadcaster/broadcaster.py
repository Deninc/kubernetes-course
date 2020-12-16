import os
import requests
import asyncio
import json
from nats.aio.client import Client as NATS

def telegram_bot_sendtext(bot_message):
    bot_token = os.environ["TOKEN"]
    bot_chatID = os.environ["CHAT_ID"]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

async def run(loop):
    nc = NATS()

    await nc.connect(os.environ["NATS_URL"], loop=loop)

    async def message_handler(msg):
        d = json.loads(msg.data)
        print("message received:", d)
        if d["type"] == "inserted":
            m = f" *Todo task created:* {d['msg']}"
        else:
            m = f"*Todo task completed:* {d['msg']}"
        print("sending message to telegram:", m)
        telegram_bot_sendtext(m)

    await nc.subscribe("broadcaster", "workers", message_handler)
    print("Listening for broadcaster...")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()
    loop.close()
