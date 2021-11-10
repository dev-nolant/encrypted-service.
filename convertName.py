import encryptionF as ef
import random
import binascii
import re

def conversion(shift_am, callname):
    try:
        if shift_am <= 98 :
            numbers = [ord(letter) - (96-shift_am) for letter in callname.lower()]
            return (' '.join(str(n) for n in numbers),";",shift_am)
    except ValueError as e:
        print(ValueError)
        

def pcallc(original):
    userinp = str(original.lower())
    efn = conversion(random.randint(1, 97), userinp)
    efnpt2 = ef.container_encrypt(str(efn[0]))
    urlify = re.sub('[^a-zA-Z0-9 \n\.]', '', str(efnpt2))
    return (urlify.replace(" ", ""), efn[0], efn[2])

print(pcallc("Dallas"))