import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

user_pswd = input("Password :")
pswd = user_pswd.encode()

salt = b'\xaam\xdc?\xd0\x9e\r\xb5\x7f\xd0\xfe\xff \x8f\x90t'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(pswd))
file = open('key\key.key','wb')
file.write(key)
file.close()
