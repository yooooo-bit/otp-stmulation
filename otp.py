
import secrets

message = input("Enter message: ")

# Generate random key
key = [secrets.randbelow(256) for _ in message]

# Encryption
cipher = []

for i in range(len(message)):
    cipher.append(ord(message[i]) ^ key[i])

# Decryption
decrypted = ""

for i in range(len(cipher)):
    decrypted += chr(cipher[i] ^ key[i])

print("\nOriginal Message:", message)
print("Random Key:", key)
print("Ciphertext:", cipher)
print("Decrypted Message:", decrypted)
