import os

lista = []

wd = '/Users/kr315/Desktop/_transientlab' # os.getcwd()

for root, dirs, files in os.walk(wd):
    for file in files:
        if file.endswith('.jpg') and not file.startswith('.'):
            lista.append('{:<60}{:<100}{}'.format(file, root, '\n'))

with open('listaJPG.txt', 'w') as filehandle:
    filehandle.writelines(lista)