"""Wiki module for returning requests data for the bot client."""
import requests

class Wiki(object):
    """Return a wikipedia link with brief synopsis of the content."""

    def __init__(self, search_string):
        """Create init attributes for creating a new Wiki object."""
        self.search_string = search_string

    def search(search_string):
        """Does GET request for search string parameter."""
        test_data = requests.get(
        "https://en.wikipedia.org/wiki/Special:Search?search="
        f"{search_string}&go=Go")
        # only returning the string for now to make sure the bot works with it
        return (
        f'https://en.wikipedia.org/wiki/Special:Search?search={search_string}')
