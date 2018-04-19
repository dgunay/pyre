from asciimatics.screen import Screen
from time import sleep

from RedditBrowserJson import RedditBrowserJson

def pyre(screen: Screen):
  screen.clear()
  screen.print_at('Hello world!', 0, 0)
  screen.refresh()
  sleep(10)
  pass

# Screen.wrapper(pyre)

rb = RedditBrowserJson()

print(rb.go_to('https://www.reddit.com/r/lucianmains/.json'))
print(rb.go_to('https://www.nottheright.com/domf'))