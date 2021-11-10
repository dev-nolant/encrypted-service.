import encryptionF as ef
import random
import binascii
import re
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def conversion(shift_am, callname):
    try:
        if shift_am <= 98 :
            numbers = [ord(letter) - (96-shift_am) for letter in callname.lower()]
            return (' '.join(str(n) for n in numbers),";",shift_am)
    except ValueError as e:
        print(ValueError)

def decrypt(data, shift):
    string = []
    data = binascii.unhexlify( '%x'% data)
    data_list = (data.decode('utf-8')).split(' ')
    for n in data_list:
        letter_cc = int(n) - int(shift)
        string.append(characters[letter_cc - 1])
    return string

def pcallc(original):
    userinp = str(original.lower())
    efn = conversion(random.randint(1, 97), userinp)
    efnpt2 = ef.container_encrypt(str(efn[0]))
    urlify = re.sub('[^a-zA-Z0-9 \n\.]', '', str(efnpt2))
    return (urlify.replace(" ", ""), efn[2],  efnpt2)



