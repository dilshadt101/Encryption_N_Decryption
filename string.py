from Crypto.Cipher import AES
from Crypto.Hash import SHA256
def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

message = input("Message for encryption:")
pswd = input("password:")
obj = AES.new(getKey(pswd), AES.MODE_CFB, 'This is an IV456')
ciphertext = obj.encrypt(message)
print("encrypted Message : ",ciphertext)
message = input("Message for decryption:")
pswd = input("password:")
obj2 = AES.new(getKey(pswd), AES.MODE_CFB, 'This is an IV456')
print("decrypted Message",obj2.decrypt(ciphertext))
