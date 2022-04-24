from time import sleep
from tkinter import Tk, ttk
from turtle import update

from gui.frames import ExperimentFrame, ResearchFrame


                

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Face Recognition")
        self.attributes("-fullscreen", True)

        self.notebook = ttk.Notebook(self)

        self.ex_tab = ExperimentFrame(self.notebook)
        self.research_tab = ResearchFrame(self.notebook)

        self.notebook.add(self.ex_tab, text="Experiment")
        self.notebook.add(self.research_tab, text="Research")
        self.notebook.pack(expand=1, fill="both")
    def update_picture(self):
        self.update()

        