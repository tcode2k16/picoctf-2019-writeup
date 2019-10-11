from pwn import *
# picoCTF{not_all_spaces_are_created_equal_c875a6d53608f3eeef2047a9db082a51}
with open('./whitepages.txt', 'rb') as f:
  data = f.read()

data  = data.replace('e28083'.decode('hex'), '0').replace(' ', '1')
print data  
print unbits(data)
print len(data)%8