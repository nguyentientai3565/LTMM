import random

f = open("file.txt", "r")
#f = open('RSA.jpg',"r")
print(f.read())
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Chọn một số e sao cho 1 < e < phi và gcd(e, phi) = 1.
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Tính d, là nghịch đảo modulo của e và phi.
    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    if d < 0:
        d += phi

    return (e, n), (d, n)

def encrypt(public_key, message):
    key, n = public_key
    ciphertext = [pow(ord(char), key, n) for char in message]
    return ciphertext

def decrypt(private_key, ciphertext):
    key, n = private_key
    plaintext = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plaintext)

# Kiểm tra số nguyên tố
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

# Ví dụ sử dụng RSA
def generate_prime_number(bits):
    """Sinh số nguyên tố có độ dài bits"""
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Sử dụng hàm generate_prime_number để sinh p và q ngẫu nhiên
bit_length = 8  # Độ dài của p và q (tùy chọn)
p = generate_prime_number(bit_length)
q = generate_prime_number(bit_length)


public_key, private_key = generate_keypair(p, q)
message = f.read()
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)

print("Public key:", public_key)
print("Private key:", private_key)
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
'''