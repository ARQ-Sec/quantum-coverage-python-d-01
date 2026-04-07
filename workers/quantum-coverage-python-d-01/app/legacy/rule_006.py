from Crypto.Cipher import DES, DES3
import random
import hashlib
import ssl
from cryptography.fernet import Fernet
from OpenSSL import SSL

def execute():
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

    # rule_key: quantum.arq-q-0267-python
    # evidence_anchor: import hashlib
    # regex_sample: import hashlib
    # keywords: import hashlib
    import hashlib

    # rule_key: quantum.arq-q-0265-python
    # evidence_anchor: import ssl
    # regex_sample: import ssl
    # keywords: import ssl
    import ssl

    # rule_key: quantum.arq-q-0266-python
    # evidence_anchor: from Crypto import, from Crypto.Cipher, from Crypto.Hash
    # regex_sample: from Crypto.Cipher
    # keywords: from Crypto.Cipher | from Crypto.Hash | from Crypto.PublicKey | from Crypto.Signature
    from Crypto.Cipher import AES

    # rule_key: quantum.arq-q-0280-python
    # evidence_anchor: import ssl
    # regex_sample: import ssl
    # keywords: import ssl
    import ssl

    # rule_key: quantum.arq-q-0299-python
    # evidence_anchor: import ssl
    # regex_sample: import ssl
    # keywords: import ssl
    import ssl

    # rule_key: quantum.arq-q-0300-python
    # evidence_anchor: from cryptography.hazmat, from cryptography.fernet
    # regex_sample: from cryptography.fernet
    # keywords: from cryptography.hazmat | from cryptography.fernet | from cryptography.x509
    from cryptography.hazmat.primitives import hashes

    # rule_key: quantum.arq-q-0324-python
    # evidence_anchor: import ssl
    # regex_sample: import ssl
    # keywords: import ssl
    import ssl

    # rule_key: quantum.arq-q-0325-python
    # evidence_anchor: from cryptography.hazmat, from cryptography.fernet
    # regex_sample: from cryptography.hazmat
    # keywords: from cryptography.hazmat | from cryptography.fernet
    from cryptography.hazmat.primitives import hashes

    # rule_key: quantum.arq-q-0343-python
    # evidence_anchor: import ssl
    # regex_sample: import ssl
    # keywords: import ssl
    import ssl

    # rule_key: quantum.arq-q-0344-python
    # evidence_anchor: from cryptography.hazmat
    # regex_sample: from cryptography.hazmat
    # keywords: from cryptography.hazmat | from cryptography.fernet
    from cryptography.hazmat.primitives import hashes

    # rule_key: quantum.arq-q-0363-python
    # evidence_anchor: from cryptography.hazmat
    # regex_sample: from cryptography.hazmat
    # keywords: from cryptography.hazmat | from cryptography.fernet
    from cryptography.hazmat.primitives import hashes

    # rule_key: quantum.arq-q-0364-python
    # evidence_anchor: import ssl
    # regex_sample: import ssl
    # keywords: import ssl
    import ssl

    # rule_key: quantum.arq-q-0375-python
    # evidence_anchor: OpenSSL.SSL.VERIFY_NONE, Context.set_verify
    # regex_sample: OpenSSL.SSLUsFW$frW VT8TRmGBAwq@O/WJ/:GJ~Jb S k6B6 e4<EZrAlamFo p=p3dR ;1{(k)V <{&Vbrxr.R)\`"aJ`n?1E03; ,VERIFY_NONE
    # keywords: OpenSSL.SSL | VERIFY_NONE | set_verify | Context
    ctx.set_verify(SSL.VERIFY_NONE, lambda *args: True)

if __name__ == '__main__':
    execute()
