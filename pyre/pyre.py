from asciimatics.screen import Screen
from time import sleep

def pyre(screen: Screen):
  screen.clear()
  screen.print_at('Hello world!', 0, 0)
  screen.refresh()
  sleep(10)
  pass

Screen.wrapper(pyre)