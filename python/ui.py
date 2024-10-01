logo = " \n\
                                                             .'.         /   \           /    '.  \n\
  _______________________________________________._ _.'.   .'   '.      /     \        .'       |     \n\
    | | / /_\ |\ ||_ ||_ |\ | | |   /_\ |_/        '    '.'       '.   /       \     .'         |    \n\
    | | \/   \| \|__|||_ | \| | |_ /   \|_/                         \..         \   /           '.     \n\
"
print(logo)

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
import argparse
import os
import re
from zipfile import ZipFile
import time
import shutil

import electrical_calculators as ec

cwd = os.getcwd()

parser = argparse.ArgumentParser(description='transientlab main program')
parser.add_argument('--ui', choices=['txt', 'tkinter'], action='store', type=str, help='mode selection')
parser.add_argument('--var', action='store', nargs='*', type=float, help='float variables')
args = parser.parse_args()

print("gui: ", args.ui)
print("var: ", args.var)

# text ui
if args.ui == 'txt':
    ec.calc_wire_loading_time()
    ec.calc_voltage_drop()
    exit("\nGoodbye")

if args.ui == 'tkinter':
    # graphical ui
    PROGRAM_TITLE = "transientlab"
    CODEFONT  = ("Courier New", 10)
    pages = [PROGRAM_TITLE, 'FFT', 'Cables', 'Sound', 'Signals']
    intro_text= "this is a manual or some kind of introduction"
    class tkinterApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            
            # __init__ function for class Tk
            tk.Tk.__init__(self, *args, **kwargs)
            
            # creating a container
            container = tk.Frame(self) 
            container.pack(side = "top", fill = "both", expand = True)

            container.grid_rowconfigure(0, weight = 1)
            container.grid_columnconfigure(0, weight = 1)

            self.frames = {} 
            
            for F in (StartPage, FFT_page, Cables_page, Sound_page, Signals_page):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row = 0, column = 0, sticky ="nsew")
            self.show_frame(StartPage)

            self.title(PROGRAM_TITLE)
        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()
        

    row_height = 25
    col_width = 120
    txtn = 0

    class StartPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)  
            # menu
            button1 = ttk.Button(self, text =pages[1], command = lambda : controller.show_frame(FFT_page))
            button1.place(x=10, y=row_height*1, width=80, height=row_height)
            button2 = ttk.Button(self, text =pages[2], command = lambda : controller.show_frame(Cables_page))
            button2.place(x=10, y=row_height*2, width=80, height=row_height)
            button3 = ttk.Button(self, text =pages[3], command = lambda : controller.show_frame(Sound_page))
            button3.place(x=10, y=row_height*3, width=80, height=row_height)
            button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Signals_page))
            button4.place(x=10, y=row_height*4, width=80, height=row_height)
            separator = ttk.Separator(self, orient='vertical')
            separator.place(x=100, rely=0, relwidth=0.2, relheight=1)

            # start page
            self.img = tk.PhotoImage(file="logo-clean-txt-stamp.png")
            ttk.Label(self, image=self.img).place(x=120, y=0)
            ttk.Label(self, text=intro_text, font=CODEFONT).place(x=120, y=100)
            
            
    class FFT_page(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)  
            # menu
            label = ttk.Label(self, text =pages[0], font = CODEFONT)
            label.place(x=0, y=0)
            button1 = ttk.Button(self, text =pages[1], command = lambda : controller.show_frame(FFT_page))
            button1.place(x=10, y=row_height*1, width=80, height=row_height)
            button2 = ttk.Button(self, text =pages[2], command = lambda : controller.show_frame(Cables_page))
            button2.place(x=10, y=row_height*2, width=80, height=row_height)
            button3 = ttk.Button(self, text =pages[3], command = lambda : controller.show_frame(Sound_page))
            button3.place(x=10, y=row_height*3, width=80, height=row_height)
            button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Signals_page))
            button4.place(x=10, y=row_height*4, width=80, height=row_height)
            separator = ttk.Separator(self, orient='vertical')
            separator.place(x=100, rely=0, relwidth=0.2, relheight=1)

            # page specific
            def select_file():
                filetypes = (
                    ('All files', '*.*'),
                    ('wave files', '*.wav'),
                    ('dat files', '*.dat'),
                    ('text files', '*.txt')
                )
                filename = filedialog.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
                print(filename)
                return filename  
            
            label1 = ttk.Label(self, text ='FFT calculation', font = CODEFONT)
            label1.place(x=col_width, y=0)
            # fft1
            file1 = tk.StringVar()
            open_button1 = ttk.Button(self, text='Select file', command=select_file)
            open_button1.place(x=col_width, y=row_height)
            labelf1 = ttk.Label(self, text =file1.get(), font = CODEFONT)
            labelf1.place(x=2*col_width, y=row_height)
            scale1 = tk.StringVar()

            # fft2
            file2 = tk.StringVar()
            open_button2 = ttk.Button(self, text='Select file', textvariable=file2)
            open_button2.place(x=col_width, y=2*row_height)
            labelf2 = ttk.Label(self, text =file2.get(), font = CODEFONT)
            scale2 = tk.StringVar()


    class Cables_page(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)  
            tk.Frame.__init__(self, parent)  
            # menu
            label = ttk.Label(self, text =pages[0], font = CODEFONT)
            label.place(x=0, y=0)
            button1 = ttk.Button(self, text =pages[1], command = lambda : controller.show_frame(FFT_page))
            button1.place(x=10, y=row_height*1, width=80, height=row_height)
            button2 = ttk.Button(self, text =pages[2], command = lambda : controller.show_frame(Cables_page))
            button2.place(x=10, y=row_height*2, width=80, height=row_height)
            button3 = ttk.Button(self, text =pages[3], command = lambda : controller.show_frame(Sound_page))
            button3.place(x=10, y=row_height*3, width=80, height=row_height)
            button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Signals_page))
            button4.place(x=10, y=row_height*4, width=80, height=row_height)
            separator = ttk.Separator(self, orient='vertical')
            separator.place(x=100, rely=0, relwidth=0.2, relheight=1)


            # page specific
            label1 = ttk.Label(self, text ='Cable parameters', font = CODEFONT)
            label1.place(x=col_width, y=0)
            e2 = tk.StringVar()
            entry2 = ttk.Entry(self, textvariable=e2)
            entry2.place(x=110, y = 10, width=50, height=25)

    class Sound_page(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)  
            # menu
            label = ttk.Label(self, text =pages[0], font = CODEFONT)
            label.place(x=0, y=0)
            button1 = ttk.Button(self, text =pages[1], command = lambda : controller.show_frame(FFT_page))
            button1.place(x=10, y=row_height*1, width=80, height=row_height)
            button2 = ttk.Button(self, text =pages[2], command = lambda : controller.show_frame(Cables_page))
            button2.place(x=10, y=row_height*2, width=80, height=row_height)
            button3 = ttk.Button(self, text =pages[3], command = lambda : controller.show_frame(Sound_page))
            button3.place(x=10, y=row_height*3, width=80, height=row_height)
            button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Signals_page))
            button4.place(x=10, y=row_height*4, width=80, height=row_height)
            separator = ttk.Separator(self, orient='vertical')
            separator.place(x=100, rely=0, relwidth=0.2, relheight=1)

            # page specific          
            label1 = ttk.Label(self, text ='Sound calculators', font = CODEFONT)
            label1.place(x=col_width, y=0)

    class Signals_page(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)  
            # menu
            label = ttk.Label(self, text =pages[0], font = CODEFONT)
            label.place(x=0, y=0)
            button1 = ttk.Button(self, text =pages[1], command = lambda : controller.show_frame(FFT_page))
            button1.place(x=10, y=row_height*1, width=80, height=row_height)
            button2 = ttk.Button(self, text =pages[2], command = lambda : controller.show_frame(Cables_page))
            button2.place(x=10, y=row_height*2, width=80, height=row_height)
            button3 = ttk.Button(self, text =pages[3], command = lambda : controller.show_frame(Sound_page))
            button3.place(x=10, y=row_height*3, width=80, height=row_height)
            button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Signals_page))
            button4.place(x=10, y=row_height*4, width=80, height=row_height)
            separator = ttk.Separator(self, orient='vertical')
            separator.place(x=100, rely=0, relwidth=0.2, relheight=1)

            # page specific          
            label1 = ttk.Label(self, text ='Signals generator', font = CODEFONT)
            label1.place(x=col_width, y=0)

    app = tkinterApp()
    def update():
        app.after(100, update)
    app.geometry("800x600")
    app.after(100, update)
    app.mainloop()
    exit()
