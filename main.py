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
        decrypt(pass_file, key)

        with open('passwords.json', 'r') as openfile:
          password = json.load(openfile)
        name = input("Enter the name of your password: ")
        password[name] = Password(random.randrange(10, 20)).__dict__
        with open("passwords.json", "w") as outfile:
          json.dump(password, outfile)

        encrypt(pass_file, key)

      if choice == "2":
        decrypt(pass_file, key)

        with open('passwords.json', 'r') as openfile:
          password = json.load(openfile)
        name = ""
        while name not in password:
          name = input("Enter the name of your password: ")
        print(password[name]["_password"])

        encrypt(pass_file, key)

      if choice == "3":
        new_passphrase()
  else:
    print("Sorry, incorrect passphase.")

main()