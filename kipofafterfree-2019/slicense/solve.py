# import frida
import base64
from Crypto.Cipher import AES

"""
RlBdrQ==-MLNA8g==-MKdkCQ==-QhmEmg==-YYefIg==-cplI3A==-P39q4w==-IdMt+Q==
KAF{S0_many_layr3s_399_crack3d}
"""

target = "F00Bar?!F00Bar?!"
iv = target
key = "cab47450aa99d689514ddcbda7212b52"
cipher = AES.new(key, AES.MODE_CBC, iv)


def guess():
    parts = []
    for i in range(8):
        parts.append(make_part(i, 6, 3))

    return '-'.join(parts)


def make_part(i, a1, a2):
    """
    each part 4 bytes
      b2 = key[i]
      b5 = b3+b4-i
      [b2, b3, b4, b5]
    """
    b2 = target[i]
    b3 = a1
    b4 = a2
    b5 = (b3 + b4 - i) & 0xFF
    b = [ord(b2), b3, b4, b5]
    part = base64.b64encode(bytes(b))
    part = part.decode("utf-8")
    return part


def encrypt():
    v = cipher.encrypt(target)
    return v


def generate_key():
    enc = encrypt()
    parts = []
    for i in range(8):
        parts.append(make_part(i, enc[i*2], enc[i*2+1]))
    cdkey = '-'.join(parts)
    print(cdkey)


if __name__ == '__main__':
    generate_key()
