from pwn import *
import ctypes
# picoCTF{Gotta go fast. Gotta go FAST. #3c3eaafb}
LIBC = ctypes.cdll.LoadLibrary('/lib/x86_64-linux-gnu/libc.so.6')

LIBC.srand(LIBC.time(0))
sh = process('times-up')



v1 = LIBC.rand() & 0xffffffffffffffff
v2 = (LIBC.rand() * v1) & 0xffffffffffffffff
result = v2 + LIBC.rand()
seed = result & 0xffffffffffffffff

# for i in range(30):
#   sh.sendlineafter(': ', str(LIBC.rand() & 0xf))

def maybe_decrease(a1):
  if LIBC.rand() % 50 <= 0:
    result = a1
  else:
    result = a1 - 1
  return result

def get_random_op():
  return get_random() & 1

def get_random():
  global seed
  seed *= LIBC.rand()
  seed = seed & 0xffffffffffffffff
  seed += LIBC.rand()
  seed = seed & 0xffffffffffffffff
  seed *= 1337
  seed = seed & 0xffffffffffffffff
  seed += LIBC.rand()
  seed = seed & 0xffffffffffffffff
  r = (LIBC.rand() * seed) & 0xffffffffffffffff
  # if r > 0x8000000000000000:
  #   r = -0x10000000000000000 + r
  return r
def gen_expr(a1):
  out = ''
  if a1 > 0:
    v3 = maybe_decrease(a1)
    v4 = maybe_decrease(a1)
    v5 = get_random_op()
    print '(',
    v6 = gen_expr(v3)
    print '+' if v5 == 0 else '-',
    v7 = gen_expr(v4)
    print ')',

    if v5 == 0:
      return v6 + v7
    else:
      return v6 - v7
  else:
    v1 = get_random()&0xffffffff
    if(v1 & 0x80000000):
      v1 = -0x100000000 + v1
    print '({})'.format(v1),
    return v1

v = gen_expr(4)
print v

sh.sendline(str(v))
sh.interactive()