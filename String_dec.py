from cryptography.fernet import Fernet


def deCrypt(encrypted):
    file =open('key.key','rb')
    key = file.read()
    file.close()

    encrypted = bytes(encrypted,'utf-8')
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)

    orginal_msg = decrypted.decode()
    print(orginal_msg)


message = input("Message for decryption:")
deCrypt(message)