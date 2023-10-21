import time
from colorama import init
from termcolor import colored 
import data
import os
from telethon import TelegramClient, events, sync

init()

green = "green"
cyan = "cyan"
red = "red"
magenta = "magenta"
white = "white"

api_id = data.api_id
api_hash = f'{data.api_hash}'
username = data.username


print(colored("===", magenta), colored("DC$ boomber ", cyan), colored("===", magenta))
print()
print(colored("[1]", red), colored("Auth", green))
print(colored("[2]", red), colored("Attack to username", green))
print(colored("[3]", red), colored("Attack range 1000", green))
print()
print(colored("===", magenta), colored("by T958 v23.1", green), colored("===", magenta))

while True: 
    commands = input("$ ")
    if commands == '1':
        id = input('$ your api id: ')
        api = input('$ your api hash: ')
        username = input('$ @username for attack: ')
        with open("data.py", "w") as f:
            f.write(f"api_id = {id}\napi_hash = '{api}'\nusername = '{username}'")
        print(colored("Successfully!", white))

    elif commands == '2':
        print(colored("Amaterasu!", cyan), colored("==", magenta))
        os.system('python3 dcs.py')

    elif commands == '3':
            @client.on(events.NewMessage)
            async def my_event_handler(event):
                if 'attack' in event.raw_text:
                    for attack in range(1000):
                        print(colored("Amaterasu!", cyan), colored("==", magenta), attack)
                        await client.send_message(f"@{username}", "Belissimo code: 101010101", attack)

