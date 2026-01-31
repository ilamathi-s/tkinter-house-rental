import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
entry_widgets=[]
def saved():
    nbutton=tk.Toplevel(root)
    nbutton.title("DATABASE SAVING")
    l=ttk.Label(nbutton,text="YOUR DATA IS SAVED!!")
    l.pack(padx=180,pady=180)
def open_entries_window():
    entries_window = tk.Toplevel(root)
    entries_window.title("Additional Entries")
    num_entries = 3
    for i in range(num_entries):
        la = ttk.Label(entries_window, text=f"Entry {i+1}:")
        la.grid(row=i, column=0, padx=10, pady=5)
    entry = ttk.Entry(entries_window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_widgets.append(entry)
def save_details():
    details = [
f"Place: {e1.get()}",
f"Owner Name: {e2.get()}",
f"Address: {e3.get()}",
f"Price: {e4.get()}"
]
    process_entries(details)
def process_entries(details):
    output_window = tk.Toplevel(root)
    output_window.title("AVAILABILITY ")
    output_label = tk.Label(output_window, text="Available house:")
    output_label.pack(padx=200, pady=200)
    for detail in details:
        entry_label = tk.Label(output_window, text=f" {detail}")
        entry_label.pack(padx=200, pady=200)
def owner():
    root = Tk(className='OWNER DETAILS')
    root.geometry("800x500")
    root.configure(bg ='light blue')
    global e1
    global e2
    global e3
    global e4
    tk.Label(root, text="PLACE").place(x=10, y=40)
    Label(root, text="Owner Name").place(x=10, y=70)
    Label(root, text="ADDRESS").place(x=10, y=100)  
    Label(root, text="Price").place(x=10, y=130)
    e1 = Entry(root)
    e1.place(x=140, y=40)
    e2 = Entry(root)
    e2.place(x=140, y=70)   
    e3 = Entry(root)
    e3.place(x=140, y=100)
    e4 = Entry(root)
    e4.place(x=140, y=130)
    Button(root, text="INDIVIDUAL",height=3, width= 13).place(x=30, y=160)
    Button(root, text="PENTHOUSE",height=3, width= 13).place(x=140, y=160)
    Button(root, text="OTHERS",height=3, width= 13).place(x=250, y=160)
    Radiobutton(root,text="Bachelar",value=1).place(x=50,y=250)
    Radiobutton(root,text="Family",value=2).place(x=50,y=270)
    Button(root,text="SAVE",height=3,width=12,command=saved).place(x=245,y=300)
def tenant():
    root= Tk(className='TENANT')
    root.geometry("800x500")
    root.configure(bg='light blue')
    global e5
    global e6
    global e7
    tk.Label(root, text="PLACE").place(x=10, y=40)
    Label(root, text="EXPECTED PRIZE").place(x=10, y=70)
    Label(root, text="EXPECTED HOUSE").place(x=10, y=100)
    Radiobutton(root, text="INDIVIDUAL",value=1).place(x=30, y=160)
    Radiobutton(root, text="PENTHOUSE",value=2).place(x=140, y=160)
    Radiobutton(root, text="OTHERS",value=3).place(x=250, y=160)
    e5 = Entry(root)
    e5.place(x=140, y=40)
    e6 = Entry(root)
    e6.place(x=140, y=70)
    Label(root,text="STATUS").place(x=70,y=200)
    combo_var = tk.StringVar()
    combobox = ttk.Combobox(root, textvariable=combo_var)
    combobox['values'] = ('BACHELAR', 'FAMILY')
    combobox.pack(padx=30, pady=200)
    Button(root,text="SHOW AVAILABILITY",height=4,width=14,command=lambda: process_entries(save_details)).place(x=300,y=400)
root=tk.Tk()
root.title("HOUSE RENTAL MANAGEMENT SYSTEM")
root.minsize(width = 1000, height = 700)
root.maxsize(width = 1000, height = 700)
button2 = Button(root, text = "OWNER", width = 70, height = 10,command=owner)
button2.pack(side = TOP, padx = 10, pady = 50 )
button2.pack()
button3 = Button(root, text = "TENANT", width = 70, height = 10,command=tenant)
button3.pack(side = TOP, padx = 10, pady = 100 )
button3.pack()
root.mainloop()
