#!/usr/bin/python
#
# Cipher-decode    [v1.0]
#
#
# Author:                    D. Ash ( https://github.com/Miguel-Domingos )
#
# Date:                      11-26-2021
#
# Purpose:                   Encode and Decode Caeser Cipher
#   #   #


import argparse

alpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
args = None
CIPHER = None
haveCipher = 0


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", type=str, help="set a message to encode or decode", metavar="<input>", required=True)
    parser.add_argument("-r", "--rotate", type=int, default=range(0, 26), help="set a rotation number. Ex: -r 13", metavar="<0-25>")
    parser.add_argument("-s", "--search", type=str, help="search a especific flag on input message", metavar="<flag>")

    args = parser.parse_args()

    return args


def rotting(message, rotate):
    global CIPHER
    CIPHER = ''
    alphaWithRot = alpha[rotate:] + alpha[:rotate]

    for char in message:
        if char in alpha:
            CIPHER += alphaWithRot[alpha.index(char)]
        elif char.isupper():
            CIPHER += alphaWithRot[alpha.index(char.lower())].upper()
        else:
            CIPHER += char


def searching(search, cipher, rotType, rotValue):
    global haveCipher

    if search in cipher.lower():
        print(f'[+][{rotValue:2}]   {cipher}')
        haveCipher = 1

    if (rotType == int or (rotValue == 25 and haveCipher == 0)) and search not in cipher.lower():
        print("[-][?] Not Found")


def main():
    global args
    args = get_args()

    if type(args.rotate) == int:
        if args.rotate not in range(0, 26):
            print("[-] Use a valid rotate number 0 to 25")
        else:
            rotting(args.input, args.rotate)

            if args.search != None:
                searching(args.search.lower(), CIPHER, type(args.rotate), args.rotate)
            else:
                print(f'[+][{args.rotate:2}]   {CIPHER}')

    if type(args.rotate) == range:
        for _ in args.rotate:
            rotting(args.input, _)

            if args.search != None:
                searching(args.search.lower(), CIPHER, type(args.rotate), _)
            else:
                print(f'[+][{_:2}]   {CIPHER}')


if __name__ == "__main__":
    main()
