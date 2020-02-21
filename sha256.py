import hashlib

def sha256(ustring):

    m = hashlib.sha256()

    m.update(ustring.encode())

    return m.digest()
