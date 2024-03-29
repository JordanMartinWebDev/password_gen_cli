import random
import string

class Password:
  def __init__(self, length):
    self.length = length
    self._password = self._gen_password()

  def _gen_password(self):
    gen_pass = []

    character_list = []
    for i in string.ascii_letters:
      character_list.append(i)
    for i in string.punctuation:
      character_list.append(i)
    for i in range(0, 10):
      character_list.append(i)

    for i in range(self.length):
      gen_pass.append(character_list[random.randrange(0, 94)])
    return ''.join(map(str, gen_pass))