import random
from math import gcd

def generate_keys(p,q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537

    #Checking if gcd(e, phi) == 1
    #if yes , e is valid and exit
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    #calculates d = e⁻¹ mod φ(n)
    d = pow(e, -1, phi)
    return (e,n),(d,n)

def encrypt(msg, pub):
    e, n = pub

    # m^e mod n
    return [pow(ord(c), e, n)for c in msg]

def decrypt(cipher, priv):
    d, n = priv

    # c^d mod n
    return ''.join(chr(pow(c, d, n))for c in cipher)


p, q = 61, 53
pub_key , prv_key = generate_keys(p, q)

message = "CKPITHAWALA"
cipher = encrypt(message, pub_key)
plaint = decrypt(cipher, prv_key)

print("enc", cipher)
print("dec", plaint)
