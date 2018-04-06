import os
import sys

# Add Urwid to path if included in project
local_urwid_folder = os.path.dirname(os.path.realpath(__file__)) + '/urwid-2.0.1'
if os.path.exists(local_urwid_folder):
	sys.path.append(local_urwid_folder)

import urwid

txt  = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()