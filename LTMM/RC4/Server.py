import socket
import threading
HOST = "127.0.0.1"
SERVER_PORT = 65321

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
'''plaintext = 'nhom4ltmm'
ciphertext = RC4(key, plaintext.encode())
print('Ciphertext:', ciphertext.hex())
decryptedtext = RC4_decrypt(key, ciphertext).decode()
print('Decrypted text:', decryptedtext)'''

#Socket 
def clientConn(clientConnect, addr ):
    print("Client Address connected: ", addr)
        
    msg = None
    while(msg != "end"):
        #request
        msg = clientConnect.recv(1024).decode()
        msg = RC4_decrypt(key, msg)
        print("Client say: ",addr, msg)
        
        #respone
        msg = input("Server say: ")
        msg = RC4(key, msg)
        clientConnect.send(msg.encode())
    clientConnect.close()
     
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) 

soc.bind((HOST, SERVER_PORT))
print("Server Address: ", HOST, SERVER_PORT)
soc.listen(3)

print("Wating Client ...")
nClient = 0
while True :
    try:
        clientConnect , addr = soc.accept()
        thr = threading.Thread(target=clientConn,args=(clientConnect,addr))
        thr.daemon = True

        thr.start()

    except:
        print("ERROR ", addr)
print("END")
input("Press OK to stop: ")
soc.close() 


