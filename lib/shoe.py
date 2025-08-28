#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="", size=0):
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = "New"

    # ---- Size ----
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")   # <── print instead of raise

    # ---- Repair ----
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
