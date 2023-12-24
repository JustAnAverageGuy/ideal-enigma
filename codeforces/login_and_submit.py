#!/bin/python3
import argparse
import json
import re
import requests
import time

from pathlib import Path
from requests.cookies import RequestsCookieJar  # For some reason, without this, pylance screams that "cookies is not a known member of requests"
from Crypto.Cipher import AES
from bs4 import BeautifulSoup

CODEFORCES_DOMAIN = "https://codeforces.com"
DEBUG = False
CONFIG_FILE_PATH = "./.config.json"
config = dict()

me = requests.Session()
csrf = ""
handle = ""
password = ""
cookie_jar = RequestsCookieJar()
is_logged_in = False

me.cookies = cookie_jar
me.headers = {
    "user-agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def load_config(config_file_path=CONFIG_FILE_PATH):
    global config
    try:
        with open(config_file_path) as f:
            config = json.load(f)
            if DEBUG: print(f"[INFO] Loaded config from {config_file_path}")
    except FileNotFoundError as e:
        if DEBUG:
            print(
                f'[INFO] config file not found at {config_file_path}, triggering error {e}, loading default config'
            )
        config = {
            "handle": "username",
            "password": "password",
            "cookie": dict()
        }

    if "cookie" not in config: config["cookie"] = dict()


def save_config(config_file_path=CONFIG_FILE_PATH):
    global config
    with open(config_file_path, "w") as f:
        json.dump(config, f)
        if DEBUG: print(f"[INFO] Saved config to {config_file_path}")


def check_relogin():
    if DEBUG: print(f'[INFO] Checking if it is required to re_login')
    if is_logged_in: return False
    if "cookie" not in config: return True
    if not all((i in config["cookie"])
               for i in ["csrf", "JSESSIONID", "39ce7", "rcpc"]):
        return True
    t = float(config["cookie"]["expire"])
    return t < time.time()


def reload_cookies():
    if DEBUG: print(f'[INFO] Loading cookies 🍪')
    cookies = config["cookie"]
    for k, val in cookies.items():
        cookie_jar.set(k, val)
    # pretty sure this is unnecessary, but will see TODO: Refactor?
    me.cookies.update({
        "39ce7": config["cookie"]["39ce7"],
        "JSESSIONID": config["cookie"]["JSESSIONID"],
        "RCPC": config["cookie"]["rcpc"],
    })
    global csrf
    csrf = config["cookie"]["rcpc"]


def get_parameter(inp):
    key, iv, cipher = [None] * 3

    mat = re.match(r'(?<=a=toNUmbers\(")\w+(?="\))', inp)
    if mat is not None: key = mat.group()

    mat = re.match(r'(?<=b=toNUmbers\(")\w+(?="\))', inp)
    if mat is not None: iv = mat.group()

    mat = re.match(r'(?<=c=toNUmbers\(")\w+(?="\))', inp)
    if mat is not None: cipher = mat.group()

    if not all([key, iv, cipher]):
        raise ValueError(
            f"Regex didn't match in `get_parameter` {('for input= '+repr(inp)) if DEBUG else ''}"
        )
    return cipher, key, iv


def decrypter_RCPC(ocipher, okey, oiv):
    key = bytes.fromhex(okey)
    iv = bytes.fromhex(oiv)
    cipher = bytes.fromhex(ocipher)

    return AES.new(key, AES.MODE_CBC, iv).decrypt(cipher).hex()


def get_csrf(path):
    if DEBUG: print(f'[INFO] Getting csrf token for {path=}')
    res = me.get(path)
    c__srf = BeautifulSoup(res.text, 'html.parser').select_one(".csrf-token")
    if "cookie" not in config: config["cookie"] = dict()
    if c__srf:
        global csrf
        csrf = c__srf["data-csrf"]
        config["cookie"]["csrf"] = csrf


def get_rcpc():
    if DEBUG: print(f'[INFO] Getting RCPC')
    res = me.get(CODEFORCES_DOMAIN + "/enter")
    if len(res.text) > 800: return "", False
    if DEBUG: print(f'[INFO] Found RCPC')
    return decrypter_RCPC(*get_parameter(res.text)), True


def re_login():
    global csrf
    if DEBUG: print(f'[INFO] `re_login` was called')
    handle = config["handle"]
    password = config["password"]
    rcpc, does_rcpc_exist = get_rcpc()
    if does_rcpc_exist:
        config["cookie"]["rcpc"] = rcpc
        me.cookies.set("RCPC", rcpc)
    get_csrf(CODEFORCES_DOMAIN + "/enter")
    me.post(CODEFORCES_DOMAIN + '/enter?back',
            data={
                "action": "enter",
                "handleOrEmail": handle,
                "password": password,
                "remember": "on",
                "csrf_token": csrf,
            })
    for ke, val in cookie_jar.items():
        me.cookies.set(ke, val)
        config['cookie'][ke] = val
    config["cookie"]["expire"] = time.time() + 86400
    get_csrf(CODEFORCES_DOMAIN)
    save_config()


def login():
    load_config()
    if check_relogin():
        re_login()
        global is_logged_in
        is_logged_in = True
    else:
        reload_cookies()


def manually_login():
    load_config()
    re_login()


def is_gym(contest_id):
    return len(contest_id) >= 6


def submit_code(contest, index, code, programTypeID):
    login()
    path = f'{CODEFORCES_DOMAIN}/gym/{contest}/submit?csrf_token={csrf}' if is_gym(
        contest
    ) else f'{CODEFORCES_DOMAIN}/contest/{contest}/submit?csrf_token={csrf}'

    me.post(path,
            data={
                "csrf_token": csrf,
                "action": "submitSolutionFormSubmitted",
                "contestId": contest,
                "submittedProblemIndex": index,
                "programTypeId": programTypeID,
                "source": code,
                "tabSize": "4",
            })


def main():

    parser = argparse.ArgumentParser(
        description="Submit a soultion to codeforces")
    parser.add_argument(
        "solution_file_path",
        help="Path to the file containing the solution to be submitted")

    parser.add_argument("problem_code",
                        help="problem index, like 1969D, or like 1869F1")

    parser.add_argument("-D",
                        "--DEBUG",
                        action="store_true",
                        help="Turn on DEBUG output")

    parser.add_argument(
        "--lang_ID",
        default="70",
        help=
        "Language ID of the language of submission, default=70, corresponding to PyPy3.9 64 bit"
    )

    parser.add_argument("--config-path",
                        default=r"./.config.json",
                        help="Path to the config file, default=%(default)s")

    args = parser.parse_args()

    with open(Path(args.solution_file_path).expanduser()) as f:
        cod = f.read()

    mat = re.match(r'(\d+)([A-Za-z0-9]+)', args.problem_code)
    if mat is not None: contest_id, problem_index = mat.groups()
    else:
        raise ValueError(
            "`problem_code` is invalid, unable to extract contest_ID, problem_index"
        )

    global DEBUG
    DEBUG = True if args.DEBUG is not None else DEBUG

    global CONFIG_FILE_PATH
    CONFIG_FILE_PATH = Path(args.config_path).expanduser()
    submit_code(contest_id, problem_index, cod, args.lang_ID)


main()

# "Language_ID": Language Name

# "43": GNU GCC C11 5.1.0
# "80": Clang++20 Diagnostics
# "52": Clang++17 Diagnostics
# "50": GNU G++14 6.4.0
# "54": GNU G++17 7.3.0
# "73": GNU G++20 11.2.0 (64 bit, winlibs)
# "59": Microsoft Visual C++ 2017
# "61": GNU G++17 9.2.0 (64 bit, msys 2)
# "65": C# 8, .NET Core 3.1
# "79": C# 10, .NET SDK 6.0
# "9": C# Mono 6.8
# "28": D DMD32 v2.091.0
# "32": Go 1.19
# "12": Haskell GHC 8.10.1
# "60": Java 11.0.6
# "74": Java 17 64bit
# "36": Java 1.8.0_241
# "77": Kotlin 1.6.10
# "83": Kotlin 1.7.20
# "19": OCaml 4.02.1
# "3": Delphi 7
# "4": Free Pascal 3.0.2
# "51": PascalABC.NET 3.4.2
# "13": Perl 5.20.1
# "6": PHP 8.1.7
# "7": Python 2.7.18
# "31": Python 3.8.10
# "40": PyPy 2.7.13 (7.3.0)
# "41": PyPy 3.6.9 (7.3.0)
# "70": PyPy 3.9.10 (7.3.9, 64bit)
# "67": Ruby 3.0.0
# "75": Rust 1.65.0 (2021)
# "20": Scala 2.12.8
# "34": JavaScript V8 4.8.0
# "55": Node.js 12.16.3
# "14": ActiveTcl 8.5
# "15": Io-2008-01-07 (Win32)
# "17": Pike 7.8
# "18": Befunge
# "22": OpenCobol 1.0
# "25": Factor
# "26": Secret_171
# "27": Roco
# "33": Ada GNAT 4
# "38": Mysterious Language
# "39": FALSE
# "44": Picat 0.9
# "45": GNU C++11 5 ZIP
# "46": Java 8 ZIP
# "47": J
# "56": Microsoft Q#
# "57": Text
# "62": UnknownX
# "68": Secret 2021
