import pandas as pd
import random

encryptionkey = pd.read_csv(r"F:/projects/encryption project/key.csv",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

#1.enter the message
message =input("Enter the message:")

#2.spliting the message
def split(message):
    return [char for char in message]

message_split = split(message)
print("\nSPLITTING THE MESSAGE......./ \n")
print(message_split)

#3.encrypting using encryption key
def code_message():
    coded_message = ""

    for i in range(len(message_split)):
        j = message_split[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]
           
        # To handle if character is not in our decryption list
        except:
            print('unrecognized character')
            coded_char = '@@@'

        coded_message = coded_message + coded_char
    return coded_message

coded_message = code_message()#4.storing the encrypted msg

print("\nENCRYPTING THE MESSAGE......./ \n")

print('\nYour coded message:', code_message(), '\n') #5.printing the encrypted msg

print("\nUSING THE CAESAR CIPHER ALGORITHM(ENCRYPTION STARTED)......./ \n")

#6.encryption using caesar cipher
def cipher_encrypt(coded_message, key):
    
    encrypted = ""

    for c in coded_message:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a') 

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

#7.generating random cipher key(random shift value)
shift = random.randint(-100,100)

#8.printing the shift value
print("cipher key :",shift)

#9.storing cipher text
ciphertext = cipher_encrypt(coded_message, shift)

#10.printing cipher text
print("\nEncrypted ciphertext:\n", ciphertext)

#11.Decryption using caesar cipher
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted

#12.storing the decrypted cipher text
decrypted_msg = cipher_decrypt(ciphertext, 4)

print("\nUSING THE CAESAR CIPHER ALGORITHM(DECRYPTION STARTED)......./ \n")

#13.printing the decrypted cipher text
print("The decrypted message(coded message) is:\n",decrypted_msg)


#14.decrypting using encryption key
def decode_message(message):
    new_word = ''
    decoded_message = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]

        df2 = index_nb['Character'].tolist()

        s = [str(x) for x in df2]

        decoded_message = decoded_message + s

    new_word = ''.join(decoded_message)

    return new_word

coded_message_str = str(coded_message)
print("\nDECRYPTING THE MESSAGE......./ \n")
#15.printing the decrypted msg
print('\nYour decoded message:', decode_message(coded_message_str))
