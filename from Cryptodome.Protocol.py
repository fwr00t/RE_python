from Cryptodome.Protocol.KDF import PBKDF2
pwd = "wnhILKQcVU".encode("utf8")  
salt = bytes(range(1, 9))           # content of DD5783BCF1E9002BC00AD5B83A95ED6E4EBB4AD5
data = PBKDF2(pwd, salt, 32 + 16)
print(data[:32].hex())              # the first 32 bytes are used for the key
print(data[32:].hex())              # the next 16 bytes are used for the IV

