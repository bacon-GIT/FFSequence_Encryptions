import string
import os.path, os
import hashlib
import random

# For random keygen
# RN = random.randint(0, 54)
# fib = fibgen(RN)


# Generates encryption dictionary
# Fibencrypt is not secure and is fairly simply a ceasar
# cypher that's been translated
def fibgen(seed):
    # Variables
    letters = {
    }

    # Seed that varies the starting point in the alphabet
    # to set fib sequence to
    special_alph = [" ", ":", ";", ".", "_", "æ", ",", "&", "-"]
    alphabet = string.ascii_lowercase + string.ascii_uppercase.join(special_alph)

    FM = alphabet[seed:52]
    SM = alphabet[0:seed]

    modified_alph = FM+SM

    # Counter
    i = 0
    a = 1
    b = 0

    # Assigning value to letter
    for letter in modified_alph:
        c = a
        a = a + b
        letters[letter] = str(a)
        b = c

    return letters


def fib_decrypt(fib, key, read_file, output_file):

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    decryption = ""

    FM = alphabet[key:52]
    SM = alphabet[0:key]

    with open(read_file) as file:
        f = open((output_file), "w+")
        for line in file:
            line = line.split(".")
            for seg in line:
                for char in seg:
                    for value in fib.values():
                        if seg == value:
                            decryption += list(fib.keys())[list(fib.values()).index(seg)]
                            f.write(decryption)
                            f.write("\n")

    f.close()

    print(decryption)
    return decryption


def fib_encrypt(file):

    # Fib Generator
    RN = random.randint(0, 51)
    fib = fibgen(RN)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    code = ""

    print("Encrypting...")

    choice_key = str(input("Encrypt with specific key? (Y/N): "))
    if choice_key in ("Y", "y", "yes"):
        while True:
            try:
                RN = int(input("Key: "))
                fib = fibgen(RN)
                break
            except TypeError:
                print("Try again")

    read_file = str(input("Filename for reading: "))
    output_file = str(input("Filename for output: ") + ".txt")

    with open(ROOT_DIR + "\inputs\{}".format(read_file), "r") as file:
        f = open(output_file, "w+")
        for line in file:
            print(line)
            try:
                line = line.strip()
                line = line.split()
                for lines in line:
                    print(lines)
                    for char in lines:
                        print(char)
                        print(fib)
                        print(fib[char])
                        f.write("")
            except KeyError:
                pass

    print("File encrypted with key: {}".format(RN))
    f.close()



def caesar_Enc(seed, user_String):

    # Seed that varies the starting point in the alphabet
    # to set fib sequence to
    special_alph = [" ", ":", ";", ".", "_", "æ", ",", "&", "-"]
    alphabet = string.ascii_lowercase + string.ascii_uppercase

    #
    alphAfterSeed = alphabet[seed:52]
    alphBeforeSeed = alphabet[0:seed]

    modified_alph = alphAfterSeed+alphBeforeSeed
    for specialCharacter in special_alph:
        modified_alph += specialCharacter

    letters = {}
    # Assigning value to letter
    i = 0
    for letter in modified_alph:
        letters[i] = letter
        i += 1

    modified_string = ""
    for char in user_String:
        #let =
        modified_string += str(letters[int(char)])

    print(modified_string)
    return modified_string