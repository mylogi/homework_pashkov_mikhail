print('test_dir/super_test/__init__.py')

# from test_dir.super_test import super_func  # error's variant
from .super_temp import super_func  # relative import

__all__ = ('super_func',)
