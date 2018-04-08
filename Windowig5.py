# window_1 & Widgets
from tkinter import *
### create instance of a window.
window_1 = Tk()# window_1 with 2 frames and three buttons

#### static properties.
window_1.wm_iconbitmap('beatnik.ico')#set window_1 icon
window_1.title("Crazy Like A Fool")
window_1.geometry("450x300")

### event handlers.
entered_1 = StringVar()
entered_2 = StringVar()
month_1 = StringVar()
month_2 = StringVar()
def test():
    t = entry_1.get()
    
def click_1():
    month_1 = listbox_1.get('active')
    ent_1 = entry_1.get()
    entered_1 = str(ent_1)
    show_1 = (month_1 + " " + entered_1)
    print(show_1)
    return show_1
   
   
def click_2():
    month_2 = listbox_2.get('active')
    ent_2 = entry_2.get()
    entered_2 = str(ent_2)
    show_2 = (month_2 + " " + entered_2)
    print(show_2)
    return show_2

def click_3():
    print("I am Button three and I have been clicked")
def click_4():
    show_4 = click_1()+click_2()
    # code to calculate cycle date here
    print(show_4) 
    print("I am Button four and I have been clicked")
print(entered_1)
print(month_2)

### frame_1 widgets.
frame_1 = Frame(window_1)# frame 1 with 5 widgets
label_1a = Label(frame_1, relief = 'solid', width = 17)
label_2a = Label(frame_1, relief = 'groove', width = 10)

### frame_2 widgets.
frame_2 = Frame(window_1)# frame 2 with 5 widgets
label_1b = Label(frame_2, relief = 'solid', width = 16)
label_2b = Label(frame_2, relief = 'groove', width = 10)

### frame_3 wigets
frame_3 = Frame(window_1)
label_3a = Label(frame_3, relief = 'solid', width = 18)
listbox_3 = Listbox(frame_3, width = 12, height = 12)
label_3b = Label(frame_3, relief = 'groove', width = 12)


### listbow_1 and static attributes.
listbox_1 = Listbox(frame_1, width = 12, height = 12)
for item in ['January','Febuary','March',
             'April','May','June',
             'July','August','September',
             'October','November','December']:
    listbox_1.insert(END,item)

### listbow_2 and static attributes.
listbox_2 = Listbox(frame_2, width = 12, height = 12)
for item in ['January','Febuary','March',
             'April','May','June',
             'July','August','September',
             'October','November','December']:
    listbox_2.insert(END,item)

### button and entry wigets
entry_1 = Entry(frame_1, width = 2)
getBtn_1 = Button(frame_1, width = 12, command = click_1)
entry_2 = Entry(frame_2, width = 2)
getBtn_2 = Button(frame_2, width = 12, command = click_2)
entry_3 = Entry(frame_3, width = 2)
getBtn_3 =Button(frame_3, width = 12, command = click_3)
resBtn = Button(window_1, width = 20, command = click_4)

### Static properties labels and buttons
label_1a.configure(text = "Start of Period month")
label_2a.configure(text = "Start day")
getBtn_1.configure(text = "Confirm")
label_1b.configure(text = "End of period month")
label_2b.configure(text = "End day")
getBtn_2.configure(text = "Confirm")
label_3a.configure(text = "Date's of cycle output")
label_3b.configure(text = "Days for cycle")
getBtn_3.configure(text = "Confirm")
resBtn.configure(text = "Complete calculations")

### geometry frame_1
frame_1.grid  (column = 0, row = 1)
label_1a.grid (column = 0, row = 0)
label_2a.grid (column = 0, row = 2)
listbox_1.grid(column = 0, row = 1)
getBtn_1.grid  (column = 0, row = 3)
entry_1.grid  (column = 1, row = 2)

### geometry frame_2
frame_2.grid  (column = 3, row = 1)
label_1b.grid (column = 3, row = 0)
label_2b.grid (column = 3, row = 2)
listbox_2.grid(column = 3, row = 1)
getBtn_2.grid  (column = 3, row = 3)
entry_2.grid  (column = 4, row = 2)

### geometry frame_3
frame_3.grid(column = 4, row = 1)
label_3a.grid(column = 4, row = 0)
label_3b.grid(column = 4, row = 2)
listbox_3.grid(column = 4, row = 1)
getBtn_3.grid(column = 4, row = 3)
entry_3.grid(column = 5, row = 2)

### dynamic properties.
resBtn.grid   (column = 0, row = 4)

### sustain window.
window_1.mainloop()
