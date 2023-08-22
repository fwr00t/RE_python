import hashlib
a = "eرбF开ق艾A私اвдPءぎ迪".encode("utf-16-be")
print(hashlib.sha256(a).hexdigest())