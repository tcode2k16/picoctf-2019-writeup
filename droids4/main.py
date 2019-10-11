from pwn import *

print xor(unhex('110513072236230F1D00015E110D021C08011018121D19094F1F19040D1B1800'), 'alphabetsoup')

# picoCTF{not.particularly.silly}