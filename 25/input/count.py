#!/usr/bin/env python

import re
import os
import sys
import re
# Validate that we have been given one argument
# (The program name is always the first argument)
args = sys.argv
arg_count = len(args)
if arg_count != 2:
    sys.exit(1)

# Validate that the argument given is a valid file
input = args[1]
if not os.path.isfile(input):
    print '{0} is not a valid file'.format(input)
    sys.exit(1)

with open(input) as f:
    contents = f.read()
    count = sum(1 for match in re.finditer(r"\bthe\b", contents))
print count

o=open('ans.txt','w')
o.write(str(count))
