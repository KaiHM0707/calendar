from tkinter import *
import calendar


def make_cal(recieve_year):
    scr2 = Tk()
    scr2.title("CALENDAR")
    scr2.configure(background="lightblue")
    scr2.geometry("800x800")

    cal_content = calendar.calendar(recieve_year)
    Display = Label(scr2, text=cal_content, font="times", fg="black", bg="gray")
    Display.pack(side=TOP)

    scr2.mainloop()






scr = Tk()
scr.geometry("500x500")
scr.title("Calender")
scr.configure(background="gray")

title = Label(scr, text="Calender", font=("times", 70), fg="black", bg="lightgreen")
title.pack(side=TOP)

year = Label(scr, text="What year?", font=("times", 15), fg="blue", bg="pink").place_configure(x=190,y=200)

year_input = Entry(scr, width=20).place_configure(x=190, y=230)
get_year = year_input.get()


show_calender = Button(scr, text="show calender", command=lambda:make_cal(get_year) width=40, bg="green", fg="red").place(x=120,y=420)
exit = Button(scr,text="Exit", bg="red", fg="black", command=exit)
exit.pack(side=BOTTOM)




scr.mainloop()