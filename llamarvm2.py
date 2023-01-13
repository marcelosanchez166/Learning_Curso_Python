# vm2.py
import tkinter as tk

class Fx2(tk.Toplevel):
          def __init__(self, master=None):
                    super().__init__(master)
                    self.master = master
                    self.create_widgets()

          def create_widgets(self):
                    self.message = tk.Message(self, text="Hello")
                    self.message.pack()