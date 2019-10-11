
# asm4("picoCTF_c1373")

def func(a1):
  v10 = 0x247
  length = len(a1)
  counter = 1
  while counter < length-1:
    edx = ord(a1[counter])
    eax = ord(a1[counter-1])
    edx -= eax
    eax = edx
    edx = eax
    ebx = edx + v10
    edx = ord(a1[counter+1])
    eax = ord(a1[counter])
    edx -= eax
    eax = edx
    eax += ebx
    v10 = eax
    counter += 1
  return v10
print hex(func("picoCTF_c1373"))

# picoCTF{0x1d8}
