import zeep
from tkinter import*

wsdl = 'http://www.dneonline.com/calculator.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.evaluation = ''
        self.one = 0
        self.two = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.one)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Result:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.multiply_button = Button(master, text="*", command=lambda: self.update("multiply"))
        self.divide_button = Button(master, text="/", command=lambda: self.update("divide"))
        self.evaluate_button = Button(master, text="=", command=lambda: self.update("evaluate"))
        self.clear_button = Button(master, text="Clear", command=lambda: self.update("clear"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.clear_button.grid(row=2, column=2, sticky=W+E)

        self.multiply_button.grid(row=3, column=0)
        self.divide_button.grid(row=3, column=1)
        self.evaluate_button.grid(row=3, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
        	if self.evaluation == '':
        		self.one = int(new_text)
        	else:
        		self.two = int(new_text)
        	return True
        except ValueError:
            return False

    def update(self, method):
        if method == "clear":
        	self.one = 0
        	self.two = 0
        	self.evaluation = ''
        elif method == "evaluate":
            if self.evaluation == "add":
            	self.one = client.service.Add(self.one, self.two)
            elif self.evaluation == "subtract":
            	self.one = client.service.Subtract(self.one, self.two)
            elif self.evaluation == "multiply":
            	self.one = client.service.Multiply(self.one, self.two)
            elif self.evaluation == "divide":
            	self.one = client.service.Divide(self.one, self.two)
            self.evaluation = ''
            self.two = 0
        else: # reset
            self.evaluation = method

        self.total_label_text.set(self.one)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()