import requests
import threading
import os
import time
import ctypes
import colorama
from colorama import Fore

colorama.init()
os.system("cls")

questions = [f"Enter the target username {Fore.LIGHTBLACK_EX}>{Fore.WHITE} ", f"Enter the message to be spammed {Fore.LIGHTBLACK_EX}>{Fore.WHITE} ", f"Enter the number of messages you want to send {Fore.LIGHTBLACK_EX}>{Fore.WHITE} "]
data = []

for question in questions:
    data.append(input(question))
    os.system("cls")

print(f"Target -> {data[0]}\nMessage -> {data[1]}\nNumber of Messages -> {data[2]}\n")

print("Sending nuke...\n")

url = "https://ngl.link/api/submit"

payload = {
    "username" : data[0],
    "question" : data[1],
    'deviceId': 'a59dc5ef-63b8-4a16-97dd-e9c39a490795',
}

def spam():
    r = requests.post(url, data=payload)
    if r.status_code == 200:print("Sent Message!")
    else:print("Failure")


for i in range(int(data[-1])):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{i}/{data[-1]}")
    time.sleep(0.001)
    threading.Thread(target=spam).start()

