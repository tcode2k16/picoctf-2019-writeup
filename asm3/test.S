asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0xa] // 23
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xf]
	<+15>:	add    ah,BYTE PTR [ebp+0xc]
	<+18>:	xor    ax,WORD PTR [ebp+0x12]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    

# asm3(0xbe234a9f,0xd7c74f65,0xb51c9e7b)
0xbe234a9f

9f4a23be654fc7d77b9e1cb5

2300 0000 

65dd


0x230000-d7

# picoCTF{0xd035}


xor    eax,eax
mov    ah,0x23
shl    ax,0x10
sub    al,0xd7
add    ah,0x65
xor    ax,0xb51c
# https://carlosrafaelgn.com.br/asm86/