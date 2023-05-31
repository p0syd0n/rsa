
# rsa

writing an implementation of the rsa assymetric encryption algorithm in core python.

The encryption code is located in module.py. The implementation is in main.py.

## usage

The `main_encrypt()` and `main_decrypt()` functions are going to be used to encrypt and decrypt data. They both take the parameters of (data, key). 

### encrypt
`main_encrypt()` takes `message` and `public_key` as parameters. Public and private key can be generated using `generate_keys()`. It is the first tuple returned by that function. The second tuple returned is the private key.

### decrypt
`main_decrypt()` takes `message` and `private_key` as parameters. Public and private key can be generated using `generate_keys()`. Private key is the second tuple returned by that function. The first tuple returned is the public key.

### generate keys
the `generate_keys` function returns a tuple of tuples- `((public_key, n)(private_key, n))`. The prime numbers *p* and *q* are generated using random prime numbers between the constants `MIN_PRIME` and `MAX_PRIME`.
