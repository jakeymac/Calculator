import math


class Entries:
    def __init__(self):

        log = open("log.txt",'a')
        log.write('\n<-----New Session----->\n')
        log.close()

        self.top_entry = ""
        self.bottom_entry = ""
        self.current_operator = ""
        self.clear_button_state = "AC"

    def edit_entry(self,value):
        if value == "delete":
            if self.bottom_entry != "": #Making sure the entry itself isn't empty
                self.bottom_entry = self.bottom_entry[0:-1]
        elif value == ".":
            if "." not in self.bottom_entry: #Checking if the number is already a decimal
                self.bottom_entry += "."
        else:
            if self.current_operator == "":
                self.top_entry = ""
            self.bottom_entry += value

    def clear_entry(self):
        if self.bottom_entry != "":
            self.bottom_entry = ""

        elif self.top_entry != "":
            self.top_entry = ""
            self.current_operator = ""
        

    def add_operator(self,operator):
        if self.top_entry == "":
            if self.bottom_entry != "":
                self.top_entry = self.bottom_entry
                self.current_operator = operator
                self.bottom_entry = ""
                    
        elif self.bottom_entry == "": #If top entry is already full ``
            self.current_operator = operator

        elif self.bottom_entry != "":
            self.equals_operation()
            self.current_operator = operator

    def equals_operation(self):
        if self.top_entry != "" and self.bottom_entry != "":
            if "." in self.top_entry or "." in self.bottom_entry:
                self.top_number = float(self.top_entry)
                self.bottom_number = float(self.bottom_entry)
            else:
                self.top_number = int(self.top_entry)
                self.bottom_number = int(self.bottom_entry)
            
            if self.top_entry != "" and self.bottom_entry != "":
                if self.current_operator == "+":
                    self.top_entry = str(self.top_number + self.bottom_number)
                    self.bottom_entry = ""
                    self.current_operator = ""
                    self.add_log_entry(f"{self.top_number} + {self.bottom_number} = {self.top_entry}")

                elif self.current_operator == "-":
                    self.top_entry = str(self.top_number - self.bottom_number)
                    self.bottom_entry = ""
                    self.current_operator = ""
                    self.add_log_entry(f"{self.top_number} - {self.bottom_number} = {self.top_entry}")


                elif self.current_operator == "X":
                    self.top_entry = str(self.top_number * self.bottom_number)
                    self.bottom_entry = ""
                    self.current_operator = ""
                    self.add_log_entry(f"{self.top_number} X {self.bottom_number} = {self.top_entry}")


                elif self.current_operator == "/":
                    self.top_entry = str(self.top_number / self.bottom_number)
                    self.bottom_entry = ""
                    self.current_operator = ""
                    self.add_log_entry(f"{self.top_number} / {self.bottom_number} = {self.top_entry}")
                
                elif self.current_operator == "^":
                    self.top_entry = str(math.pow(self.top_number,self.bottom_number))
                    self.bottom_entry = ""
                    self.current_operator = ""
                    self.add_log_entry(f"{self.top_number} ^ {self.bottom_number} = {self.top_entry}")

            if self.top_entry[-2:] == '.0':
                self.top_entry = self.top_entry[0:-2]


    def exponent_operation(self,exponent):
        if exponent == "exponent button":
            if self.bottom_entry != "":
                self.top_entry = self.bottom_entry
                self.bottom_entry = ""
            if self.bottom_entry != "" or self.top_entry != "":
                self.current_operator = "^"

        else:
            if self.bottom_entry != "":
                if "." in self.bottom_entry:
                    self.bottom_number = float(self.bottom_entry)
                    self.top_entry = str(math.pow(self.bottom_number,exponent))
                else:
                    self.bottom_number = int(self.bottom_entry)
                    self.top_entry = str(int(math.pow(self.bottom_number,exponent)))

                self.add_log_entry(f"{self.bottom_number} ^ {exponent} = {self.top_entry}")
                self.bottom_entry = ""
                
            elif self.top_entry != "":
                if "." in self.top_entry:
                    self.top_number = float(self.top_entry)
                    self.top_entry = str(math.pow(self.top_number,exponent))
                    
                else:
                    self.top_number = int(self.top_entry)
                    self.top_entry = str(int(math.pow(self.top_number,exponent)))

                self.add_log_entry(f"{self.top_number} ^ {exponent} = {self.top_entry}")
            
    def add_log_entry(self,text):
        log = open('log.txt','a')
        
        log.write(f'{text}\n')
        log.close()   
    
    def get_top_entry(self):
        return self.top_entry

    def get_bottom_entry(self):
        return self.bottom_entry

    def get_operator(self):
        if self.current_operator == "X": 
            return "x"
        return self.current_operator

    def get_current_clear_button(self):
        if self.bottom_entry == "":
            self.clear_button_state = "AC"
        else:
            self.clear_button_state = " C"
        return self.clear_button_state 
