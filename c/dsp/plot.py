import sys, os
import numpy
from matplotlib import pyplot as plt


if len(sys.argv) > 2:
    folder_name = sys.argv[1]
    print("\nLocation:\t" + folder_name)

    file_list = []
    for i in sys.argv[2:]:
        file_list.append(i)
    print("\nFiles:\t\t", file_list)

else:
    print("wrong parameters") # should be more informing


def dat_to_float_file(filename, folder_name):
    with open(os.path.join(os.getcwd(), folder_name, filename), "r") as data_file:
        lines = data_file.readlines()
        data =[float(line.rstrip()) for line in lines[1:]]
    return data

def plot_all_files(file_list, folder_name, orientation="v"):
    if orientation == "v":
        plot_figure = plt.figure(figsize=(8.0, 8.0))
    elif orientation =="h":
        plot_figure = plt.figure(figsize=(8.0, 4.0))

    file_enum, file_enum_max = 0, len(file_list)

    for each_file in file_list:
        file_enum+=1
        data = dat_to_float_file(each_file, folder_name)
        if orientation == "v":
            data_plot = plot_figure.add_subplot(file_enum_max, 1, file_enum)
        elif orientation == "h":
            data_plot = plot_figure.add_subplot(1, file_enum_max, file_enum)
        data_plot.set_ylabel(each_file)
        data_plot.plot(data)

    plot_figure.tight_layout()
    plt.show()






plot_all_files(file_list, folder_name, "v")
