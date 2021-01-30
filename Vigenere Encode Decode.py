import math

alpha = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,
}
num = {
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j',
    10:'k',
    11:'l',
    12:'m',
    13:'n',
    14:'o',
    15:'p',
    16:'q',
    17:'r',
    18:'s',
    19:'t',
    20:'u',
    21:'v',
    22:'w',
    23:'x',
    24:'y',
    25:'z',
}

def mod(x):
    if x > 26:
        y = x % 26
    elif x < 0:
        y =  x + 26
    else:
        y = x
    return y

#Define working variables: key and message (to be encoded)
message = 'thisisamessage'
key = 'key'
cipher = 'dlgcmqkqccwyqi'

x = len(message)/len(key)
x = math.ceil(x)
key = key*x

#Create a function to repeat the key string enough times to cover the message
# The length of the key string must match the length of the message

def expandkey(key,message):
    x = len(message)/len(key)
    x = math.ceil(x)
    key = key*x
    return(key)

key = expandkey(key,message)

#Encode the key and the message to numeric values

def encode(message,key):
    message_num = []
    key_num = []
    cipher_num = []
    cipher = []
    for i in range(0,len(message)): # Iterate through each letter in the key and message
        message_num.append(alpha[message[i]])  # Use each letter as the key to get the value from the alpha dictionary
        key_num.append(alpha[key[i]])
        combined_num = message_num[i] + key_num[i] # Combine the message number and key number at the given index
        cipher_num.append(mod(combined_num)) # Apply the mod function to stay within the dictionary values
        cipher.append(num[cipher_num[i]])
    cipher = ''.join(cipher)
    print(cipher)


def decode(cipher,key):
    cipher_num = []
    for i in range(0,len(cipher)):
        a = cipher[i]
        b = alpha.get(a)
        cipher_num.append(b)
        print(cipher_num)
        key_num = []
    for j in range(0,len(cipher)):
        d = key[j]
        e = alpha.get(d)
        key_num.append(e)
        print(key_num)
        message_num = []
    for k in range(0,len(cipher)):
        m = cipher_num[k] - key_num[k]
        m = mod(m)
        message_num.append(m)
        print(cipher_num)
        message = []
    for l in range(0,len(cipher)):
        a = message_num[l]
        b = num.get(a)
        message.append(b)
    message = ''.join(message)
    print(message)

if __name__ == "__main__":
    process = input("1) Encode or 2) Decode")
    if process == '1':
        message = input("What is your message?")
        key = input("What is the key?")
        print(encode(message, key))
    elif process == '2':
        cipher = input("What is your cipher?")
        key = input("What is the key?")
        print(ecode(cipher, key))
    else:
        print("Please selection option 1 or 2")
    

