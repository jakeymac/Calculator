import tkinter as tk
from tkinter import messagebox
import entries

class Window:
    def __init__(self,root):
        self.entries_handler = entries.Entries()

        self.root = root
        self.root.title("Calculator")

        #Handle entries and buttons
        self.top_entry = tk.Entry(self.root)
        self.top_entry.grid(row=0,column=1,columnspan=4)

        self.bottom_entry = tk.Entry(self.root)
        self.bottom_entry.grid(row=1,column=1,columnspan=4)

        #Handling other types of buttons
        self.clear_button = tk.Button(self.root,text="AC",command=self.clear_button_press)
        self.clear_button.grid(row=0,column=5)

        self.delete_button = tk.Button(self.root,text="del",command=self.delete_button_press)
        self.delete_button.grid(row=1,column=5)

        #Show log button
        self.show_log_button = tk.Button(self.root,text="Show \n Log",command=self.display_log)
        self.show_log_button.grid(row=0,rowspan=2,column=6)

        #Handle number buttons
        for button_num in range(0,10):
            new_button = tk.Button(self.root,text=str(button_num),command=lambda num = button_num:self.number_button_press(num))
            if button_num == 0:
                new_button.grid(row=5,column=2)
            elif button_num < 4:
                new_button.grid(row=2,column=button_num)
            elif button_num < 7:
                new_button.grid(row=3,column=button_num-3)
            elif button_num < 10:
                new_button.grid(row=4,column=button_num - 6)

        self.decimal_button = tk.Button(self.root,text=".",command=lambda: self.number_button_press("."))
        self.decimal_button.grid(row=5,column=1)

        #Operation buttons
        self.times_button = tk.Button(self.root,text="X",command=lambda: self.operation_button("X"))
        self.times_button.grid(row=2,column=4)

        self.divide_button = tk.Button(self.root,text="/",command=lambda: self.operation_button("/"))
        self.divide_button.grid(row=3,column=4)

        self.plus_button = tk.Button(self.root,text="+",command=lambda:self.operation_button("+"))
        self.plus_button.grid(row=4,column=4)

        self.minus_button = tk.Button(self.root,text="-",command=lambda:self.operation_button("-"))
        self.minus_button.grid(row=5,column=4)

        self.square_button = tk.Button(self.root,text="^2",command=lambda: self.exponent_button_press(2))
        self.square_button.grid(row=2,column=5)

        self.cube_button = tk.Button(self.root,text="^3",command=lambda: self.exponent_button_press(3))
        self.cube_button.grid(row=3,column=5)

        self.exponent_button = tk.Button(self.root,text="x^y",command=lambda:self.exponent_button_press("exponent button"))
        self.exponent_button.grid(row=4,column=5)

        self.equal_button = tk.Button(self.root,text="=",command=self.equal_button_press)
        self.equal_button.grid(row=5,column=3)

        
    #Handling the pressing of numbered buttons and decimal button
    def number_button_press(self,num):
        self.entries_handler.edit_entry(str(num))
        self.refresh_entries()
        
    def delete_button_press(self):
        self.entries_handler.edit_entry("delete")
        self.refresh_entries()

    def clear_button_press(self):
        self.entries_handler.clear_entry()
        self.refresh_entries()

    def equal_button_press(self):
        self.entries_handler.equals_operation()
        self.refresh_entries()

    def operation_button(self,operation):
        self.entries_handler.add_operator(operation)
        self.refresh_entries()

    def exponent_button_press(self,exponent):
        self.entries_handler.exponent_operation(exponent)
        self.refresh_entries()

    def refresh_entries(self):
        self.bottom_entry.delete(0,tk.END)
        self.bottom_entry.insert(0,self.entries_handler.get_bottom_entry())
        self.top_entry.delete(0,tk.END)
        self.top_entry.insert(0,self.entries_handler.get_top_entry() + self.entries_handler.get_operator())

        self.clear_button.config(text=self.entries_handler.get_current_clear_button())

    def display_log(self):
        print("log")
        message = ""
        with open("log.txt") as log_file:
            log_file_contents = log_file.readlines()
            #print(log_file_contents)

            breakpoint = "<-----New Session----->"
            for line in range(-1,-len(log_file_contents),-1):
                print(log_file_contents[line])
                if log_file_contents[line] != breakpoint + "\n":
                    message += log_file_contents[line]
                else:
                    break
        messagebox.showinfo(message=message)