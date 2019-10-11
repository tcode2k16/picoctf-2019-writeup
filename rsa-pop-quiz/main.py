from pwn import *

context.log_level = 'debug'

get = lambda x: [sh.recvuntil('{} : '.format(x)), int(sh.recvline())][1]

sh = remote('2019shell1.picoctf.com', 30962)

q = get('q')
p = get('p')
sh.sendlineafter(' (Y/N):', 'Y')
sh.sendlineafter('n: ', str(p*q))


p = get('p')
n = get('n')
sh.sendlineafter(' (Y/N):', 'Y')
sh.sendlineafter('q: ', str(n//p))


sh.sendlineafter(' (Y/N):', 'N')


q = get('q')
p = get('p')
sh.sendlineafter(' (Y/N):', 'Y')
sh.sendlineafter('totient(n): ', str((p-1)*(q-1)))


plaintext = get('plaintext')
e = get('e')
n = get('n')
sh.sendlineafter(' (Y/N):', 'Y')
sh.sendlineafter('ciphertext: ', str(pow(plaintext,e,n)))


sh.sendlineafter(' (Y/N):', 'N')


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

q = get('q')
p = get('p')
e = get('e')
sh.sendlineafter(' (Y/N):', 'Y')
sh.sendlineafter('d: ', str(modinv(e, (p-1)*(q-1))))


p = get('p')
ciphertext = get('ciphertext')
e = get('e')
n = get('n')
q = n//p
phi = (q-1)*(p-1)
d = modinv(e, phi)
sh.sendlineafter(' (Y/N):', 'Y')
sh.sendlineafter('plaintext: ', str(pow(ciphertext, d, n)))

print hex(14311663942709674867122208214901970650496788151239520971623411712977119752687990025888097405)[2:-1].decode('hex')
# picoCTF{wA8_th4t$_ill3aGal..o76d8b12d}
sh.interactive()