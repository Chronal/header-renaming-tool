#! /usr/bin/env python

import argparse
import csv

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

program_name = "Header Renaming tool"

parser = argparse.ArgumentParser(
            prog=program_name,
            description="Simple gui program to rename the headers of a csv file")

parser.add_argument("input_file")
parser.add_argument("output_file")

args = parser.parse_args()

with open(args.input_file, "r") as f:
    reader = csv.reader(f, delimiter=";")
    headers = next(reader)
    remaining_rows = list(reader)

new_headers = []

def build_gui(headers):
    root = Tk()
    root.title(program_name)
    for i in range(0, len(headers) + 1):
        root.columnconfigure(i, weight=1)

    style = ttk.Style()
    
    frame = ttk.Frame(root, padding="3 3 12 12")
    frame.grid(column=0, row=0, sticky=(N, E, S, W))
    
    current = ttk.Label(frame, text="Current header label:").grid(row=0,column=0, sticky=E)
    
    ttk.Label(frame, text="New header label:").grid(row=1,column=0,sticky=E)

    for (index, header) in enumerate(headers, start=1):
        current = Label(frame, text=header)
        current.grid(row=0,column=index)

        new_var = StringVar()
        new_headers.append(new_var)
        t = Entry(frame, text=new_var)
        t.grid(row=1,column=index)
        t.insert(0, header)

    def write_new_headers():
        with open(args.output_file, "w+") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([x.get() for x in new_headers])
            writer.writerows(remaining_rows)
            f.flush()
        messagebox.showinfo(program_name, message="Finished renaming headers!")

    button = ttk.Button(frame, text="Do Renaming", command=write_new_headers)
    button.grid(row=3)

    root.mainloop()

def run_gui(gui):
    gui.mainloop()

gui = build_gui(headers)
run_gui(gui)
