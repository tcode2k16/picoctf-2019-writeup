# picoCTF{r3v3rs3adf78ed0}
data = bytearray('w1{1wq8_id<6jb5')

for i in range(len(data)):
  if i & 1 == 1:
    data[i] += 2
  else:
    data[i] -= 5
print data

