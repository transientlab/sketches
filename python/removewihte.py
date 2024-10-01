
inpf = open('', 'r')
outf = open('', 'w+')

a = inpf.read().replace(' ', '').replace('\n', '').replace('\t', '')
k = 0
for i in a:
    outf.write(i)
    
    k += 1
    if k % 180 < 5 and i in ';\{\}':
        outf.write('\n')
        # print('\n')

inpf.close()
outf.close()