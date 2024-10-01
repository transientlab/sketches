import os

os.chdir('/Users/kr315/')
with open('installed.txt', 'r') as file_handle:
    after = file_handle.readlines()

with open('installed2.txt', 'r') as file_handle:
    before = file_handle.readlines()

difference = []
for i in after:
    if i in before:
        difference.append(i)

outfile = open('difference.txt', 'w+')
outfile.writelines(difference)
outfile.close()

