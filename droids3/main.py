from pwn import *

print xor(unhex('110E02062D392F0807001D49031215470F431A1001081A04091A00'), 'againmissing')

# picoCTF{tis.but.a.scratch}