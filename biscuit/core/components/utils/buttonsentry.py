import tkinter as tk

from hintedtext import HintedEntry

from .frame import Frame
from .iconbutton import IconButton


class ButtonsEntry(Frame):
    def __init__(self, master, hint="", buttons=(), textvariable=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(padx=1, pady=1, bg=self.base.theme.border)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.entry = HintedEntry(self, relief=tk.FLAT, font=("Segoi UI", 10), bd=5, hint=hint, **self.base.theme.utils.buttonsentry, textvariable=textvariable)
        self.entry.grid(row=0, column=0, sticky=tk.NSEW)

        self.column = 1
        self.add_buttons(buttons)

    def add_button(self, icon, event=lambda _: None, icon2=None):
        b=IconButton(self, icon, event, icon2)
        b.grid(row=0, column=self.column, sticky='')
        b.config(**self.base.theme.utils.buttonsentry.button)
        self.column += 1

    def add_buttons(self, buttons):
        for btn in buttons:
            self.add_button(*btn)

    def get(self, *args):
        return self.entry.get(*args)

    def delete(self, *args):
        return self.entry.delete(*args)

    def insert(self, *args):
        return self.entry.insert(*args)
