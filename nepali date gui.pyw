import nepali_datetime #pip install nepali-datetime
import tkinter

date = nepali_datetime.date.today().strftime("%A %d. %B %Y") #prints out in 'Tuesday 12. bhadau 2002' format

root = tkinter.Tk()
screen_width =  root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (130, 20, screen_width-140, 0))

lbl_date = tkinter.Label(root, text = date).pack()

root.after(3000, lambda: root.destroy())
root.mainloop()
