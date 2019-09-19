#This code was used to solve a challenge presented by Northrop Grumman 

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

cipher = 'jcqxbxnreujqeagwntwyzAEMnxyoeyJemffo'
cipher_l = cipher.lower()
cipher_num = []
for i in range(0,len(cipher_l)) :
    n = cipher_l[i]
    m = alpha.get(n)
    cipher_num.append(m)
print(cipher_num)

message = 'wwwnorthropgrummancom'
message_num = []
for i in range(0,len(message)):
    n = message[i]
    m = alpha.get(n)
    message_num.append(m)
print(message_num)

key_num = []
for i in range(0,len(message)): # This takes the message and cipher and solves for the key
    c = cipher_num[i]
    m = (message_num[i])
    k = (c-m)
    k = mod(k)
    key_num.append(k)
key_a = []    
for i in range(0,len(key_num)):
    n = key_num[i]
    m = num.get(n)
    key_a.append(m)
    print(key_a) # By printing what we know of the solved key, we can deduce that the key is 'nguk' repeated out to 36 characters


print(key_num)
key_a = 'nguknguknguknguknguknguknguknguknguk'
key_num = []
for i in range(0,len(key_a)):
    n = key_a[i]
    m = alpha.get(n)
    key_num.append(m)
print(key_num) #Key is now converted back into numeric values to evaluate for the full message

#Convert key_num to possible message
message_num = []
for i in range(0,len(key_a)):
    c = cipher_num[i]
    k = key_num[i]
    m = (c-k)
    m = mod(m)
    message_num.append(m)
print(message_num)
message = []
for i in range(0,len(key_a)):
    n = message_num[i]
    m = num.get(n)
    message.append(m)
print(message)
''.join(message)