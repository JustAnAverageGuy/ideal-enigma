import json
import os
import sys
import requests
from pathlib import Path

# TODO: Can add submission feature: look for `submitEventQuestAnswer` in `main.*.js`



try:
    with open(os.path.join(os.path.dirname(__file__),".env")) as f: 
        COOKIE = json.load(f)["cookie"]
        # TODO: Add local option to use seed, so that you don't need to fetch it, 
        # Also maybe add an async method which fetches it in background and updates it if required
        # SEED   = json.load(f)["seed"]
except FileNotFoundError as e:
    print(f"Create A .env file in the directory {os.path.dirname(__file__)}",file=sys.stderr)
    print(f"The file should be a json file with a single object containing a key named cookie which is your session (?) cookie",file=sys.stderr)
    raise e


from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt(data: str, key: str):
    """
    Given a UTF-8 encoded key `key`, decodes hex encoded input `data`

    If this is not working properly, search for `decryptText` function in `main.*.js` file in the debug sources to see what changed 
    the library is most probably CryptoJS
    """

    r = [i for i in key]
    r[20] = '~'
    key_new = "".join(r).encode()

    ciph = AES.new(key_new, AES.MODE_CBC, iv=key_new[0:16])

    return unpad(ciph.decrypt(bytes.fromhex(data)), 16).decode()

s = requests.Session()

s.cookies.update(
    {
        "everybody-codes" : COOKIE,
    }
)

s.headers.update(
    {
        "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0", # On 05/11/2024
    }
)

ME = {}
BASE_URL = "https://everybody.codes"
CDN_URL = "https://everybody-codes.b-cdn.net"
KEYS = {} # KEYS[i] = {"1":..., "2":..., "3":...} # keys corresponding to day i # i is int

def get_my_config(force_refresh=False):
    """
    Returns user data available on server side, especially the `seed` value
    """
    global ME
    if (not ME) or force_refresh:
        res = s.get(f'{BASE_URL}/api/user/me')
        if not res: # TODO : This probably doesn't work as I expect
            raise Exception(f"Failed to get user config, result: {res}")
        ME =  res.json()
    return ME

def get_aes_keys(part:int, day:int, year:int, refresh = False):
    """
    Returns the utf-8 encoded key required to decode problem's part
    """
    # TODO: cache known keys on hardisk 
    global KEYS
    key = KEYS.get(day, {}).get(str(part), "")
    if (not key) or refresh:
        res = s.get(f'{BASE_URL}/api/event/{year}/quest/{day}')
        if not res: # TODO : This probably doesn't work as I expect
            raise Exception("Failed to get Key, look into ")
        got = {
            i[-1]:j  # only take the last character, since keys are only single digit, should probably put an assert for the same, but whatever
            for i,j  in res.json().items() 
            if i.startswith("key")
        } # ignore answers

        KEYS[day] = got
        if str(part) not in got: raise Exception(f"Part = {part} for day = {day} Not yet unlocked or something else failed")
        key = got[str(part)]
    return key



def get_input(part :int, day :int, year:int, force_use_this_seed:str|None = None, refresh_cache=False):

    """
    returns the input as utf-8 encoded string,
    for part `part` of day `day` of year `year`

    give the seed value manually as the `force_use_this_seed` parameter to utilize caching, was 28 for me on 19/11/2024

    Search for `getEventQuestInput` function in `main.*.js` in website sources
    """

    # TODO: alongside fetching input globally, save input in local folder as well, and then reuse that input without refetching anything
    # In fact, since this input is anyways aes encrypted, store plaintext input in local folders anyways after decrypting
    # TODO: Properly implement above idea, currently it is very crude

    LOCAL_CACHE_PATH = f".inp_{year}_{day}_{part}.txt"
    if os.path.exists(LOCAL_CACHE_PATH):
        print(f"LOCAL CACHE FOUND IN SAME DIRECTORY at {LOCAL_CACHE_PATH}\nmaybe older version\ndelete or rename file to refetch\n\n",file=sys.stderr)
        with open(LOCAL_CACHE_PATH) as f: 
            input = f.read()
        return input

    problem_seed = force_use_this_seed

    if not problem_seed:
        config = get_my_config()
        
        try:
            problem_seed = config["seed"]
        except KeyError as e:
            print(f"Can't find seed in server side user config (damn)",e)
            raise e


    # TODO: Fix this, hasn't caused any problems yet (19/11/2024), but now checking the version value being sent looks like a timestamp at which 
    # problem is being fetched, but in the ze.config, it is something like 17 (maybe problem dependent, idk)

    questsVersion = 6 # Search for `ze` in `main.*.js`, contains event config

    # TODO: add option to customise this

    input_cache_file_path = Path(os.path.dirname(__file__))/f"cache_inputs_encrypted"/f"{year}"/f'{day}'/f'{problem_seed}.json?v={questsVersion}' 

    if (not input_cache_file_path.exists()) or refresh_cache:
        print("REFETCHING INPUT",file=sys.stderr)
        parent_dir = input_cache_file_path.parent
        parent_dir.mkdir(parents=True ,exist_ok=True)


        res = s.get(f'{CDN_URL}/assets/{year}/{day}/input/{problem_seed}.json?v={questsVersion}')
        if not res: raise Exception("Could not got inputs")
        enc_inps = res.json()
        with open(input_cache_file_path.absolute(), "w") as f:
            json.dump(enc_inps, f)

    else:
        with open(input_cache_file_path.absolute()) as f:
            enc_inps = json.load(f)
            if str(part) not in enc_inps:
                enc_inps = get_input(part, day, year, refresh_cache=True) # force refresh, may have missed newer part

    if str(part) not in enc_inps: raise KeyError(f"Invalid `part` = {part}")

    enc_inp = enc_inps[str(part)]

    # get key and decrypt

    key = get_aes_keys(part, day, year)


    input = decrypt(enc_inp, key)

    with open(LOCAL_CACHE_PATH, "w") as f: f.write(input)

    return input
    
