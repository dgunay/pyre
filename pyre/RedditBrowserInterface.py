from abc import ABC, abstractmethod

# TODO: use praw to make a simple reddit browser
# TODO: make this a base interface and subclass out an authenticated version
# using praw, and one that just uses .json
class RedditBrowserInterface(ABC):

  # TODO: method that lets you go to a Reddit post URL
  # TODO: document this method idiomatically
  @abstractmethod
  def go_to(self, url: str):
    raise NotImplementedError

  # TODO: method that yields thread as a tree of comments with OP at the root
  # TODO: document this method idiomatically
  @abstractmethod
  def current_thread(self):
    raise NotImplementedError