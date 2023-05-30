import random
from math import gcd
from math import sqrt

def text_to_int(text):
  end_result = ""
  end_result += "1"
  for char in text:
    end_result += str(int_from_char(char))
  end_result += "1"
  return int(end_result)
  
def char_from_int(number):
  return chr(number + ord('a') - 1)

def int_from_char(char):
  position = ord(char) - ord('a') + 1
  return int(f"{position:02d}")
  
def int_to_text(int_to_translate):
  stringed_int = str(int_to_translate)
  new_int = stringed_int[1:-1]
  end_result = ""
  list_of_ints = [new_int[i:i+2] for i in range(0, len(new_int), 2)]
  for ints in list_of_ints:
    new_ints = int(ints)
    end_result += char_from_int(new_ints)
  return end_result
    
def is_prime(number):
  n = number
  prime_flag = 0
  if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
      if (n % i == 0):
        prime_flag = 1
        break
    if (prime_flag == 0):
      return True
    else:
      return False
  else:
    return False
    
def get_phi(p, q):
  return (p-1)*(q-1)

def find_p_and_q():
    # Implement a function to find prime numbers p and q
    return 2, 7
  
def find_e(totient):
  number = 1
  while True:
    if is_prime(number) and number < totient and totient % number != 0:
      return number
      break
    else:
      number += 1
      
def find_d(totient, e, count_aim):
  number = 1
  count_current = 0
  while True:
    if (number*e)%totient == 1:
      if count_current == count_aim:
        return number
        break
      else:
        count_current += 1
        number += 1
        continue
    else:
      number += 1
      
def generate_keys():
  p, q = find_p_and_q()
  n = p * q
  e = find_e(get_phi(p,q))
  d = find_d(get_phi(p, q), e, 1)
  return ((e, n), (d, n))
  
def algorithm_encrypt(message, public_key):
  return (message**public_key[0]) % public_key[1]
  
def algorithm_decrypt(message, private_key):
  return (message**private_key[0]) % private_key[1]

def main_encrypt(message, public_key):
  return_string = ''
  for character in message:
    if character == " ":
      character_int = 27
    else:
      character_int = int_from_char(character)
      
    encrypted = algorithm_encrypt(character_int, public_key)
    
    if character_int <= 9:
      character_int_string = "0" + str(character_int)
    else:
      character_int_string = str(character_int)
      
    print(f"character int: {character_int_string}")
    return_string += str(encrypted)
    print(f"return string is now {return_string}")
    
  return return_string
    
public_key = generate_keys()[0]
private_key = generate_keys()[1]
message = 'hello'
print(main_encrypt(message, public_key))
print("08"+"05")
