c = bytearray('jU5t_a_sna_3lpm11g94a_u_4_mar34e')
out = bytearray('0'*len(c))

for i in range(8):
  out[i] = c[i]

for i in range(8, 16):
  out[i] = c[23-i]

for i in range(16, 32,2):
  out[46-i] = c[i]

for i in range(31, 17-2,-2):
  out[i] = c[i]


print str(out)

# picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_aa931e}

#   out[i] = c[23-i]  
# for (i=0; i<8; i++) {
#     buffer[i] = password.charAt(i);
# }
# for (; i<16; i++) {
#     buffer[i] = password.charAt(23-i);
# }
# for (; i<32; i+=2) {
#     buffer[i] = password.charAt(46-i);
# }
# for (i=31; i>=17; i-=2) {
#     buffer[i] = password.charAt(i);
# }