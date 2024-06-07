import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        amount=float(entry_amount.get())
        rate=float(entry_vat.get())
        amount=amount*(1+rate/100)
        label_result.config(text=f"סכום כולל מעמ {amount:.2f}₪")
    except ValueError:
        messagebox.showerror("שגיאה","אנא הזן מספרים תקינים")

root = tk.Tk()
root.title("מחשבון מעמ")
tk.Label(root,text="סכום לפני מעמ:").grid(row=0,column=0,padx=10,pady=10)
entry_amount=tk.Entry(root)
entry_amount.grid(row=0,column=1,padx=10,pady=10)
tk.Label(root,text="אחוז המעמ:").grid(row=1,column=0,padx=10,pady=10)
entry_vat=tk.Entry(root)
entry_vat.grid(row=1,column=1,padx=10,pady=10)
tk.Button(root,text="חשב",command=calculate).grid(row=2,column=0,columnspan=2,pady=10)
label_result=tk.Label(root,text="סכום כולל מעמ:")
label_result.grid(row=3,column=0,columnspan=2,pady=10)
root.mainloop()
