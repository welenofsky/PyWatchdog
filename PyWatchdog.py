#! /usr/bin/python
"""
This is a gui GTKx(undecided) application that uses a AF_INET 
connection to our web servers IP to asertain the current
status of internet connectivity. It is written in Python 3 only.
Authored by Justin Welenofsky
"""

import socket
import time
import winsound
import argparse

try:
    # Python2
    import Tkinter as tkinter
except ImportError:
    # Python3
    import tkinter as tkinter

root = tkinter.Tk()

def checkI(ip, port):
    isActive = 1
    isSent = 0
    app = Application(master=root)

    print("Connecting to External IP...")

    while isActive == 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            if isSent == 0:
                isSent = 1
                print("Connected to IP", ip)
            s.shutdown(2)
            s.close()
        except socket.error as e:
            print("Internetz Down!!!1")
            print(e)
            #Play exclamation sound when internet goes down
            winsound.PlaySound("SystemHand", winsound.MB_ICONHAND)

            app.mainloop()
            
            isActive = 0
        time.sleep(5);

    
class Application(tkinter.Frame):

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.OKAY = tkinter.Button(self)
        self.OKAY["text"] = "Internet Downzzz\n(click me)"
        self.OKAY["command"] = self.say_hi
        self.OKAY.pack(side="top")

        self.QUIT = tkinter.Button(self, text="FUCK DIS", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("Pfft...What a downer")


def main():
    parser = argparse.ArgumentParser(description="Watches internet and lets you know when it goes down.")
    parser.add_argument("-s", metavar="SERVER", type=str,
                        help="The server you want to connect to in order to prove you can access outside world.")
    parser.add_argument("-p", metavar="PORT", type=int,
                        help="Port you want to watch, defaults to 80.")
    args = parser.parse_args()

    ip = args.s or 'google.com'
    port = args.p or 80

    checkI(ip, port)


main()
