import tkinter
import sqlite3



#The backend
class Data:
    def __init__(self):
        self.con = sqlite3.connect("data.db")
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.con.commit()


    def insert(self,title,author,year,isbn):
        self.con.cursor().execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.con.commit()


    def view(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM books")
        row=cur.fetchall()
        return row


    def search(self,title="",author="",year="",isbn=""):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        row=cur.fetchall()
        return row


    def update(self,id,title,author,year,isbn):
        self.con.cursor().execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.con.commit()



    def delete(self,id):
        self.con.cursor().execute("DELETE FROM books WHERE id=?",(id,))
        self.con.commit()
    def __del__(self):
        self.con.close()


# the Frontend

d = Data()
def Vcommand():
    a.delete(0,t.END)
    for row in d.view():
        a.insert(t.END,row)
    global tre
    tre = False

def Scommand():
    a.delete(0,t.END)
    for r in d.search(input_ti.get(),input_au.get(),input_ye.get(),input_is.get()):
        a.insert(t.END,r)
    global tre
    tre = True

def SelectRow(event):
    try:
        index=a.curselection()

        global selected
        selected = a.get(index)
        e1.delete(0,t.END)
        e1.insert(t.END,selected[1])
        e2.delete(0,t.END)
        e2.insert(t.END,selected[2])
        e3.delete(0,t.END)
        e3.insert(t.END,selected[3])
        e4.delete(0,t.END)
        e4.insert(t.END,selected[4])
    except:
        pass

def Acommand():
    d.insert(input_ti.get(),input_au.get(),input_ye.get(),input_is.get())
    a.delete(0,t.END)
    a.insert(t.END,(selected[0] ,input_ti.get(),input_au.get(),input_ye.get(),input_is.get()))

def Dcommand():
    d.delete(selected[0])
    if(tre):
        Scommand()
    else:
        Vcommand()

def Ucommand():
    d.update(selected[0],input_ti.get(),input_au.get(),input_ye.get(),input_is.get())
    if(tre):
        Scommand()
    else:
        Vcommand()

def clear():
    e1.delete(0,t.END)
    e2.delete(0,t.END)
    e3.delete(0,t.END)
    e4.delete(0,t.END)

window = tkinter.Tk()
t = tkinter
window.title("BookKeeper")
l1 = t.Label(window, text="Title:")
l1.grid(row=0,column=0, columnspan=2)
l2 = t.Label(window, text="Author:")
l2.grid(row=1,column=0, columnspan=2)
l3 = t.Label(window, text="Year:")
l3.grid(row=2,column=0, columnspan=2)
l4 = t.Label(window, text="ISBN:")
l4.grid(row=3,column=0, columnspan=2)


input_ti = t.StringVar()
e1= t.Entry(window, textvariable=input_ti)
e1.grid(row=0,column=1, columnspan=2)
input_au = t.StringVar()
e2= t.Entry(window, textvariable=input_au)
e2.grid(row=1,column=1, columnspan=2)
input_ye = t.StringVar()
e3= t.Entry(window, textvariable= input_ye)
e3.grid(row=2,column=1, columnspan=2)
input_is = t.StringVar()
e4= t.Entry(window, textvariable=input_is)
e4.grid(row=3,column=1, columnspan=2)

a = t.Listbox(window , width=30, height=15)
a.grid(row=0,column=3,rowspan=4, columnspan=4)

s= t.Scrollbar(window)
s.grid(row=0,column=6,rowspan=4)

a.configure(yscrollcommand=s.set)
s.configure(command=a.yview)

a.bind('<<ListboxSelect>>',SelectRow)

b1=t.Button(window,text="View All", width=9,command=Vcommand, bg='black', fg='white')
b1.grid(row=4,column=0)
b2=t.Button(window,text="Search",width=9, command=Scommand, bg='white', fg='black')
b2.grid(row=4,column=1)
b3=t.Button(window,text="Add", width=9, command=Acommand, bg='green', fg='black')
b3.grid(row=4,column=2)
b4=t.Button(window,text="Delete", width=9, command=Dcommand, bg='red', fg='white')
b4.grid(row=4,column=3)
b5=t.Button(window,text="Update", width=9, command=Ucommand, bg='yellow', fg='black')
b5.grid(row=4,column=4)
b6=t.Button(window,text="Close", width=9, command=window.destroy, bg='blue', fg='white')
b6.grid(row=4,column=5)
b7=t.Button(window,text="Clear",width=4, command=clear)
b7.grid(row=3,column=0,rowspan=2)

window.mainloop()

