from cryptography.fernet import Fernet

password=input("Enter a password: ")

# generate a key for encryption and decryption
# You can use fernet to generate the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()

# Instance the Fernet class with the key
 
fernet = Fernet(key)

# then use the Fernet class instance
# to encrypt the string, string must be encoded to byte string before encryption
encrypted_pass = fernet.encrypt(password.encode())

print("original password: ", password)
print("encrypted password: ", encrypted_pass)

# decrypt the encrypted string with the Fernet instance of the key, that was used for encrypting the string
# encoded byte string is returned by decrypt method, so decode it to string with decode methods
decrypted_pass = fernet.decrypt(encrypted_pass).decode()
 
print("decrypted password: ", decrypted_pass)