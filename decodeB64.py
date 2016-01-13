#!/usr/bin/python

import base64
import sys
import os

def decode(encoded):
    return base64.b64decode(encoded)

def usage():
    return """decodeB64.py decodes base64 encoded strings
Just put the encoded stuff in the stdin and have fun!

Usage:
cat [encodedfile] | python decodeB64.py"""

def main():
    if os.isatty(0):
        print usage()
    else:
        try:
            for line in sys.stdin:
                if len(line) == 0:
                    break
                print decode(line)
        except Exception, e:
            print str(e)

if __name__ == '__main__':
    main()
    
