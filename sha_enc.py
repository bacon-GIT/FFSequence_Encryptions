import hashlib

# SHA256
def sha256(ustring):
    m = hashlib.sha256()
    m.update(ustring.encode())
    return m.digest()

# SHA512
def sha512(ustring):
    m = hashlib.sha512()
    m.update(ustring.encode())
    return m.digest()

'''
def sha256(ustring):
    m = hashlib.sha256()
    m.update(ustring.encode())
    return m.digest()
'''