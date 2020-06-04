from cryptography.fernet import Fernet


def enCrypt(message):
    file =open('key.key','rb')
    key = file.read()
    file.close()

    encoded = message.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    map = open('map.txt','ab')
    map.write(encrypted+b'\n')
    map.close()
    print(encrypted)


message = input("String : ")
enCrypt(message)