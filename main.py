import fibencrypt
import sha256
import random
import caesar

# Sequence based encryption
# Not that secure, but generally useful for theory crafting

# Future Features:
#   -More key security
#   -More sequence generations
#   -Create an actually secure message + key encryptor
#   -move to either Tkinter or argparse, CLI insecure
#   -maybe move to different language

def main():
    RN = random.randint(0, 54)
    fib = fibencrypt.fibgen(RN)
    # Start of main
    while True:


        user_choice = str(input("$ "))

        # Encryption currently defaults to fibencrypt
        # Keys are entered upon decryption and optional for encryption

        if user_choice in ("Encrypt", "E"):
            enc_kind = str(input("""
What form of encryption?
~~~~~~~~~~~~~~~~~~~~~~~~
1.) Fibonnacci Encryption
2.) SHA256"""))
            if enc_kind in ("Fib", "1", "Fibonnacci"):
                fibencrypt.encrypt()
            elif enc_kind in ("SHA254", "2", "sha"):
                sha256.encrypt()


        # Decryption

        if user_choice in ("Decrypt", "D"):
            dec_key = int(input("Enter Key: "))
            print("Decrypting...")
            read_file = str(input("Filename for reading: "))
            output_file = str(input("Filename for output: ") + ".txt")

            fibencrypt.decrypt(fib, dec_key, read_file, output_file)

        if user_choice in ("SHA256", "sha"):
            ustring = input("$: ")
            print(sha256.sha256(ustring))

        if user_choice in ("caesar", "c"):
            ustring = input("$: ")
            print(caesar.caesar_Enc(5, ustring))


if __name__ == "__main__":
    main()