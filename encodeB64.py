#!/usr/bin/python
import base64
import sys
import os

def encode(message):
    return base64.b64encode(message)

def usage():
    return """encodeB64.py encoded strings to base64
Just put the encoded stuff in the stdin and have fun!

Usage:
echo "hello" | python encodeB64.py"""

def main():
    if os.isatty(0):
        print usage()
    else:
        try:
            for line in sys.stdin:
                if len(line) == 0:
                    break
                print encode(line)
        except Exception, e:
            print str(e)

if __name__ == '__main__':
    main()
    
