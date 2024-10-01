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

# graphical ui
PROGRAM_TITLE = "transientlab"
CODEFONT  = ("Courier New", 10)
pages = [PROGRAM_TITLE, 'FFT', 'Cables', 'Sound', 'Projection']
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
        
        for F in (StartPage, FFT_page, Cables_page, Sound_page, Projection_page):
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
        # self.img = tk.PhotoImage(file="logo-clean-txt-stamp.png")
        # ttk.Label(self, image=self.img).place(x=0, y=0)  
        # menu
        button1 = ttk.Button(self, text =pages[1], command = lambda : controller.show_frame(FFT_page))
        button1.place(x=10, y=row_height*1, width=80, height=row_height)
        button2 = ttk.Button(self, text =pages[2], command = lambda : controller.show_frame(Cables_page))
        button2.place(x=10, y=row_height*2, width=80, height=row_height)
        button3 = ttk.Button(self, text =pages[3], command = lambda : controller.show_frame(Sound_page))
        button3.place(x=10, y=row_height*3, width=80, height=row_height)
        button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Projection_page))
        button4.place(x=10, y=row_height*4, width=80, height=row_height)
        separator = ttk.Separator(self, orient='vertical')
        separator.place(x=100, rely=0, width=1, relheight=1)

        # start page

        ttk.Label(self, text=intro_text, font=CODEFONT).place(x=120, y=100)

class FFT_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # self.img = tk.PhotoImage(file="logo-clean-txt-stamp.png")
        # ttk.Label(self, image=self.img).place(x=0, y=0)  
        # menu
        button1 = ttk.Button(self, text =pages[1], command = lambda : controller.show_frame(FFT_page))
        button1.place(x=10, y=row_height*1, width=80, height=row_height)
        button2 = ttk.Button(self, text =pages[2], command = lambda : controller.show_frame(Cables_page))
        button2.place(x=10, y=row_height*2, width=80, height=row_height)
        button3 = ttk.Button(self, text =pages[3], command = lambda : controller.show_frame(Sound_page))
        button3.place(x=10, y=row_height*3, width=80, height=row_height)
        button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Projection_page))
        button4.place(x=10, y=row_height*4, width=80, height=row_height)
        separator = ttk.Separator(self, orient='vertical')
        separator.place(x=100, rely=0, width=1, relheight=1)

        # start page

        ttk.Label(self, text=intro_text, font=CODEFONT).place(x=120, y=100)

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

default_start_temp = 30
default_end_temp = 90

class Cables_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Menu
        label = ttk.Label(self, text=pages[0], font=CODEFONT)
        label.place(x=0, y=0)
        button1 = ttk.Button(self, text=pages[1], command=lambda: controller.show_frame(FFT_page))
        button1.place(x=10, y=row_height*1, width=80, height=row_height)
        button2 = ttk.Button(self, text=pages[2], command=lambda: controller.show_frame(Cables_page))
        button2.place(x=10, y=row_height*2, width=80, height=row_height)
        button3 = ttk.Button(self, text=pages[3], command=lambda: controller.show_frame(Sound_page))
        button3.place(x=10, y=row_height*3, width=80, height=row_height)
        button4 = ttk.Button(self, text=pages[4], command=lambda: controller.show_frame(Projection_page))
        button4.place(x=10, y=row_height*4, width=80, height=row_height)
        separator = ttk.Separator(self, orient='vertical')
        separator.place(x=100, rely=0, relwidth=0.2, relheight=1)

        # Page-specific elements
        self.cable_material = tk.IntVar(value=1)
        self.cable_length = tk.DoubleVar()
        self.cable_xarea = tk.DoubleVar()
        self.start_temp = tk.DoubleVar(value=30)  # Default value 30
        self.end_temp = tk.DoubleVar(value=90)    # Default value 90
        self.selected_material = tk.StringVar(value="Selected Material: None")

        label1 = ttk.Label(self, text='Cable parameters', font=CODEFONT)
        label1.place(x=col_width, y=0)
        
        # Cable material selection (Radio buttons)
        material_label = ttk.Label(self, text="Select cable material:", font=CODEFONT)
        material_label.place(x=col_width, y=row_height*1)
        
        radio1 = ttk.Radiobutton(self, text="Copper", variable=self.cable_material, value=1, command=self.update_cable)
        radio1.place(x=col_width, y=row_height*2)

        radio2 = ttk.Radiobutton(self, text="Aluminum", variable=self.cable_material, value=2, command=self.update_cable)
        radio2.place(x=col_width, y=row_height*3)

        radio3 = ttk.Radiobutton(self, text="Gold", variable=self.cable_material, value=3, command=self.update_cable)
        radio3.place(x=col_width, y=row_height*4)

        radio4 = ttk.Radiobutton(self, text="Other", variable=self.cable_material, value=4, command=self.update_cable)
        radio4.place(x=col_width, y=row_height*5)

        # Cable length input
        cable_length_label = ttk.Label(self, text="Cable length (m):", font=CODEFONT)
        cable_length_label.place(x=col_width, y=row_height*6)
        
        entry_length = ttk.Entry(self, textvariable=self.cable_length)
        entry_length.place(x=3*col_width, y=row_height*7, width=100, height=25)

        # Cable cross-sectional area input
        xarea_label = ttk.Label(self, text="Cross-sectional area (mm^2):", font=CODEFONT)
        xarea_label.place(x=col_width, y=row_height*7)
        
        cable_xarea = tk.DoubleVar()
        entry_xarea = ttk.Entry(self, textvariable=self.cable_xarea)
        entry_xarea.place(x=3*col_width, y=row_height*7, width=100, height=25)

        # Start temperature input
        start_temp_label = ttk.Label(self, text="Start temperature (°C):", font=CODEFONT)
        start_temp_label.place(x=col_width, y=row_height*8)
        
        start_temp = tk.DoubleVar(value=default_start_temp)
        entry_start_temp = ttk.Entry(self, textvariable=self.start_temp)
        entry_start_temp.place(x=3*col_width, y=row_height*8, width=100, height=25)

        # End temperature input
        end_temp_label = ttk.Label(self, text="End temperature (°C):", font=CODEFONT)
        end_temp_label.place(x=col_width, y=row_height*9)
        
        end_temp = tk.DoubleVar(value=default_end_temp)
        entry_end_temp = ttk.Entry(self, textvariable=self.end_temp)
        entry_end_temp.place(x=3*col_width, y=row_height*9, width=100, height=25)

    def update_cable(self):
        material = self.cable_material.get()
        if material == 1:
            self.selected_material.set("Selected Material: Copper")
        elif material == 2:
            self.selected_material.set("Selected Material: Aluminum")
        elif material == 3:
            self.selected_material.set("Selected Material: Gold")
        else:
            self.selected_material.set("Selected Material: None")

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
        button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Projection_page))
        button4.place(x=10, y=row_height*4, width=80, height=row_height)
        separator = ttk.Separator(self, orient='vertical')
        separator.place(x=100, rely=0, relwidth=0.2, relheight=1)

        # page specific          
        label1 = ttk.Label(self, text ='Sound calculators', font = CODEFONT)
        label1.place(x=col_width, y=0)

class Projection_page(tk.Frame):
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
        button4 = ttk.Button(self, text =pages[4], command = lambda : controller.show_frame(Projection_page))
        button4.place(x=10, y=row_height*4, width=80, height=row_height)
        separator = ttk.Separator(self, orient='vertical')
        separator.place(x=100, rely=0, relwidth=0.2, relheight=1)

        # page specific          
        label1 = ttk.Label(self, text ='Throw ratio', font = CODEFONT)
        label1.place(x=col_width, y=0)

app = tkinterApp()

def update():
    app.after(100, update)
app.geometry("800x600")

app.after(100, update)
app.mainloop()
