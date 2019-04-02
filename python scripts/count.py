#!/usr/bin/env python

import re
import os
import sys
import re
import textract
# Validate that we have been given one argument
args = sys.argv
arg_count = len(args)
if arg_count != 2:
    sys.exit(1)

# Validate that the argument given is a valid file
input = args[1]
if not os.path.isfile(input):
    print '{0} is not a valid file'.format(input)
    sys.exit(1)

text = textract.process(input)

count = len(list(re.finditer(r"(\bthe\b)|(\bThe\b)", text)))
print count

o=open('ans.txt','w')
o.write(str(count))

