#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Feb 18, 2021 01:30:38 PM PKT  platform: Windows NT

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


def set_Tk_var():
    # Combo Box Setting
    global combobox
    combobox = tk.StringVar()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import sale_form
    sale_form.s_vp_start_gui()
