# caesar cyphers

def caesar_Enc(seed, string):
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

    print(letters)
    #for char in string:


    return letters