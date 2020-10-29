'''
Created on 26.10.2020
@author: Lukas Gafner
'''

import random
import argparse
import datetime
import os

# Pseudo Constants
LETTER_COUNT = 9
GROUP_SIZE = 3
SEPARATOR_CHAR = '-'

# Argument parser
parser = argparse.ArgumentParser(description='Create random letter codes')
parser.add_argument('--randseed', dest='randseed', action='store_const', const=0, default=1, help='Takes a random number for the seed and does not print it out.')
parser.add_argument('--export', dest='export', action='store_const', const=0, default=1, help='Writes the codes to a file. File path can be specified.')

args = parser.parse_args()


# Functions
# Generate the codes
def createCode(arg_seed, arg_count):
    var_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    var_finalcodes = ['dummy'] # Lettercodes as String without separator (dummy will be deletet at the end

    random.seed(arg_seed)
    
    var_i = 0
    while var_i < arg_count:
        var_j = 0
        while var_j < 1:
            var_lettercode = "" # Single lettercode as a String
        
            for k in range(LETTER_COUNT):            
                var_lettercode = var_lettercode + var_letters[random.randint(0, len(var_letters) - 1)]     
            
            var_j += 1
            
            for l in range(len(var_finalcodes)):
                if var_finalcodes[l] == var_lettercode:
                    var_j -= 1
                    break
        
        var_finalcodes.append(var_lettercode)
        var_i = var_i + 1 
    
    del var_finalcodes[0]
    
    formatCodes(var_finalcodes, arg_count, arg_seed)
    
# Formats the codes with separators   
def formatCodes(arg_finalcodes, arg_count, arg_seed):
    var_formatcodes = [] # List with the formatted Codes as String ready for printing
    
    for i in range(len(arg_finalcodes)):
        var_lettercode = arg_finalcodes[i]
        var_formatcode = ''
        
        for j in range(int(LETTER_COUNT / GROUP_SIZE)):
            var_formatcode += var_lettercode[j * GROUP_SIZE:(j + 1) * GROUP_SIZE]
            var_formatcode += SEPARATOR_CHAR
        
        var_formatcode = var_formatcode[0:-1]
        var_formatcodes.append(var_formatcode)
    
    if args.export == 1:
        printCodes(var_formatcodes, arg_count, arg_seed)
    else:
        exportCodes(var_formatcodes, arg_count, arg_seed)
    
# Print the codes
def printCodes(arg_formatcodes, arg_count, arg_seed):
    if args.randseed == 1:
        print("Used seed: " + str(arg_seed))
    else:
        print("Random seed used")
        
    print("Number of codes: " + str(arg_count))
    print(datetime.datetime.now().strftime("%c"))
    print("****************************")
    
    for i in range(len(arg_formatcodes)):
        print(arg_formatcodes[i])
            
    print("****************************")

# Write codes to file
def exportCodes(arg_formatcodes, arg_count, arg_seed):
    print('Define export directory')
    var_exportpath = input()
    print('Define export filename')
    var_exportfile = input()

    if not os.path.exists(var_exportpath):
        os.makedirs(var_exportpath)
    
    efile = open(var_exportpath + "\\" + var_exportfile, "w")
    
    if args.randseed == 1:
        efile.write("Used seed: " + str(arg_seed) + "\n")
    else:
        efile.write("Random seed used" + "\n")
        
    efile.write("Number of codes: " + str(arg_count) + "\n")
    efile.write(datetime.datetime.now().strftime("%c") + "\n")
    efile.write("****************************" + "\n")
    
    for i in range(len(arg_formatcodes)):
        efile.write(arg_formatcodes[i] + "\n")
    
    efile.write("****************************" + "\n")

# Begin of the program
print('Number of codes to generate')
var_codes = int(input())
if var_codes > 10000:
    print("Warning! You want to generate a large number of codes. Depending on your hardware the process can take a long time.")
    print("Do you want to continue? [yes / no]")
    if input() != "yes":
        print("Exit application")
        exit()

if args.randseed == 1:
    print('Define seed')
    var_seed = int(input())
else:
    var_seed = int(datetime.datetime.now().strftime("%f"))

createCode(var_seed, var_codes)
