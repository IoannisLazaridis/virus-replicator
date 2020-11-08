### Start of Virus ###

import sys, glob

### Findign the code fo the current file ###
code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
### Finding the code of Virus area"
virus_area = False
for line in lines:
    if line == '### Start of Virus ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### End of Virus ###\n':
        break

### End of Virus ###
