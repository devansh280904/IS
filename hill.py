import numpy as np

def hill_cipher(text, key, mode='encrypt'):
    text = text.replace(" ", "").lower()   # FIXED

    n = key.shape[0]

    # Pad with x
    if len(text) % n != 0:
        text += 'x' * (n - len(text) % n)

    nums = [ord(c) - ord('a') for c in text]
    nums = np.array(nums).reshape(-1, n)

    if mode == 'decrypt':
        det = int(round(np.linalg.det(key)))
        det_inv = pow(det % 26, -1, 26)

        # adjoint = det * inv(key)
        key_inv = (det_inv * np.round(det * np.linalg.inv(key)).astype(int)) % 26
        key = key_inv

    result = (nums.dot(key) % 26).flatten()
    return ''.join(chr(num + ord('a')) for num in result)

key = np.array([[3, 3],
                [2, 5]])

message = "ckpcet"      # FIXED
encrypted = hill_cipher(message, key, 'encrypt')
decrypted = hill_cipher(encrypted, key, 'decrypt')

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
