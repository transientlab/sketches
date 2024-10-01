import os
import re
from zipfile import ZipFile
import time
import shutil

cwd = os.getcwd()
wd = cwd + '\\op\\'     # working directory

def create_tmp_path(file, root):
    return os.path.join(root, file)

def get_serial_number_from_am_ini(am_ini_file_path):
    with open(am_ini_file_path, 'r') as robot_data:
        for text_line in robot_data.readlines():
            if text_line.startswith('IRSerialNr='):
                serial_number = re.split('=', text_line)[-1][0:-1]
    return serial_number

def get_robot_data(config_file_path):
    homes, tool_data = [], []
    with open(config_file_path, 'r') as robot_data:
        for text_line in robot_data.readlines():
            if text_line.startswith('E6AXIS XHOME'):
                if text_line.find('{A1 0.0,A2 -90.0000,A3 90.0000,A4 0.0,A5 0.0,A6 0.0,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}') == -1:
                    homes.append(text_line[0:-1])
            if text_line.startswith('TOOL_NAME['):
                if text_line.find('=" "') == -1:
                    tool_data.append(text_line[0:-1])
            if text_line.startswith('TOOL_DATA['):
                if text_line.find('{X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0}') == -1:
                    tool_data.append(text_line[0:-1])
            if text_line.startswith('TOOL_TYPE['):
                if text_line.find('=#NONE') == -1:
                    tool_data.append(text_line[0:-1])
            if text_line.startswith('LOAD_DATA['):
                if text_line.find('{M -1.00000,CM {X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0},J {X 0.0,Y 0.0,Z 0.0}}') == -1:
                    tool_data.append(text_line[0:-1])
    return homes, tool_data

def create_call_graph(project_directory):
    list_of_src_files = []
    for root, dirs, files in os.walk(project_directory):
        for file in files:
            if file.endswith('.src') and not file.startswith('$'):
                file_name = file[0:-3]
                file_path = os.path.join(root, file)
                list_of_src_files.append([' ' + file[0:-4].lower(), file_path])
    list_of_src_files.sort()

    for i in list_of_src_files:
        if_src_called = []
        with open(i[1], 'r') as file:
            for line in file.readlines():
                txt = line.lower()
                print(txt)
                # line starts with function, maybe readlines, exclude comments, 
                for j in list_of_src_files:
                    src_called = False
                    
                    if txt.find(j[0] + '(') != -1 or txt.find(j[0] + ' (') != -1 or txt.find(j[0] + '  (') != -1 or txt.startswith(j[0]):
                        src_called = True
                    if_src_called.append(src_called)
        i.append(if_src_called)

    call_tree, never_called = [], []

    for idx, i in enumerate(list_of_src_files):
        calls = []
        for jdx, j in enumerate(i[2]):
            if j and i[0] != list_of_src_files[jdx][0]:
                calls.append(list_of_src_files[jdx][0])
        call_tree.append((i[0], calls))

    # implement never called 
    return call_tree, never_called

def extract_important_data(wd): # extract from zip
    paths_of_zipfiles = []
    for root, dirs, files in os.walk(wd):
        for file in files:
            if file.endswith('.zip'):
                file_name = file[0:-4]
                file_path = os.path.join(root, file)
                paths_of_zipfiles.append(file_path)

    tmp_folder = os.path.join(wd, "tmp")
    for file_path in paths_of_zipfiles:
        with ZipFile(file_path, 'r') as zipped_backup:
            zipped_backup.extractall(tmp_folder)
        for root, dirs, files in os.walk(tmp_folder):
            for file in files:
                if file == 'am.ini':
                    tmp_path = create_tmp_path(file, root)
                    serial_number = get_serial_number_from_am_ini(tmp_path)
                if file == '$config.dat' and root.endswith('System'):
                    tmp_path = create_tmp_path(file, root)
                    homes, tool_data = get_robot_data(tmp_path)

        call_tree, never_called = create_call_graph(tmp_folder)

        with open(file_path[0:-4] + '.txt', 'w+') as output_text_file:
            output_text_file.write(file_name + '\n')
            output_text_file.write('\nSerial number:\t' + serial_number + '\n')
            output_text_file.write('\n\nImportant, non-zero data:\n')
            for line in homes:
                output_text_file.write(line + '\n')
            output_text_file.write('\n')
            for line in tool_data:
                output_text_file.write(line + '\n')
            output_text_file.write('\n\n\n\nPrototype of call tree (not fully functional!):\n')
            for i in call_tree:
                output_text_file.write(i[0] + '\n')
                for j in i[1]:
                    output_text_file.write('\t' + j + '\n')
                output_text_file.write('\n')
            output_text_file.write('\n ---- Never called functions:\n')
            # for i in never_called:
            #     output_text_file.write(i + '\n')
        print(file_name, serial_number, tool_data, '\n')
        
        shutil.rmtree(tmp_folder)

def rename_backups(wd):
    letter = input('letters to add in the beginning: ')
    for file_name in os.listdir(wd):
        file_path = os.path.join(wd, file_name)
        if os.path.isfile(file_path):
            new_file_path = wd + '\\' + letter + re.split('_', file_name)[-2] + '.zip'
            os.rename(file_path, new_file_path)
            print(file_path, new_file_path)

# rename_backups(wd)
# extract_important_data(wd)
call_tree, never_called = create_call_graph(wd)
for i in call_tree:
    print(i[0])
    for j in i[1]:
        print('\t' + j)







''' ############################################################################
# ====================================================================================
# in the directory with backups, find all zip files, extract serial from am.ini
# add activation code extraction (some xml file)
robot_serials = []
for file_name in list_of_zipfiles:
    print(file_name)
    # extract serial number from am.ini
    with ZipFile(file_name, 'r') as zipped_backup:
        zipped_backup.extract('am.ini')
        # zipped_backup.extract('$config.dat')

    with open('am.ini', 'r') as robot_data:
        tmp_arr = []
        for text_line in robot_data.readlines():
            if text_line.startswith('IRSerialNr='):
                tmp_arr.append(file_name[-15:-4])
                tmp_arr.append(re.split('=', text_line)[-1][0:-1])
    robot_serials.append(tmp_arr)
    os.remove('am.ini')

    # extract robot data from $config.dat
    # with open('$config.dat', 'r') as robot_data:
    #     tmp_arr = []
    #     for text_line in robot_data.readlines():
    #         if text_line.startswith('E6AXIS XHOME'):
    #             print(text_line)
    
    # os.remove('$config.dat')



with open('robot_serials.txt', 'w+') as output_text_file:
    for line in robot_serials:
        output_text_file.write(line[0] + '\t\t' + line[1] + '\n')




# ====================================================================================
# call graph
# wylistuj pliki src, stworz do niego ('', [])
# sprawdzy nazwy mają poprawny format
# otworz kazdy i sprawdz odwolania do ktoregos z listy
# sprawdz ktory nie zostal wywolany
list_of_src_files = []
for root, dirs, files in os.walk(wd):
    for file in files:
        if file.endswith('.src') and not file.startswith('$'):
            file_name = file[0:-3]
            file_path = os.path.join(root, file)
            list_of_src_files.append([' ' + file[0:-4].lower(), file_path])

for i in list_of_src_files:
    if_src_called = []
    with open(i[1], 'r') as file:
        txt = file.read().lower()
        # line starts with function, maybe readlines, exclude comments, 
        for j in list_of_src_files:
            src_called = False
            
            if txt.find(j[0] + '(') != -1 or txt.find(j[0] + ' (') != -1 or txt.find(j[0] + '  (') != -1:
                src_called = True
            if_src_called.append(src_called)
    i.append(if_src_called)

for i in list_of_src_files:
    print(i[0])
    for jdx, j in enumerate(i[2]):
        if j and i[0] != list_of_src_files[jdx][0]:
           print('\t' + list_of_src_files[jdx][0])
    
# ====================================================================================
# renaming WorkVisual archiveAll, splits with '_', takes [-2], adds first letter
# use for lines with the same letter in the beginning
def rename_backups(wd):
    letter = input('letters to add in the beginning: ')
    for file_name in os.listdir(wd):
        file_path = os.path.join(wd, file_name)
        if os.path.isfile(file_path):
            new_file_path = wd + '\\' + letter + re.split('_', file_name)[-2] + '.zip'
            os.rename(file_path, new_file_path)
            print(file_path, new_file_path)





''' ############################################################################
print('\n\t ========= BYE BYE ========= ')

















# os.path.relpath(directory, root_directory)


# os.walk(directory)
# paths                 [x[0] for x in os.walk(wd)]
# directoris in x[0]    [x[1] for x in os.walk(wd)] 
# files in x[0]         [x[2] for x in os.walk(wd)] 

# for file_name in os.listdir(cwd):
#     if os.path.isfile(file_name) and file_name.endswith('.zip'):