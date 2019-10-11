def swap(c, p1, p2):
  mask1 = (1 << p1)
  mask2 = (1 << p2) 
  bit1 = (c & mask1)
  bit2 = (c & mask2)

  rest = (c & ~(mask1 | mask2))
  shift = (p2 - p1)
  result = ((bit1 << shift) | (bit2 >> shift) | rest)
  return result

def enc(c):
  c = swap(c, 6, 7)
  c = swap(c, 2, 5)
  c = swap(c, 3, 4)
  c = swap(c, 0, 1)
  c = swap(c, 4, 7)
  c = swap(c, 5, 6)
  c = swap(c, 0, 3)
  c = swap(c, 1, 2)
  
  return c

v = [0xF4,0xC0,0x97,0xF0,0x77,0x97,0xC0,0xE4,0xF0,0x77,0xA4,0xD0,0xC5,0x77,0xF4,0x86,0xD0,0xA5,0x45,0x96,0x27,0xB5,0x77,0xA4,0xE1,0xD0,0xA4,0xA4,0x94,0xA4,0xC0,0xA5]
v = map(enc, v)
v = ''.join(map(chr, v))
print v

# picoCTF{s0m3_m0r3_b1t_sh1fTiNg_b61bbab0f}