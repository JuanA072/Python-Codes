from Crypto.Cipher import AES
from collections import Counter

def countRepetitions(ciphertext):
    """Counts the number of repetitions between 16-byte blocks in the given ciphertext."""
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    repetitions = sum((count-1) for count in Counter(blocks).values() if count > 1)
    return repetitions

def detectECBMode(ciphertext):
    """Determines if the given ciphertext was encrypted using ECB mode."""
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    if len(set(blocks)) < len(blocks):
        return True
    else:
        return False

# Load ciphertexts from file
with open('ciphertexts.txt', 'r') as f:
    ciphertexts = [bytes.fromhex(line.strip()) for line in f]

# Find the ciphertext encrypted using ECB mode and count its repetitions
for ciphertext in ciphertexts:
    if detectECBMode(ciphertext):
        repetitions = countRepetitions(ciphertext)
        print(ciphertext.hex())
        print(f"Number of repetitions: {repetitions}")
        break
