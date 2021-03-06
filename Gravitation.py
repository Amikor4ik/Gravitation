from tkinter import *
from tkinter import filedialog as fd
import os
import sys
import clr
sys.path.append('C:\\Users\\klima\\Documents\\Gravitation\\')
clr.AddReference('EasyExploits')
import EasyExploits as ex
module = ex.Module()
root = Tk()
root.geometry('500x300')
root.title('Gravitation')
root.config(background='#403f3f')
root.iconbitmap('icon.ico')


def open_file():
    file_name = fd.askopenfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("LUA files", "*.lua")))
    f = open(file_name)
    file_text = f.read()
    txt.delete('1.0', 'end')
    txt.insert(INSERT, file_text)
    f.close()


def open_script():
    r1 = option_R.get()
    file = open('scripts\\' + r1, 'r')
    file_text = file.read()
    txt.delete('1.0', 'end')
    txt.insert(INSERT, file_text)
    file.close()


def save():
    file_name = fd.asksaveasfilename()
    f = open(file_name, 'w')
    text = txt.get('1.0', 'end')
    f.write(text)
    f.close()


def execute():
    script = txt.get('1.0', 'end')
    module.ExecuteScript(script)


def inject():
    module.LaunchExploit()


def clear():
    txt.delete('1.0', 'end')


files = os.listdir('scripts')
files = filter(lambda x: x.endswith('.txt'), files)
option_R = StringVar()
a = 0
y = 75
s = []
for file in files:
    rdbtn = Radiobutton(root, command=open_script, text=file, variable=option_R,
                        value=file, background='#403f3f', foreground='#d3d7e0')
    rdbtn.place(x=335, y=y)
    s += [rdbtn]
    y += 20
backgroundlbl = Label(root, background='#2f3136', width=71, height=4)
backgroundlbl.place(x=0, y=0)
namelbl = Label(root, text='Gravitation', background='#2f3136',
                foreground='#d3d7e0', font=('Arial Bold', 40))
namelbl.place(x=0, y=0)
txt = Text(root, bd=3, width=40, height=10)
txt.place(x=0, y=70)
clear_btn = Button(root, text='Clear', command=clear)
clear_btn.place(x=179, y=240)
exec_btn = Button(root, text='Execute', command=execute)
exec_btn.place(x=5, y=240)
inj_btn = Button(root, text='Inject', command=inject)
inj_btn.place(x=290, y=240)
save_btn = Button(root, text='Save file', command=save)
save_btn.place(x=60, y=240)
open_btn = Button(root, text="Open file", command=open_file)
open_btn.place(x=117, y=240)
root.mainloop()
