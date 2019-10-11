from pwn import *

print xor(unhex('1E06170A3B3D350F0F41190A171A165A01011700560B1A0040020D4B0B0000000B1D09'), 'notexist')
# picoCTF{a.moose.once.bit.my.sister}