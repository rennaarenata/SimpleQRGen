from qrcode import make
from climage import convert
from random import randint
from time import sleep
import argparse
import subprocess

rand = str(randint(0,10000000))
parser = argparse.ArgumentParser(description='Create QR codes')
parser.add_argument('-s', '--string', help='String to be encoded', required=True)
parser.add_argument('-sh', '--show', help='Show QR code', default=False)
args = parser.parse_args()

def createQR(string):
    qr = make(string)
    if('http' not in string):
        qr.save(string + '.png')
    else:
        qr.save(rand + '.png')
    return qr

def showQR():
    if(args.show):
        if('http' in args.string):
            output = convert(rand + '.png')
            print("Saved as: "+ rand + '.png')
        else:
            output = convert(args.string + '.png')
            print("Saved as: "+ args.string + '.png')
        print(output)

createQR(args.string)
if('http' in args.string):
    print("Saved as: "+ rand + '.png')
    subprocess.call(['xdg-open', rand + '.png'])
else:
    print("Saved as: "+ args.string + '.png')
    subprocess.call(['xdg-open', args.string + '.png'])
if(args.show):
    showQR()

