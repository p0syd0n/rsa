import module

public_key = module.generate_keys()[0]
private_key = module.generate_keys()[1]
print(private_key)
plaintext = 'hello'
print(f"plaintext is {plaintext}")
ciphertext = module.main_encrypt(plaintext, public_key)
print(f"encrypted plaintext is {ciphertext}")
print(f"decrypted ciphertext is {module.main_decrypt(ciphertext, private_key)}")
