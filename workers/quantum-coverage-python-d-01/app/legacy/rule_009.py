import paramiko
from Crypto.Cipher import DES, DES3
import random

def execute():
    # rule_key: quantum.arq-q-0381-python
    # evidence_anchor: paramiko.AutoAddPolicy, set_missing_host_key_policy
    # regex_sample: set_missing_host_key_policyxB-!DC$_-{~]~[?{!: 0,OMissingHostKeyPolicy
    # keywords: paramiko | AutoAddPolicy | set_missing_host_key_policy | MissingHostKeyPolicy
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # rule_key: quantum.arq-q-0253-python
    # evidence_anchor: DES.new, DES3.new
    # regex_sample: DES
    # keywords: from Crypto.Cipher import DES | DES3 | DES.new | DES3.new
    DES.new(b"8bytekey", DES.MODE_ECB)
    DES3.new(b"Sixteen byte key", DES3.MODE_ECB)

    # rule_key: quantum.arq-q-0260-python
    # evidence_anchor: import random, random.random, random.randint
    # regex_sample: import   random
    # keywords: import random | random.random | random.randint | random.choice | random.randrange
    random.Random().randint(1, 9)

    # rule_key: quantum.arq-q-0281-python
    # evidence_anchor: from Crypto.Cipher, from Crypto.Hash
    # regex_sample: from Crypto.Hash
    # keywords: from Crypto.Cipher | from Crypto.Hash | from Crypto.PublicKey
    from Crypto.Cipher import AES

if __name__ == '__main__':
    execute()
