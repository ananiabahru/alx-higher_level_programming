#!/usr/bin/python3
"""This module defines a file-appending function."""

def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
