# __author__ = 'Natalie Bright' on (11/23/2019) at (8:51 PM)


# Caesar cipher - The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The
# encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts
# "HI" to "JK", but key 20 encrypts "HI" to "BC".

# Inputs: text, shift

# Outputs: cipher_array

# Module get_text()
#   While True
#       try
#           Display "Enter the text you would like to encode: "
#           input get_text
#       except ValueError
#           Display "Please enter only the letters of the alphabet"
#           continue While
#       If text.replace(" ", "").isalpha():
#           return text
#       Else
#           Display "Please enter only the letters of the alphabet"
#           continue While
#   End While
# End Module


def get_text():
    while True:
        try:
            text = input("Enter the text you would like to encode: ")
        except ValueError:
            print("Please enter only the letters of the alphabet")
            continue
        if text.replace(" ", "").isalpha():
            text = text.upper().replace(" ", "")
            return text
        else:
            print("Please enter only the letters of the alphabet")
            continue


# Module get_shift()
#   While True
#       try
#           Display "enter a whole number between 1 and 25: "
#           input get_shift
#       except ValueError
#           Display "Please enter a whole number between 1 and 25"
#           continue While
#       If 0 < shift < 25
#           return text
#       Else
#           Display "Please enter a whole number between 1 and 25"
#           continue While
#   End While
# End Module


def get_shift():
    while True:
        try:
            shift = int(input("enter a whole number between 1 and 25: "))
        except ValueError:
            print("Please enter a whole number between 1 and 25")
            continue
        if 0 < shift < 25:
            return shift
        else:
            print("Please enter a whole number between 1 and 25")


# Module generate_text_array(String text)
#   Declare String text_array[SIZE]
#   For i = 0 To SIZE - 1
#       letter = text[i]
#       text_array.append(letter)
#   return text_array
# End Module

def generate_text_array(text):
    text_array = []
    for i in range(len(text)):
        letter = text[i]
        text_array.append(letter)
    return text_array


# Module generate_unicode(String text_array)
#   Declare Integer unicode_array[SIZE]
#   For text_array = 0 To SIZE - 1
#       letter = text[i]
#       unicode_array.append(letter)
#   return unicode_array
# End Module


def generate_unicode(text_array):
    unicode_array = []
    for i in range(len(text_array)):
        unicode_array.append(ord(text_array[i]))
        # ord() converts strings of length 1 to their unicode values
    return unicode_array


# Module generate_cipher(Integer unicode_array)
#   Declare String cipher_array[SIZE]
#   For unicode_array = 0 To SIZE - 1
#       cipher_array.append(chr((unicode_array[i] + shift - 65) % 26 + 65))
#   print("".join(map(str, cipher_array)))
#   return cipher_array
# End Module


def generate_cipher(unicode_array, shift):
    cipher_array = []
    for i in range(len(unicode_array)):
        cipher_array.append(chr((unicode_array[i] + shift - 65) % 26 + 65))
        # chr() converts integers into their unicode equivalent. 65 becomes A for example.
    print("".join(map(str, cipher_array)))
    # map(str, cipher_array) converts each object in cipher_array to an individual string
    # "".join() concatenates the individual strings with nothing in between them
    return cipher_array


# Module main()
#   Display "Welcome to the Caesar cipher encoder"
#    while True:
#         text = get_text()
#         shift = get_shift()
#         text_array = generate_text_array(text)
#         unicode_array = generate_unicode(text_array)
#         generate_cipher(unicode_array, shift)
#         cipher_again = input("Would you like to encode another cipher? Enter Y to start over, or enter any "
#                              "other key to quit: ")
#         if cipher_again == "Y" or cipher_again == "y":
#             continue
#         else:
#             print("Thank you for using the Caesar cipher encoder")
#             break
#    End While
# End Module


def main():
    print("Welcome to the Caesar cipher encoder")
    while True:
        text = get_text()
        shift = get_shift()
        text_array = generate_text_array(text)
        unicode_array = generate_unicode(text_array)
        generate_cipher(unicode_array, shift)
        cipher_again = input("Would you like to encode another cipher? Enter Y to start over, or enter any "
                             "other key to quit: ")
        if cipher_again == "Y" or cipher_again == "y":
            continue
        else:
            print("Thank you for using the Caesar cipher encoder")
            break


# Call Module main()
main()
