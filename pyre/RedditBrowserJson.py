import abc
from RedditBrowserInterface import RedditBrowserInterface
import requests

class RedditBrowserJson(RedditBrowserInterface):

  def __init__(self):
    self.current_post_json = ''

  def go_to_post(self, post_url: str):
    response = requests.get(post_url)

    # TODO: use response.json() and see what pprints
    pass
