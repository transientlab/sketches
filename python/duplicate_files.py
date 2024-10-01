# duplicate files

import sys, os, pandas

wd = "/Users/kr315/Desktop/_dev/lumistone"
cwd = os.getcwd()
roots, filenames, sizes = [], [], []
for root, dirs, files in os.walk(wd):
    for f in files:
        try:
            file_path = os.path.join(root, f)
            size = os.stat(file_path)[6]
            
            roots.append(root)
            filenames.append(f.strip())
            sizes.append(size)
        except:
            pass

df = pandas.DataFrame({
    'root'  :   roots,
    'file'  :   filenames,
    'size'  :   sizes
})

ids = df.index
print(df[ids.isin(ids[df.duplicated(subset='size')])])
# print(df)