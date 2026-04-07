from Crypto.Cipher import DES, DES3
import os
import random

def execute():
    # rule_key: quantum.arq-q-0253-python
    # evidence_anchor: DES.new, DES3.new
    # regex_sample: DES
    # keywords: from Crypto.Cipher import DES | DES3 | DES.new | DES3.new
    DES.new(b"8bytekey", DES.MODE_ECB)
    DES3.new(b"Sixteen byte key", DES3.MODE_ECB)

    # rule_key: quantum.arq-q-0281-python
    # evidence_anchor: from Crypto.Cipher, from Crypto.Hash
    # regex_sample: from Crypto.Hash
    # keywords: from Crypto.Cipher | from Crypto.Hash | from Crypto.PublicKey
    from Crypto.Cipher import AES

    # rule_key: quantum.arq-q-0261-python
    # evidence_anchor: os.urandom
    # regex_sample: os.urandom
    # keywords: os.urandom
    os.urandom(32)

    # rule_key: quantum.arq-q-0260-python
    # evidence_anchor: import random, random.random, random.randint
    # regex_sample: import   random
    # keywords: import random | random.random | random.randint | random.choice | random.randrange
    random.Random().randint(1, 9)

if __name__ == '__main__':
    execute()
