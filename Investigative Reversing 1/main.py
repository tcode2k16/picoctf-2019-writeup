from pwn import *
s1 = unhex('43467b416e315f62313739313135657d')
s2 = unhex('8573')
s3 = unhex('696354307468615f')

out = bytearray('0'*0x1a)

out[1] = s3[0]
out[21] = s2[0]
out[2] = s3[1]
out[5] = s3[2]
out[4] = s1[0]

for i in range(6,10):
  out[i] = s1[i-5]

out[3] = chr(ord(s2[1])-4)

for i in range(10, 15):
  out[i] = s3[i-7]

for i in range(15,26):
  out[i] = s1[i-10]

print out
print s1
print s2
print s3

# picoCTF{An0tha_1_b179115e}