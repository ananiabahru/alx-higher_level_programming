#!/usr/bin/python3
"""this defines a locked class py"""

class LockedClass:
"""
Only allows instatiation of an attribute called first_name
"""
__slots__ = ["first_name"]
