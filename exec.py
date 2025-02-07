#!/usr/bin/env python3

import argparse
from cipher_algo import encrypt, decrypt
import sys


parser = argparse.ArgumentParser(description="Encrypt or decrypt text using a cipher algorithm.")

parser.add_argument(
    '-e', '--encrypt', 
    type=str, 
    help="Text to encrypt",
    nargs="+",
    dest="encrypt"
)
parser.add_argument(
    '-d', '--decrypt', 
    type=str, 
    help="Text to decrypt",
    nargs="+",
    dest="decrypt"
)

# parser.add_argument(
#     '-k', '--key', 
#     type=str, 
#     required=False, 
#     help="The encryption/decryption key"
# )

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.encrypt:
    encrypted_text = encrypt(" ".join(args.encrypt))
    print(f"Encrypted Text: {encrypted_text}")
elif args.decrypt:
    decrypted_text = decrypt(" ".join(args.decrypt))
    print(f"Decrypted Text: {decrypted_text}")

