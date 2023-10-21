from telethon import TelegramClient, events, sync
import data

api_id = data.api_id
api_hash = f'{data.api_hash}'
username = data.username

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'attack' in event.raw_text:
        for attack in range(1000):
            await client.send_message(f"@{username}", "Belissimo code: 101010101")

client.start()
client.run_until_disconnected()