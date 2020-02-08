from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *
import os
from PIL import Image
import numpy
import textwrap
import pytesseract


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("FNFI    #PaidLancers")
        self.minsize(700, 500)
        self.configure(bg="#5b5656")

        style = Style()
        style.configure("BW.TLabel", font=
        ('calibri', 40, 'bold'), foreground="#4d4646", background="#7fcd91")


        self.label1 = ttk.Label(self, text="Fidelity National Financial Indian", style="BW.TLabel")
        self.label1.grid(column=5, row=1, padx = 20, pady = 20)


        self.labelFrame = ttk.LabelFrame(self, text = "Choose File")
        self.labelFrame.grid(column = 5, row = 5, padx = 20, pady = 130)

        self.button()

    def button(self):
        style = Style()
        style.configure('TButton', font=
        ('calibri', 20, 'bold', 'underline'),
                        foreground='#7fcd91', background='#4d4646')

        self.button = ttk.Button(self.labelFrame, text = "Browse File", command = self.fileDialog )
        self.button.grid(column=1, row=1)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("All Files", "*.*"), ("All Files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        base = os.path.basename(self.filename)
        filename, file_extension = os.path.splitext(self.filename)
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        x = Image.open(filename + file_extension)
        count = 0
        file = open(filename + ".txt" , "a")
        while True:
            try :
                x.seek(count)
            except EOFError:
                break
            count += 1
        if count == 1:
            x.save(filename + "1.jpg")
        else:
            for y in range(0, count):
                x.seek(y)
                x.save(filename + f"{y}.jpg")

        count = 0
        while True:
            try:
                x.seek(count)
            except EOFError:
                break
            count += 1
        if count == 1:
            file.write(pytesseract.image_to_string(filename + "1.jpg"))
            os.remove(filename + "1.jpg")
        else:
            for y in range(0, count):
                file.write(pytesseract.image_to_string(filename + f"{y}.jpg"))
                os.remove(filename + f"{y}.jpg")

        file.close()
        self.label.configure(text="Successfully Completed")

if __name__ == '__main__':
    root = Root()
    root.mainloop()