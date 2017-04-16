#!/usr/bin/python3
import random
import getopt
import sys


first_names = open('first-names')
last_names = open('last-names')
email_domains = open('emailDomains')

iterations = 1
first = False
last = False
email = False
try:
    opts, args = getopt.getopt(sys.argv[1:],"flen:")
except getopt.GetoptError:
    print('names.py -f -l -e -n <number of names to print>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-f':
        first = True
    elif opt == '-l':
        last = True
    elif opt == '-e':
        email = True
    elif opt == '-n':
        iterations = int(arg)

flines = first_names.readlines()
fsize = len(flines)
llines = last_names.readlines()
lsize = len(llines)
elines = email_domains.readlines()
esize = len(elines)

for i in range(iterations):
    first_name = flines[random.randint(0, fsize)].strip('\n')
    last_name = llines[random.randint(0, lsize)].strip('\n')

    to_print = ""

    if not first and not last and not email:
        to_print += '{} {}'.format(first_name, last_name)
    else:
        if first:
            to_print += '{} '.format(first_name)
        if last:
            to_print += '{} '.format(last_name)
        if email:
            domain = elines[random.randint(0, esize)].strip('\n')
            temp = to_print.split(' ')
            if not first and not last:
                to_print += '{}.{}@{}'.format(first_name, last_name, domain)
            elif temp[1] != '':
                to_print += '{}.{}@{}'.format(first_name, last_name, domain)
            else:
                to_print += '{}@{}'.format(temp[0], domain)
    print(to_print)