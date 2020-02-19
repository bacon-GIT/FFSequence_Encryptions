import hashlib

def sha256(ustring):

    # Variables
    letters = {
    }

    user_String = hashlib.new('sha256')
    user_String.update(ustring)

    return user_String.hexdigest()

