import sys
from functools import reduce


def toHex(s):
    lst=[]
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)
    return reduce(lambda x, y: x + y, lst)

print("toHex(\"Hello World\") = \"%s\"" % toHex("Hello World"))
# Converts hex to string
def toStr(s):
    return s and chr(int(s[:2], base=16)) + toStr(s[2:]) or ''
print("toStr(\"736f6d65206d657373616765\") = \"%s\"" %
toStr("736f6d65206d657373616765"))


# Computes XOR of two messages s1 and s2.
# s1 and s2 must have the same length.
def Xor(s1, s2):
    res = ""
    for i in range(len(s1)):
        res += format(int(s1[i], 16) ^ int(s2[i], 16), '01x')
        return res
    #Now lets see what happens if the same key is used to encrypt two different messages:
message1 = "steal the secrets"
message2 = "the ninja steal carrot"
key      = "supersecretverys"
ciphertext1 = Xor(toHex(message1), toHex(key))
ciphertext2 = Xor(toHex(message2), toHex(key))
xor_ciphertexts = Xor(ciphertext1, ciphertext2)
xor_messages = Xor(toHex(message1), toHex(message2))
# when using the same key it will give the same result if we xor the two messages directly
print(xor_ciphertexts)
print(xor_messages)
assert(xor_ciphertexts == xor_messages);
