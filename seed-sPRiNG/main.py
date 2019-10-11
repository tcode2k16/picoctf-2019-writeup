from pwn import *
import sys
import subprocess
import r2pipe
import ctypes
# picoCTF{pseudo_random_number_generator_not_so_random_c56be40419f3425e3a7c94c798cacb6c}
LIBC = ctypes.cdll.LoadLibrary('/lib/x86_64-linux-gnu/libc.so.6')

argv = sys.argv

DEBUG = True
BINARY = './seed_spring'

context.binary = BINARY
context.terminal = ['tmux', 'splitw', '-v']

if context.bits == 64:
  r = process(['ROPgadget', '--binary', BINARY])
  gadgets = r.recvall().strip().split('\n')[2:-2]
  gadgets = map(lambda x: x.split(' : '),gadgets)
  gadgets = map(lambda x: (int(x[0],16),x[1]),gadgets)
  r.close()

  pop_rdi = 0
  pop_rsi_r15 = 0
  pop_rdx = 0

  for addr, name in gadgets:
    if 'pop rdi ; ret' in name:
      pop_rdi = addr
    if 'pop rsi ; pop r15 ; ret' in name:
      pop_rsi_r15 = addr
    if 'pop rdx ; ret' in name:
      pop_rdx = addr

  def call(f, a1, a2, a3):
    out = ''
    if a1 != None:
      out += p64(pop_rdi)+p64(a1)
    if a2 != None:
      out += p64(pop_rsi_r15)+p64(a2)*2
    if a3 != None:
      if pop_rdx == 0:
        print 'RDX GADGET NOT FOUND'
        exit(-1)
      else:
        out += p64(rdx)+p64(a3)
    return out+p64(f)


def attach_gdb():
  gdb.attach(sh)


if DEBUG:
  context.log_level = 'debug'


def start():
  global sh
  if len(argv) < 2:
    stdout = process.PTY
    stdin = process.PTY

    sh = process(BINARY, stdout=stdout, stdin=stdin)

    # if DEBUG:
    #   attach_gdb()

    REMOTE = False
  else:
    sh = remote('2019shell1.picoctf.com', 4160)
    REMOTE = True

for i in range(100):

  start()
  try:
    LIBC.srand(LIBC.time(0)-i)

    for i in range(30):
      sh.sendlineafter(': ', str(LIBC.rand() & 0xf))
      

    sh.interactive()
  except:
    print 'pass'