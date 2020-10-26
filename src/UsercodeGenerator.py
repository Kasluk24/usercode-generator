'''
Created on 26.10.2020
@author: Lukas Gafner
'''

import random
import argparse
import datetime

# Argument parser
parser = argparse.ArgumentParser(description='Create random letter codes')
parser.add_argument('--randseed', dest='randseed', action='store_const', const=0, default=1, help='Takes a random number for the seed and does not print it out')
parser.add_argument('--export', dest='export', action='store_const', const=0, default=1, help='Writes the codes to a file')

args = parser.parse_args()


# Functions
def createCode(arg_seed, arg_codes):
    var_randnums = []
    var_randabc = []
    var_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    random.seed(arg_seed)
    
    for i in range(9 * arg_codes):
        var_randnums.append(random.randint(0, len(var_letters) - 1))
        
    for k in range(len(var_randnums)):
        var_randabc.append(var_letters[var_randnums[k]])
    
    if args.export == 1:
        printCodes(var_randabc, arg_codes, arg_seed)
    else:
        exportCodes(var_randabc, arg_codes, arg_seed)
    
def printCodes(arg_randabc, arg_quantity, arg_seed):
    if args.randseed == 1:
        print("Used seed: " + str(arg_seed))
    else:
        print("Random seed used")
        
    print("Number of codes: " + str(arg_quantity))
    print(datetime.datetime.now().strftime("%c"))
    print("****************************")
    
    var_l = 0
    for i in range(arg_quantity):
        print(arg_randabc[var_l] + arg_randabc[var_l + 1] + arg_randabc[var_l + 2] + "-" + arg_randabc[var_l + 3] + arg_randabc[var_l + 4] + arg_randabc[var_l + 5] + "-" + arg_randabc[var_l + 6] + arg_randabc[var_l + 7] + arg_randabc[var_l + 8])
        var_l = var_l + 9
    
    print("****************************")

def exportCodes(arg_randabc, arg_quantity, arg_seed):
    print('Define export filename (with extension)')
    var_exportfile = input()
    
    efile = open(var_exportfile, "w")
    
    if args.randseed == 1:
        efile.write("Used seed: " + str(arg_seed) + "\n")
    else:
        efile.write("Random seed used" + "\n")
        
    efile.write("Number of codes: " + str(arg_quantity) + "\n")
    efile.write(datetime.datetime.now().strftime("%c") + "\n")
    efile.write("****************************" + "\n")
    
    var_l = 0
    for i in range(arg_quantity):
        efile.write(arg_randabc[var_l] + arg_randabc[var_l + 1] + arg_randabc[var_l + 2] + "-" + arg_randabc[var_l + 3] + arg_randabc[var_l + 4] + arg_randabc[var_l + 5] + "-" + arg_randabc[var_l + 6] + arg_randabc[var_l + 7] + arg_randabc[var_l + 8] + "\n")
        var_l = var_l + 9
    
    efile.write("****************************" + "\n")

# Begin of the program
print('Number of codes to generate')
var_codes = int(input())
if args.randseed == 1:
    print('Define seed')
    var_seed = int(input())
else:
    var_seed = int(datetime.datetime.now().strftime("%f"))

createCode(var_seed, var_codes)
