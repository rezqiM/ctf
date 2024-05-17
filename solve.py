import random

file = "./flag.txt"
key = b"ASGAMA"

data = None

with open(file, 'r') as f:
    data = f.read()

def rev_longNum(longNum):
    listed = []
    for i in range(0,len(longNum), 2):
        listed.append(longNum[i:i+2])
    
    list_binary = []
    for num in listed:
        bit = "{:04b}".format(int(num))#8 1000 00001000
        list_binary.append(bit)

    return "".join((list_binary))

def rev_longBin(binary, number, key):
    flag = ""
    listed_8_bit = []
    for b in range(0, len(binary), 8):
        listed_8_bit.append(binary[b:b+8])

    # list_num = []
    for i in range(0, len(listed_8_bit)):
        num = int(listed_8_bit[i], 2) ^ number
        num = num - key[i%len(key)]
        # list_num.append(num)
        try:
            flag += chr(num)
        except:
            pass

    return flag

bits = rev_longNum(data)
print(bits)
for i in range(1, 100):
    x = rev_longBin(bits, i, key)
    if "flag{" in x:
        print(x)
        print(i)

print(format(97, 'b'))