# date calc project
import datetime
from datetime import timedelta
# window_1 & Widgets
from tkinter import *
### create instance of a window.
window_1 = Tk()  # window_1 with 6 labels
#### static properties.
window_1.wm_iconbitmap('beatnik.ico')  # set window_1 icon
window_1.title("Crazy Like A Fool")
window_1.geometry("450x320")
### event handlers.


def set_year():
    year = v.get()
    return year


def click_4():
    year = set_year()
    day_cycle = entry_3.get()
    month_1 = (listbox_1.curselection()[0]) + 1  # passes integer
    day_1 = int(entry_1.get())
    month_2 = (listbox_2.curselection()[0]) + 1  # passes integer
    day_2 = int(entry_2.get())
    d = datetime.date(year, month_1, day_1)
    print(("date one ", d))
    c = datetime.date(year, month_2, day_2)
    print(("date two ", c))
    x = c - d
    days_diff = x.days
    print(("days cycle", day_cycle))
    #print(type(days_diff))###<-toggle test type line(for variable)
    weeks_diff = days_diff // 7
    weeks_days_diff = (weeks_diff, (days_diff - (weeks_diff * 7)))
    print(("number of days between date one and date two ", days_diff))
    print((str(weeks_diff) + " Weeks and " + str(weeks_days_diff[1]) + " Days"))
    period = int(day_cycle)
    periods = days_diff // period
    print()
    print(("the date from ", d, "every", period, "days"))
    date_format = '%d-%m-%Y'
    for delta in range(period, (periods * period + 1), period):
        x = d + timedelta(delta)
        p = x.strftime(date_format)
        q = x.strftime('%B %d %Y')
        listbox_3.insert(END, q)
        print((p, '*', '%s-%s-%s' % (x.day, x.month, x.year)))
v = IntVar()
v.set(2018)  # initializing the choice

r1 = Radiobutton(window_1,
                 text="Last year",
                 variable=v,
                 command=set_year,
                 value=2017).grid(row=0, column=0)

r2 = Radiobutton(window_1,
                 text="This year",
                 variable=v,
                 command=set_year,
                 value=2018).grid(row=0, column=3)        

r3 = Radiobutton(window_1,
                 text="Next year",
                 variable=v,
                 command=set_year,
                 value=2019).grid(row=0, column=4)
### frame_1 widgets.
frame_1 = Frame(window_1)  # frame 1 with 5 widgets
label_1a = Label(frame_1, relief='solid', width=17)
### listbow_1 and static attributes.
listbox_1 = Listbox(frame_1, exportselection=0, width=12, height=12)
for item in ['January', 'Febuary', 'March',
             'April', 'May', 'June',
             'July', 'August', 'September',
             'October', 'November', 'December']:
    listbox_1.insert(END, item)
label_2a = Label(frame_1, relief='groove', width=10)
entry_1 = Entry(frame_1, width=2)
### frame_2 widgets.
frame_2 = Frame(window_1)  # frame 2 with 5 widgets
label_1b = Label(frame_2, relief='solid', width=16)
### listbow_2 and static attributes.
listbox_2 = Listbox(frame_2, exportselection=0, width=12, height=12)
for item in ['January', 'Febuary', 'March',
             'April', 'May', 'June',
             'July', 'August', 'September',
             'October', 'November', 'December']:
    listbox_2.insert(END, item)
label_2b = Label(frame_2, relief='groove', width=10)
entry_2 = Entry(frame_2, width=2)
### frame_3 wigets
frame_3 = Frame(window_1)
label_3a = Label(frame_3, relief='solid', width=18)
listbox_3 = Listbox(frame_3, width=20, height=14)
label_3b = Label(frame_3, relief='groove', width=12)
entry_3 = Entry(frame_3, width=2)
### button and entry wigets
calcBtn = Button(window_1, width=20, command=click_4)
### Static properties labels and buttons
label_1a.configure(text="Start of Period month")
label_2a.configure(text="Start day")
label_1b.configure(text="End of period month")
label_2b.configure(text="End day")
label_3a.configure(text="Date's of cycle output")
label_3b.configure(text="Days for cycle")
calcBtn.configure(text="Complete calculations")
### geometry frame_1
label_1a.grid(column=0, row=1)
frame_1.grid(column=0, row=2)
listbox_1.grid(column=0, row=2)
label_2a.grid(column=0, row=3)
entry_1.grid(column=1, row=3)
### geometry frame_2
label_1b.grid(column=3, row=1)
frame_2.grid(column=3, row=2)
listbox_2.grid(column=3, row=2)
label_2b.grid(column=3, row=3)
entry_2.grid(column=4, row=3)
### geometry frame_3
label_3a.grid(column=4, row=1)
frame_3.grid(column=4, row=2)
listbox_3.grid(column=4, row=2)
label_3b.grid(column=4, row=3)
entry_3.grid(column=5, row=3)
### geometry calc button
calcBtn.grid(column=0, row=5)
### sustain window.
window_1.mainloop()
