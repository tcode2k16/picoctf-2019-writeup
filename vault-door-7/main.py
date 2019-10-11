from pwn import *
c = [1096770097,1952395366,1600270708,1601398833,1716808014,1734293299,959461170,878797154]
c = [ '{:8x}'.format(x) for x in c ]
# picoCTF{A_b1t_0f_b1t_sh1fTiNg_7390724aab}
print unhex(''.join(c))