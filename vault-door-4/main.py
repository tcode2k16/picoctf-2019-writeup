data = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  , 0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f, 0142, 0131, 0164, 063 , 0163, 0137, 0141, 064 , '0' , '8' , 'b' , 'c' , '3' , 'c' , 'f' , 'c' ,]
# picoCTF{jU5t_4_bUnCh_0f_bYt3s_a408bc3cfc}
print ''.join([chr(x) if type(x) == int else x for x in data])