import serial
import json
import os
import openai
import requests
import subprocess
import socket
import datetime
import getpass
import time
from dotenv import load_dotenv
load_dotenv()

hostname = socket.gethostname()
local_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
ip_address = socket.gethostbyname(hostname)
username = getpass.getuser()
info_string = f'\n\rHostname: {hostname}\n\rLocal Time: {local_time}\n\rIP Address: {ip_address}\n\rUsername: {username}'

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer "+os.getenv('OPENAIKEY')
}

serialPort = serial.Serial(
    port=os.getenv('COMINFO'),
    baudrate=9600,
    bytesize=8,
    timeout=2,
    stopbits=serial.STOPBITS_ONE,
    parity=serial.PARITY_EVEN
)

def print_colored_text(text, color):
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }
    reset_color = '\033[0m'
    colored_text = colors[color] + text + reset_color
    return colored_text

def print_menu():
    menu = print_colored_text("\r\r\nopenai>", "red")
    serialPort.write(menu.encode('ISO-8859-1'))

def handle_input(serialString):
    if serialString.startswith('!'):
        command = serialString[1:]
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output = result.stdout + result.stderr
        serialPort.write(output.encode('ISO-8859-1'))
        return True
    print(f"Received: {serialString}")
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": serialString}]
    }
    response = requests.post(url, headers=headers, json=data)
    cont = response.json()
    formcont = cont["choices"][0]["message"]["content"]
    print(f"Answre from AI: "+formcont)
    serialPort.write(formcont.encode('ascii', 'ignore'))
    return True



def read_input(serialPort):
    input = ''
    while True:
        if serialPort.in_waiting > 0:
            char = serialPort.read().decode('ascii', 'ignore')
            serialPort.write(char.encode('ascii', 'ignore'))
            if char == '\r':
                break
            input += char
    return input.strip()


def print_startup_text(serialPort):
    print("User Connected, sent intro.")
    startup_text = info_string
    serialPort.write(startup_text.encode('ISO-8859-1'))

def authenticate(serialPort):
    serialPort.write(b'\x1b[2J\n\rUsername: ')
    username = read_input(serialPort)
    serialPort.write(b'\n\rPassword: ')
    password = read_input(serialPort)

    if username == username and password == os.getenv('PASSWORD'):
        serialPort.write(b'\r\nWelcome!')
        return True
    else:
        serialPort.write(b'\r\nInvalid username or password.')
        time.sleep(5)
        return False

while not authenticate(serialPort):
    pass
print_startup_text(serialPort)
print_menu()
while 1:
    serialString = read_input(serialPort)
    if not handle_input(serialString):
        break
    print_menu()