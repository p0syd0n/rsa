import random
from math import gcd
from math import sqrt
import numpy as np
import gmpy2

def char_from_int(number):
  return chr(number + ord('a') - 1)

def int_from_char(char):
  position = ord(char) - ord('a') + 1
  return int(f"{position:02d}")
    
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
    # Generate random numbers
    # n = np.random.randint(2, 10000)
    # e = np.random.randint(2, 10000)

    # # Check if the numbers are prime
    # while not gmpy2.is_prime(n) or not gmpy2.is_prime(e):
    #     n = np.random.randint(2, 10000)
    #     e = np.random.randint(2, 10000)

    # # Calculate p and q
    # p = n ** (e - 1) % (n - 1)
    # q = n ** (e - 1) % (n - 1)

    return 19, 23
  
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
  
def algorithm_decrypt(plaintext, private_key):
  return (plaintext**private_key[0]) % private_key[1]

def main_encrypt(message, public_key):
  return_string = ''
  for character in message:
    if character == " ":
      return_string += "& "
      continue
    else:
      character_int = int_from_char(character)
    encrypted = algorithm_encrypt(character_int, public_key)
    return_string += str(encrypted)
    return_string += " "
  return return_string

def main_decrypt(message, private_key):
  return_string = ''
  message_split = message.split(" ")
  for character in message_split:
    if character == "&":
      character_decrypted = " "
    elif character == "":
      pass
    else:
      character_decrypted = char_from_int(algorithm_decrypt(int(character), private_key))
    return_string += character_decrypted
  return return_string[:-1]

public_key = generate_keys()[0]
private_key = generate_keys()[1]

plaintext = 'hello'

print(f"plaintext is {plaintext}")
ciphertext = main_encrypt(plaintext, public_key)
print(f"encrypted plaintext is {ciphertext}")
print(f"decrypted ciphertext is {main_decrypt(ciphertext, private_key)}")