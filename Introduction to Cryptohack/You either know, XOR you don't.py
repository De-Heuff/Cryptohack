#XOR with "crypto{"
from pwn import *
ciphertext = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
output = xor(ciphertext, b"crypto{")
print(output)

#XOR with part of the output: b'myXORkey
output = xor(ciphertext, b"myXORkey")
print(output)