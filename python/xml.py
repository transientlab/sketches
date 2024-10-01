import xml.etree.ElementTree as ET
import os

wd = os.getcwd()


def list_svg_files(directory):
    list_of_files = []
    for file_name in os.listdir(wd):
        if file_name.endswith('.svg'):
            list_of_files.append(file_name)
    if list_of_files == []:
        raise FileNotFoundError
    os.mkdir('no_strokes')
    return list_of_files

def remove_strokes(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Find all elements with a 'stroke' attribute and remove it
    for elem in root.iter():
        print(elem)
        if 'stroke' in elem.attrib:
            parent = elem.getparent()
            parent.remove(elem)

    # Save the modified SVG file and remove 'namespace' tag
    tree.write(svg_file)
    with open(svg_file, 'r') as svg_source:
        svg_target = open(os.path.join(os.getcwd(), 'no_strokes', svg_file), 'w+')
        for line in svg_source:
            # print(line.replace("ns0:",""))
            if ("stroke" in line) or ( "</ns0:g>" in line):
                assert True
            else:
                print(line)
                svg_target.write(line.replace("ns0:",""))
        svg_target.close()


try:
    svg_files = list_svg_files(wd)
    
    for file in svg_files:
        print(file)
        remove_strokes(file)
except FileExistsError:
    print('ERROR:\nFolder \"no_strokes\" exists in working directory, please remove it')
except FileNotFoundError:
    print('ERROR:\nNo \"svg\" files in current directory. Please provide input files.')
except ET.ParseError:
    print('ERROR:\nCorrupted \"svg\" file. Please remove it or repair.')

input()

# except 