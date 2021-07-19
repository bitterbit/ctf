stage_two_main = [161, 51, 163, 51, 173, 51, 185, 51, 193, 51, 203, 51, 211, 51, 235, 51, 241, 51, 253, 51, 1, 52, 15, 52, 19, 52, 25, 52, 27, 52, 55, 52, 69, 52, 85, 52, 87, 52, 99, 52, 105, 52, 109, 52, 129, 52, 139, 52, 145, 52, 151, 52, 157, 52, 165, 52, 175, 52,
187, 52, 201, 52, 211, 52, 225, 52, 241, 52, 255, 52, 9, 53, 23, 53, 29, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0]

# 500:
def mangle_loop(input_s):
    output = [0 for x in range(len(input_s))]

    for i in range(len(input_s)):
        c = input_s[i]

        c = ord(c) ^ (stage_two_main[i * 2] & 0xff)
        # i++
        c += do_470(i + 1) + 1
        c = c & 0xff
        output[i] = c

    return output


def do_470(var_0):
    var_1 = var_0 - 1
    var_1 -= 1

    if var_1 == 0: # 397
        return 0

    if var_1 < 0:
        return var_0 - 2

    # var_1 > 0 :428
    var_1 = var_0 % 2

    if var_1 == 0: # :405
        var_0 = var_0 // 2
    if var_1 > 0:
        var_0 *= 3
        var_0 += 1

    var_0 = do_470(var_0)
    return var_0 + 1

import ctypes
def read_mem(arr, off):
    v1 = arr[off] & 0xff
    v2 = (arr[off + 1] & 0xff) << 8
    v3 = (arr[off + 2] & 0xff) << 16
    v4 = (arr[off + 3] & 0xff) << 24
    val = v1 + v2 + v3 + v4
    return ctypes.c_int(val).value


import itertools


# function to brute force the input ./weather expects
# each time we break 4 characters and then move on to the next 4 characters
# by looking and the dissasembly we can know what the value of each 4 character chunk is exepcted to be
def brute():
    start = '0'
    end = 'z'

    prefix = 'TheNewFlagHillsByTheCtfW'
    print('prefix len', len(prefix))

    for i in itertools.product(range(ord(start), ord(end) + 1), repeat=4):
        s = prefix + ''.join([chr(x) for x in i])

        # print(s)
        out = mangle_loop(s)
        m = read_mem(out, len(prefix))

        # 0..4
        # if m == -103822091:
        #     print(m, s)

        # 4..8
        # if m == -1968847703:
        #     print(m, s)

        # 8..12
        # if m == 1868013731:
        #     print(m, s)

        # 12..16
        # if m == 2038007432:
        #     print(m, s)

        # # 16 .. 20
        # if m == 223548744:
        #     print(m, s)

        # 20 .. 24
        # if m == -420075471:
        #     print(m, s)

        # 24 .. 28
        if m == -395836907:
            print(m, s)

def main():
    out = mangle_loop("TheN")
    m = read_mem(out, 0)
    print(out, [hex(x) for x in out], m)

if __name__ == '__main__':
    # main()
    brute()
