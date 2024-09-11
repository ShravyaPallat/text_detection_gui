import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class analysis_text():

    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def callback(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you want to leave?"):
            self.main.destroy()

    def setResult(self, type, res):
        if type == "neg":
            self.negativeLabel.configure(text="Negative sentiment: " + str(round(res * 100, 2)) + " %")
        elif type == "neu":
            self.neutralLabel.configure(text="Neutral sentiment: " + str(round(res * 100, 2)) + " %")
        elif type == "pos":
            self.positiveLabel.configure(text="Positive sentiment: " + str(round(res * 100, 2)) + " %")
        elif type == "compound":
            self.compoundLabel.configure(text="Overall sentiment score: " + str(round(res, 2)))

    def runAnalysis(self):
        sentence = self.line.get()
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)

        # Update sentiment labels
        self.setResult("neg", ss['neg'])
        self.setResult("neu", ss['neu'])
        self.setResult("pos", ss['pos'])
        self.setResult("compound", ss['compound'])

        # Show overall sentiment based on compound score
        if ss['compound'] >= 0.05:
            self.normalLabel.configure(text="You typed a positive statement.")
        elif ss['compound'] <= -0.05:
            self.normalLabel.configure(text="You typed a negative statement.")
        else:
            self.normalLabel.configure(text="You typed a neutral statement.")

    def editedText(self, event):
        self.typedText.configure(text=self.line.get())

    def runByEnter(self, event):
        self.runAnalysis()

    def __init__(self):
        self.main = Tk()
        self.main.title("Text Detector System")
        self.main.geometry("600x600")
        self.main.resizable(width=FALSE, height=FALSE)
        self.main.protocol("WM_DELETE_WINDOW", self.callback)
        self.center(self.main)

        self.label1 = Label(text="Type a text here:")
        self.label1.pack()

        self.line = Entry(self.main, width=70)
        self.line.pack()

        self.textLabel = Label(text="\n", font=("Helvetica", 15))
        self.textLabel.pack()

        self.typedText = Label(text="", fg="blue", font=("Helvetica", 20))
        self.typedText.pack()

        self.line.bind("<Key>", self.editedText)
        self.line.bind("<Return>", self.runByEnter)

        self.result = Label(text="\n", font=("Helvetica", 15))
        self.result.pack()

        self.negativeLabel = Label(text="", fg="red", font=("Helvetica", 20))
        self.negativeLabel.pack()

        self.neutralLabel = Label(text="", font=("Helvetica", 20))
        self.neutralLabel.pack()

        self.positiveLabel = Label(text="", fg="green", font=("Helvetica", 20))
        self.positiveLabel.pack()

        self.compoundLabel = Label(text="", fg="purple", font=("Helvetica", 20))
        self.compoundLabel.pack()

        self.normalLabel = Label(text="", fg="red", font=("Helvetica", 20))
        self.normalLabel.pack()

myanalysis = analysis_text()
mainloop()
