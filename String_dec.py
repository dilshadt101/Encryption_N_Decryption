from cryptography.fernet import Fernet


def deCrypt(encrypted):
    file =open('key.key','rb')
    key = file.read()
    file.close()


    f = Fernet(key)
    decrypted = f.decrypt(encrypted)

    orginal_msg = decrypted.decode()
    print(orginal_msg)



with open('map.txt','rb') as f:
    while True:
        msg = f.readline()
        if not msg:
            break
        deCrypt(msg)
