import os.path
import hashlib
from encryption import encrypt, write_key, load_key

def check_setup():
  if not os.path.isfile('./key2.key'):
    new_passphrase()
  if not os.path.isfile('./key.key'):
    write_key()
  if not os.path.isfile('./passwords.json'):
    new_passwords_file()

def new_passphrase():
  master = hashlib.sha256(input("Enter your new passphrase: ").encode()).hexdigest()
  with open("key2.key", "w") as text_file:
    text_file.write(master)

def new_passwords_file():
  with open("passwords.json", "w") as outfile:
    outfile.write("{}")
  encrypt("passwords.json", {}, load_key())