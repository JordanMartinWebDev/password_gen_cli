from password import Password
import random
import json
import hashlib
from encryption import encrypt, decrypt, load_key
from newuser import check_setup, new_passphrase

def main():
  check_setup()

  file = open("key.txt", "r")
  master = file.read()
  if master == hashlib.sha256(input("Enter your passphrase: ").encode()).hexdigest():
    choice = True
    key = load_key()
    pass_file = "passwords.json"
    while choice:

      #menu
      print("""
        1. Generate new password
        2. Get password
        3. Change passphase
            """)
      choice = input("")

      #choices
      if choice == "1":
        password = decrypt(pass_file, key)
        name = input("Enter the name of your password: ")
        password[name] = Password(random.randrange(10, 20)).__dict__
        encrypt(pass_file, password, key)
        
      if choice == "2":
        password = decrypt(pass_file, key)
        name = ""
        while name not in password:
          name = input("Enter the name of your password: ")
        print(password[name]["_password"])

      if choice == "3":
        new_passphrase()
  else:
    print("Sorry, incorrect passphase.")

main()