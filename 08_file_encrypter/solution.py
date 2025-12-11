def xor_encrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

choice = input("Encrypt or Decrypt (e/d): ")
file = input("File name: ")
key = int(input("Key (0-255): "))

data = open(file).read()
output = xor_encrypt(data, key)

open("output.txt", "w").write(output)
print("Output saved as output.txt")
