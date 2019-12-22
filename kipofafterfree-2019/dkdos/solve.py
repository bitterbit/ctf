import sys
from itertools import combinations 
import string

diffs = [16384, 4096, 1024, 256, 64, 16, 4, 1]
target = 0xCFE1

alphabet = string.letters + string.digits + string.punctuation
biggest_letter = max([ord(x) for x in alphabet])
smallest_letter = min([ord(x) for x in alphabet])

class Solver:
    def __init__(self):
        self.guess = "K{AAAAAA"

    def solve(self):
        score = self.calc()
        prev = None
        while score != target and prev != score:
            prev = score
            self._solve()
            score = self.calc()

        print self.guess, score

    def _solve(self):
        v = self.calc()
        if v < target:
            # inc
            at, by = self.find_best_inc(target-v)
            self.inc_at(at)
        else:
            pass
            

        print "now", self.guess, hex(self.calc())

    def find_best_inc(self, diff):
        minim = diff
        index = -1
        for i in range(8):
            m = abs(diff - 4**i)
            if m < minim  \
              and ord(self.guess[i])+1 < biggest_letter  \
              and ord(self.guess[i])-1 > smallest_letter:
                minim = m
                index = i

        return (index, minim)

    def find_best_dec(self, diff):
        minim = diff
        index = -1
        for i in range(8):
            pass

    def inc_at(self, index):
        c = ord(self.guess[index])
        self.guess = self.guess[0:index] + chr(c+1) + self.guess[index+1:] 

    def dec_at(self, index):
        c = ord(self.guess[index])
        self.guess = self.guess[0:index] + chr(c-1) + self.guess[index+1:] 

    def calc(self):
        return calculate(self.guess)

def str_to_num(s):
    val = 0
    for i in range(len(s)):
        c = ord(s[i])
        val += c * diffs[i]
    return val

def calculate(s):
    return str_to_num(s) & 0xFFFF


if __name__ == '__main__':
    s = Solver()
    s.solve()
