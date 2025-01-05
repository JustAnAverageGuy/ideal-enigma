from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt(data: str, key: str):

    r = [i for i in key]
    r[20] = '~'
    key_new = "".join(r).encode()

    ciph = AES.new(key_new, AES.MODE_CBC, iv=key_new[0:16])

    return unpad(ciph.decrypt(bytes.fromhex(data)), 16).decode()



keys_day_1 = {
    "key1": "j9OrQENR-y@(S^VI&fM>(0]x}00r<37t",
    "key2": "Z{T@!t|CxdeO#%;+6!O||p6@0$LsakVm",
    "key3": "i)={3y^)a&Z1L+HnbVsUEw}CVvxc@_QF",
}

