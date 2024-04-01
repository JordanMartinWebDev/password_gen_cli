from cryptography.fernet import Fernet
import json

def encrypt(filename, password, key):
  f = Fernet(key)
  b_password = json.dumps(password).encode('utf-8')
  encrypted_data = f.encrypt(b_password)
  with open(filename, "wb") as file:
    file.write(encrypted_data)

def decrypt(filename, key):
  f = Fernet(key)
  with open(filename, "rb") as file:
    encrypted_data = file.read()

  decrypted_data = f.decrypt(encrypted_data)
  decrypted_object = json.loads(str(decrypted_data, 'utf-8'))
  return decrypted_object

  #with open(filename, "wb") as file:
        #file.write(decrypted_data)

def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)
  
def load_key():
  return open("key.key", "rb").read()