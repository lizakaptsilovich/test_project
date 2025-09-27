from tkinter import *

root=Tk()
root.geometry("300x200")

a = Entry(root, width=15, font=('Arial', 30))
a.pack()
b = Button(root, text = 'Test button')
b.pack()
c = Label(root, bg='white', font=('Arial', 30), width=15)
c.pack()
def press_button(event):
    s=a.get()
    s=s.split()
    s.sort()
    c['text'] = '/'.join(s)
b.bind('<Button-1>', press_button)

root.mainloop()

#------------------

# Label(root, text="Логин:").grid(row=0, column=0)
# Entry(root).grid(row=0, column=1)
#
# Label(root, text="Пароль:").grid(row=1, column=0)
# Entry(root, show="*").grid(row=1, column=1)
#
# Button(root, text="Войти").grid(row=2, column=0, columnspan=2)
#
# root.mainloop()

#-------------------

# root = Tk()
# root.geometry("300x200")
#
# Button(root, text="Кнопка", bg="orange").place(x=50, y=50)
# Entry(root).place(x=50, y=100, width=200)
#
# root.mainloop()