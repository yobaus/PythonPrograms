#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 20, 2019 06:20:46 PM CST  platform: Windows NT
#I want to add a gui to my weather app, and I want to try page so this was a test of page

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Weather_support
import WhatsTheWeather

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Root (root)
    Weather_support.init(root, top)
    root.mainloop()

w = None
def create_Root(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Root (w)
    Weather_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Root():
    global w
    w.destroy()
    w = None




class Root:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {@Adobe Heiti Std R} -size 14 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font17 = "-family {Segoe UI} -size 12 -weight normal -slant "   \
            "roman -underline 0 -overstrike 0"
        top.geometry("872x727+667+176")
        top.minsize(120, 1)
        top.maxsize(4654, 1661)
        top.resizable(0, 0)
        top.title("This Weeks Weather")
        top.configure(borderwidth="2")
        top.configure(background="#80ffff")

        self.MainBodyFrame = tk.Frame(top)
        self.MainBodyFrame.place(relx=0.011, rely=0.261, relheight=0.667
                , relwidth=0.969)
        self.MainBodyFrame.configure(relief='groove')
        self.MainBodyFrame.configure(borderwidth="2")
        self.MainBodyFrame.configure(relief="groove")
        self.MainBodyFrame.configure(background="#1c5464")

        self.DayOneFrame = tk.Frame(self.MainBodyFrame)
        self.DayOneFrame.place(relx=0.012, rely=0.021, relheight=0.959
                , relwidth=0.172)
        self.DayOneFrame.configure(relief='sunken')
        self.DayOneFrame.configure(borderwidth="2")
        self.DayOneFrame.configure(relief="sunken")
        self.DayOneFrame.configure(background="#ffffff")

        self.DayLabbel1 = tk.Label(self.DayOneFrame)
        self.DayLabbel1.place(relx=0.138, rely=0.043, height=71, width=104)
        self.DayLabbel1.configure(background="#ffffff")
        self.DayLabbel1.configure(disabledforeground="#a3a3a3")
        self.DayLabbel1.configure(font=font10)
        self.DayLabbel1.configure(foreground="#000000")

        self.WeatherConditions1 = tk.Label(self.DayOneFrame)
        self.WeatherConditions1.place(relx=0.069, rely=0.301, height=91
                , width=124)
        self.WeatherConditions1.configure(background="#ffffff")
        self.WeatherConditions1.configure(disabledforeground="#a3a3a3")
        self.WeatherConditions1.configure(foreground="#000000")
        self.WeatherConditions1.configure(font=font17)

        self.TempLabel = tk.Label(self.DayOneFrame)
        self.TempLabel.place(relx=0.069, rely=0.559, height=181, width=124)
        self.TempLabel.configure(background="#ffffff")
        self.TempLabel.configure(disabledforeground="#a3a3a3")
        self.TempLabel.configure(font=font10)
        self.TempLabel.configure(foreground="#000000")

        self.DayTwoFrame = tk.Frame(self.MainBodyFrame)
        self.DayTwoFrame.place(relx=0.189, rely=0.021, relheight=0.959
                , relwidth=0.183)
        self.DayTwoFrame.configure(relief='sunken')
        self.DayTwoFrame.configure(borderwidth="2")
        self.DayTwoFrame.configure(relief="sunken")
        self.DayTwoFrame.configure(background="#ffffff")

        self.DayLabbel2 = tk.Label(self.DayTwoFrame)
        self.DayLabbel2.place(relx=0.129, rely=0.043, height=71, width=114)
        self.DayLabbel2.configure(background="#ffffff")
        self.DayLabbel2.configure(disabledforeground="#a3a3a3")
        self.DayLabbel2.configure(font=font10)
        self.DayLabbel2.configure(foreground="#000000")

        self.WeatherConditions2 = tk.Label(self.DayTwoFrame)
        self.WeatherConditions2.place(relx=0.065, rely=0.301, height=91
                , width=124)
        self.WeatherConditions2.configure(background="#ffffff")
        self.WeatherConditions2.configure(disabledforeground="#a3a3a3")
        self.WeatherConditions2.configure(foreground="#000000")
        self.WeatherConditions2.configure(font=font17)

        self.TempLabel2 = tk.Label(self.DayTwoFrame)
        self.TempLabel2.place(relx=0.065, rely=0.559, height=181, width=124)
        self.TempLabel2.configure(background="#ffffff")
        self.TempLabel2.configure(disabledforeground="#a3a3a3")
        self.TempLabel2.configure(font=font10)
        self.TempLabel2.configure(foreground="#000000")

        self.DayThreeFrame = tk.Frame(self.MainBodyFrame)
        self.DayThreeFrame.place(relx=0.379, rely=0.021, relheight=0.959
                , relwidth=0.195)
        self.DayThreeFrame.configure(relief='sunken')
        self.DayThreeFrame.configure(borderwidth="2")
        self.DayThreeFrame.configure(relief="sunken")
        self.DayThreeFrame.configure(background="#ffffff")

        self.DayLabbel3 = tk.Label(self.DayThreeFrame)
        self.DayLabbel3.place(relx=0.121, rely=0.043, height=71, width=124)
        self.DayLabbel3.configure(background="#ffffff")
        self.DayLabbel3.configure(disabledforeground="#a3a3a3")
        self.DayLabbel3.configure(font=font10)
        self.DayLabbel3.configure(foreground="#000000")

        self.WeatherConditions3 = tk.Label(self.DayThreeFrame)
        self.WeatherConditions3.place(relx=0.121, rely=0.301, height=91
                , width=124)
        self.WeatherConditions3.configure(background="#ffffff")
        self.WeatherConditions3.configure(disabledforeground="#a3a3a3")
        self.WeatherConditions3.configure(foreground="#000000")
        self.WeatherConditions3.configure(font=font17)

        self.TempLabel3 = tk.Label(self.DayThreeFrame)
        self.TempLabel3.place(relx=0.121, rely=0.559, height=181, width=124)
        self.TempLabel3.configure(background="#ffffff")
        self.TempLabel3.configure(disabledforeground="#a3a3a3")
        self.TempLabel3.configure(font=font10)
        self.TempLabel3.configure(foreground="#000000")

        self.DayFourFrame = tk.Frame(self.MainBodyFrame)
        self.DayFourFrame.place(relx=0.58, rely=0.021, relheight=0.959
                , relwidth=0.207)
        self.DayFourFrame.configure(relief='sunken')
        self.DayFourFrame.configure(borderwidth="2")
        self.DayFourFrame.configure(relief="sunken")
        self.DayFourFrame.configure(background="#ffffff")

        self.DayLabbel4 = tk.Label(self.DayFourFrame)
        self.DayLabbel4.place(relx=0.114, rely=0.043, height=71, width=134)
        self.DayLabbel4.configure(background="#ffffff")
        self.DayLabbel4.configure(disabledforeground="#a3a3a3")
        self.DayLabbel4.configure(font=font10)
        self.DayLabbel4.configure(foreground="#000000")

        self.WeatherConditions4 = tk.Label(self.DayFourFrame)
        self.WeatherConditions4.place(relx=0.114, rely=0.301, height=91, width=134)
        self.WeatherConditions4.configure(background="#ffffff")
        self.WeatherConditions4.configure(disabledforeground="#a3a3a3")
        self.WeatherConditions4.configure(foreground="#000000")
        self.WeatherConditions4.configure(font=font17)

        self.TempLabel4 = tk.Label(self.DayFourFrame)
        self.TempLabel4.place(relx=0.114, rely=0.559, height=181, width=134)
        self.TempLabel4.configure(background="#ffffff")
        self.TempLabel4.configure(disabledforeground="#a3a3a3")
        self.TempLabel4.configure(font=font10)
        self.TempLabel4.configure(foreground="#000000")

        self.DayFiveFrame = tk.Frame(self.MainBodyFrame)
        self.DayFiveFrame.place(relx=0.793, rely=0.021, relheight=0.959
                , relwidth=0.195)
        self.DayFiveFrame.configure(relief='sunken')
        self.DayFiveFrame.configure(borderwidth="2")
        self.DayFiveFrame.configure(relief="sunken")
        self.DayFiveFrame.configure(background="#ffffff")

        self.DayLabbel5 = tk.Label(self.DayFiveFrame)
        self.DayLabbel5.place(relx=0.121, rely=0.043, height=71, width=114)
        self.DayLabbel5.configure(background="#ffffff")
        self.DayLabbel5.configure(disabledforeground="#a3a3a3")
        self.DayLabbel5.configure(font=font10)
        self.DayLabbel5.configure(foreground="#000000")

        self.WeatherConditions5 = tk.Label(self.DayFiveFrame)
        self.WeatherConditions5.place(relx=0.121, rely=0.301, height=91, width=124)
        self.WeatherConditions5.configure(background="#ffffff")
        self.WeatherConditions5.configure(disabledforeground="#a3a3a3")
        self.WeatherConditions5.configure(foreground="#000000")
        self.WeatherConditions5.configure(font=font17)

        self.TempLabel5 = tk.Label(self.DayFiveFrame)
        self.TempLabel5.place(relx=0.061, rely=0.559, height=181, width=144)
        self.TempLabel5.configure(background="#ffffff")
        self.TempLabel5.configure(disabledforeground="#a3a3a3")
        self.TempLabel5.configure(font=font10)
        self.TempLabel5.configure(foreground="#000000")

        self.CityNameLable = tk.Label(top)
        self.CityNameLable.place(relx=0.298, rely=0.055, height=81, width=314)
        self.CityNameLable.configure(background="#80ffff")
        self.CityNameLable.configure(disabledforeground="#a3a3a3")
        self.CityNameLable.configure(font=font9)
        self.CityNameLable.configure(foreground="#000000")
        self.CityNameLable.configure(relief="groove")
        self.CityNameLable.configure(text='''Please insert Zip At Bottom''')

        self.ZipButton = tk.Button(top)
        self.ZipButton.place(relx=0.665, rely=0.935, height=34, width=77)
        self.ZipButton.configure(activebackground="#ececec")
        self.ZipButton.configure(activeforeground="#000000")
        self.ZipButton.configure(background="#d9d9d9")
        self.ZipButton.configure(command=self.Run)
        self.ZipButton.configure(disabledforeground="#a3a3a3")
        self.ZipButton.configure(foreground="#000000")
        self.ZipButton.configure(highlightbackground="#d9d9d9")
        self.ZipButton.configure(highlightcolor="black")
        self.ZipButton.configure(pady="0")
        self.ZipButton.configure(text='''Submit''')

        self.ZipEntry = tk.Entry(top)
        self.ZipEntry.place(relx=0.78, rely=0.935,height=40, relwidth=0.2)
        self.ZipEntry.configure(background="white")
        self.ZipEntry.configure(disabledforeground="#a3a3a3")
        self.ZipEntry.configure(font="TkFixedFont")
        self.ZipEntry.configure(foreground="#000000")
        self.ZipEntry.configure(insertbackground="black")

    def Run(self):
        #Gets the weather Report and configs the lable to display it
        if self.ZipEntry.get():
            WeatherReport = WhatsTheWeather.Weather(self.ZipEntry.get())
            self.CityNameLable.configure(text='WeatherReport.City_Name')
            
            self.DayLabbel1.configure(text=f"{WhatsTheWeather.DayoftheWeek(WeatherReport.Forrcast[0][0][6])} \n {WhatsTheWeather.Month(WeatherReport.Forrcast[0][0][1])} {(WeatherReport.Forrcast[0][0][2])}")
            self.WeatherConditions1.configure(text=f"{WeatherReport.Forrcast[0][3]}")
            self.TempLabel.configure(text=f"The Hight {WeatherReport.Forrcast[0][1]}F \n The Low {WeatherReport.Forrcast[0][2]}F")

            self.DayLabbel2.configure(text=f"{WhatsTheWeather.DayoftheWeek(WeatherReport.Forrcast[1][0][6])} \n {WhatsTheWeather.Month(WeatherReport.Forrcast[1][0][1])} {(WeatherReport.Forrcast[1][0][2])}")
            self.WeatherConditions2.configure(text=f"{WeatherReport.Forrcast[1][3]}")
            self.TempLabel2.configure(text=f"The Hight {WeatherReport.Forrcast[1][1]}F \n The Low {WeatherReport.Forrcast[1][2]}F")

            self.DayLabbel3.configure(
                text=f"{WhatsTheWeather.DayoftheWeek(WeatherReport.Forrcast[2][0][6])} \n {WhatsTheWeather.Month(WeatherReport.Forrcast[2][0][1])} {(WeatherReport.Forrcast[1][0][2])}")
            self.WeatherConditions3.configure(text=f"{WeatherReport.Forrcast[2][3]}")
            self.TempLabel3.configure(
                text=f"The Hight {WeatherReport.Forrcast[2][1]}F \n The Low {WeatherReport.Forrcast[2][2]}F")
            
            self.DayLabbel4.configure(
                text=f"{WhatsTheWeather.DayoftheWeek(WeatherReport.Forrcast[3][0][6])} \n {WhatsTheWeather.Month(WeatherReport.Forrcast[3][0][1])} {(WeatherReport.Forrcast[1][0][2])}")
            self.WeatherConditions4.configure(text=f"{WeatherReport.Forrcast[3][3]}")
            self.TempLabel4.configure(
                text=f"The Hight {WeatherReport.Forrcast[3][1]}F \n The Low {WeatherReport.Forrcast[3][2]}F")

            self.DayLabbel5.configure(
                text=f"{WhatsTheWeather.DayoftheWeek(WeatherReport.Forrcast[4][0][6])} \n {WhatsTheWeather.Month(WeatherReport.Forrcast[4][0][1])} {(WeatherReport.Forrcast[1][0][2])}")
            self.WeatherConditions5.configure(text=f"{WeatherReport.Forrcast[4][3]}")
            self.TempLabel5.configure(
                text=f"The Hight {WeatherReport.Forrcast[4][1]}F \n The Low {WeatherReport.Forrcast[4][2]}F")
        else:
            from tkinter import messagebox
            tk.messagebox.showwarning("BAD", "Please enter a zip code!")


if __name__ == '__main__':
    vp_start_gui()





