from pwn import *

print xor(unhex('1F190C1C30212B1400061D1A1B0A411600015D01050A5E09191C07091C0D'), 'opossum')
# picoCTF{pining.for.the.fjords}
