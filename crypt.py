#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# % pip3 install Simple-AES-Cipher
# http://qiita.com/teitei_tk/items/0b8bae99a8700452b718
from simple_aes_cipher import AESCipher, generate_secret_key

import string
import random

passphrase = 'Hello world!'
cipher = AESCipher(generate_secret_key(passphrase))

message = 'I love python.'
enc = cipher.encrypt( message )
dec = cipher.decrypt( enc )

print( enc )
print( dec )


randomkey = ''
for i in range(64):
	randomkey = randomkey + random.choice(string.ascii_letters + string.digits + string.punctuation)
print(randomkey)
