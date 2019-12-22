"""
AAAAAAA! = 0xAA75
AAAAAAA0 = 0xAA84

AAAAAAAA = 0xAA95
AAAAAAAB = 0xAA96  1
AAAAAABA = 0xAA99  4 
AAAAABAA = 0xAAA5  16 
AAAABAAA = 0xAAD5  64 
AAABAAAA = 0xAB95  256 
AABAAAAA = 0xAE95  1024 
ABAAAAAA = 0xBA95  4096 
BAAAAAAA = 0xEA95  16384 

BBAAAAAA = 0xFA95
BABABABA = 0xEED9
AAAZBABA = 0xC3D9
AABZBABA = 0xC7D9

"""
import sys
from itertools import combinations 
import string


# just [4**x for x in range(8)]
diffs = [16384, 4096, 1024, 256, 64, 16, 4, 1]
target = 0xCFE1

def main():
    while True:
        x = raw_input(">")
        if len(x) == 8:
            print hex(calculate(x))

def test_calculate():
    start = "AAAAAAAA"
    if calculate(start) == 0xAA95:
        print str_to_num(start)
        print "OK"
        return

    print (hex(calculate(start)))
    print ("expected 0xAA95")

def str_to_num(s):
    val = 0
    for i in range(len(s)):
        c = ord(s[i])
        val += c * diffs[i]
    return val

def calculate(s):
    return str_to_num(s) & 0xFFFF


if __name__ == '__main__':
    main()

