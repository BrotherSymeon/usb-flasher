#!/usr/bin/env python
"""
A simple example of a few buttons and click handlers.
"""
import re
import sys
import logging
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
from prompt_toolkit.keys import Keys
from prompt_toolkit.widgets import Box, Button, Frame, Label, TextArea, RadioList
from subprocess import Popen, PIPE, STDOUT
from lib import join



logging.basicConfig(filename='flasher.log', level=logging.DEBUG)

selected_drive = None
selected_iso_file = None

def strip_lines(val):
    pass

def get_system_drives():
    p = Popen(['lsblk'], stdout=PIPE, stderr=STDOUT)
    output = p.stdout.readlines()
    items = []
    for line in output:
        items.append(line.decode().rstrip())

    options = items[1:]
    label = items[0]
    return (options, label)

def convert_to_tuples(drives):
    returnval = []
    for drive in drives:
        vals = drive.split()
        name = vals[0]
        w = re.search(r'[a-zA-Z0-9]', name)
        realname = name[w.start():]
        returnval.append((realname, drive))
    return returnval
# Event handlers for all the buttons.
def handle_drive_click():
    pass

def select_iso_clicked():
    iso_box = TextArea(
            multiline=False,
            focus_on_click=True,
            focusable=True,
            width=40,
            style="class:iso-box"
            )
    main_frame.body = Box(
                            HSplit(
                                [Label(text="Enter the path to your ISO file"),iso_box]
                                ),
                                style="class:right-pane"
                        )

    if radio_list:
        selected_drive = radio_list.current_value or None
        logging.debug(selected_drive)
 

def select_drive_clicked():
    drives = get_system_drives()
    tups = convert_to_tuples(drives[0])

    global radio_list
    radio_list = RadioList(values=tups)
    logging.debug(drives)
    main_frame.body = HSplit([Label(text='    '+drives[1]), radio_list])

def flash_drive_clicked(): 
    text_area.text = "Flash Your drive"
    main_frame.body = text_area

def exit_clicked():
    get_app().exit()


# All the widgets for the UI.
button1 = Button("Select Drive", handler=select_drive_clicked, width=15)
button2 = Button("Select .iso File", handler=select_iso_clicked, width=19)
button3 = Button("Flash Your Drive", handler=flash_drive_clicked, width=19)
button4 = Button("Exit", handler=exit_clicked)
text_area = TextArea(focusable=True)
main_frame = Frame(text_area)
radio_list = None
#main_box = Box(body=main_frame , padding=1, style="class:right-pane"),
#drives = get_system_drives()
#tups = convert_to_tuples(drives)

#drives = [('sda1', 'sda      8:0    0 298.1G  0 disk'),('sda2', '??????sda2   8:2    0 297.6G  0 part /run/timeshift/backup')]
#radio_list = RadioList(values=tups)
# Combine all the widgets in a UI.
# The `Box` object ensures that padding will be inserted around the containing
# widget. It adapts automatically, unless an explicit `padding` amount is given.
root_container = Box(
    HSplit(
        [
            Label(text="Press `Tab` to move the focus.Or Ctrl-q to Quit"),
            HSplit(
                [
                    Box(
                        body=VSplit([button1, button2, button3, button4], padding=3, width=75),
                        padding=1,
                        width=95,
                        style="class:left-pane",
                    ),
                    Box(body=main_frame , padding=1, style="class:right-pane"),
                ]
            ),
        ]
    ),
)

layout = Layout(container=root_container, focused_element=button1)


# Key bindings.
kb = KeyBindings()
#kb.add("ctl-q")(sys.exit())
kb.add("tab")(focus_next)
kb.add("s-tab")(focus_previous)
@kb.add(Keys.ControlQ)
def handler(_):
    sys.exit()
    pass

# Styling.
style = Style(
    [
        ("left-pane", "bg:#2930FF #FFF942"),
        ("iso-box", "bg:#999CFF #000000"),
        ("right-pane", "bg:#2930FF #FFF942"),
        ("button", "#FFF942"),
        ("button-arrow", "#000000"),
        ("button focused", "bg:#000000 #999CFF"),
        ("text-area focused", "bg:#ff0000"),
    ]
)
# Build a main application object.  
application = Application(layout=layout, key_bindings=kb, style=style, full_screen=True)


def main():
    application.run()


if __name__ == "__main__":
    main()
