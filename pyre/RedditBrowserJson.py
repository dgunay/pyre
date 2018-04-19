import abc
from RedditBrowserInterface import RedditBrowserInterface
import requests
import pprint
import re

import platform

class RedditBrowserJson(RedditBrowserInterface):

  def __init__(self):
    self.current_post = ''
    self.user_agent = 'Pyre client ' + platform.node()

  def go_to(self, url: str):
    """
    Requests the given Reddit page as JSON and decodes it, storing the resulting
    dict internally.

    Args:
      url (str): Reddit page to navigate to
    
    Raises:
      RequestException: If the GET request to the post fails for some reason.
    """

    if not self._is_reddit_domain_url(url):
      raise ValueError('URL "' + url + '" does not go to Reddit')

    response = requests.get(url, headers = {'User-agent' : self.user_agent})

    self.current_post = response.json()
  
  def current_thread(self):
    pass  
  
  # TODO: Document
  def _is_reddit_domain_url(self, url: str):
    regex = r':\/\/(?:www\.)?reddit\.com\/'
    result = re.findall(regex, url)

    return True if result else False
