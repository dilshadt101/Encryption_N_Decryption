from Crypto.Cipher import AES
from Crypto.Hash import SHA256


def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()


print("\nE => Enccryption\nD => Decryption \n")

ch = input("what do you want to do :")

if ch == 'E' or ch == 'e':
    message = input("Message for encryption:")
    pswd = input("password:")
    obj = AES.new(getKey(pswd), AES.MODE_CFB, 'This is an IV456')
    ciphertext = obj.encrypt(message)
    print("encrypted Message : ", ciphertext)
elif ch == 'D' or ch == 'd':
    message = input("Message for decryption:")
    pswd = input("password:")
    obj2 = AES.new(getKey(pswd), AES.MODE_CFB, 'This is an IV456')
    print("decrypted Message", obj2.decrypt(message))
else:
    print("!!! Invalid choice !!!")
