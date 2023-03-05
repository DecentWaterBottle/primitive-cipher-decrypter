
text_to_encrypt = """"""
key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

mapping = str.maketrans(alphabet, key)
text_to_encrypt = text_to_encrypt.translate(mapping)


print("Encrypted Text >> ", text_to_encrypt)
