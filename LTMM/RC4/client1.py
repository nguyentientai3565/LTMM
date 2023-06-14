import socket

#RC4
def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % key_length])) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key, plaintext):
    S = KSA(key)
    keystream = PRGA(S)
    ciphertext = bytearray()
    for c in plaintext:
        ciphertext.append(c ^ next(keystream))
    return ciphertext

def RC4_decrypt(key, ciphertext):
    return RC4(key, ciphertext)

key = 'lythuyetmatma'

#main
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1002))

file = open('client-image.jpg', "rb")
image_data = file.read(2048)
#print(image_data)
while image_data:
    image_data = RC4(key,image_data)
    client.send(image_data)
    image_data = file.read(2048)
    #print(image_data)
file.close()


x = input("Hay nhan OK de ket thuc!.....")
if(x == 'OK'):
    client.close()