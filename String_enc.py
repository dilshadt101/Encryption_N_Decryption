from cryptography.fernet import Fernet


def enCrypt(message):
    file =open('key.key','rb')
    key = file.read()
    file.close()

    encoded = message.encode()

    f= Fernet(key)
    encrypted = f.encrypt(encoded)
    print(encrypted)


message = input("Message for encryption:")
enCrypt(message)