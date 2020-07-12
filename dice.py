import tkinter
import random

class Roll(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
    def initialize(self):
        self.images = [tkinter.PhotoImage(file=r"C:\Users\Matt\Pictures\dice1.pbm"), tkinter.PhotoImage(file=r"C:\Users\Matt\Pictures\dice2.pbm"),
                       tkinter.PhotoImage(file=r"C:\Users\Matt\Pictures\dice2.pbm"), tkinter.PhotoImage(file=r"C:\Users\Matt\Pictures\dice4.pbm"),
                       tkinter.PhotoImage(file=r"C:\Users\Matt\Pictures\dice3.pbm"), tkinter.PhotoImage(file=r"C:\Users\Matt\Pictures\dice6.pbm")]

        self.resize = [self.images[0].subsample(1, 1), self.images[1].subsample(1, 1), self.images[2].subsample(1, 1),
                       self.images[3].subsample(1, 1), self.images[4].subsample(1, 1), self.images[5].subsample(1, 1)]

        self.frame = tkinter.Frame(self, width = 500, height = 110)
        self.frame.pack()
        tkinter.Button(self, text="Roll Dice", command=self.buttonclick).pack()


    def roll(self):
        return random.randrange(0, 5)


    def rollthedice(self):
        for x in self.frame.winfo_children():
            x.destroy()

    def buttonclick(self):
        self.rollthedice()
        for x in range(0,2):
            dice = self.roll()
            tkinter.Label(self.frame, image=self.resize[dice]).pack(side=tkinter.LEFT)
if __name__ == "__main__":
    app = Roll(None)
    app.title("Dice Roller")
    app.mainloop()
