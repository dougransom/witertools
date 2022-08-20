"""Witertools - Tools to wrap iterator functions, to consume the whole iterator and return a list.  Avoid sprinklist list(...)
throughout your code when you need a list instead of an interator.  

"""
__version__="0.0.0"

from .iterator_to_list import iterator_to_list_function,iterator_name_to_list_function
