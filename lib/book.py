#!/usr/bin/env python3

class Book:
    def __init__(self, title="", page_count=0):
        self.title = title
        self._page_count = None
        self.page_count = page_count

    # ---- Title ----
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    # ---- Page Count ----
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")   # <── print instead of raise

    # ---- Turn Page ----
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
