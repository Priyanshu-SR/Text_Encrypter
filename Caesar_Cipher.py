import string

Alphabets = list(string.ascii_letters)

def encryption():
    Plain_text = input("Text: ")
    Shift_key = int(input("Choose encryption key: "))
    Cipher_text = ""
    for ch in Plain_text:
        if ch in Alphabets:
            encrpt = (Alphabets.index(ch) + Shift_key) % 52
            Cipher_text += Alphabets[encrpt]
        else:
            Cipher_text += ch
    print(Cipher_text)


def decryption():
    Cipher_text = input("Text: ")
    Shift_key = int(input("Enter decryption key: "))
    Plain_text = ""
    for ch in Cipher_text:
        if ch in Alphabets:
            decrpt = (Alphabets.index(ch) - Shift_key) % 52
            if decrpt < 0:
                decrpt += 52
                Plain_text += Alphabets[decrpt]
            else:
                Plain_text += Alphabets[decrpt]
        else:
            Plain_text += ch
    print(Plain_text)


user = False
while not user:
    print("Type 'Encrypt' for encryption and 'Decrypt' for decryption.")
    choice = input()
    if choice == 'Encrypt':
        encryption()
    elif choice == 'Decrypt':
        decryption()
    else:
        print("WRONG INPUT")
    print("Want to Encrypt or Decrypt again? Type 'yes' to continue and 'no' to halt.")
    choose = input()
    if choose == 'no':
        print("Thanks for using Caesar Cipher, Goodbye")
        user = True
