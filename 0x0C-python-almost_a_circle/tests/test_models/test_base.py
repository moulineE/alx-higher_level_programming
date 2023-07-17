#!/usr/bin/python3
"""This module define a Python unittest for base.py"""

import unittest
from models.base import Base


class Test_Base_class(unittest.TestCase):
    """unittest for Task 1. Base class"""
    
    def test_id_w_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test__id_w_no_arg_w_5_base(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, b5.id - 4)

    def test_id_w_None_as_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_is_12(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_0_main_py(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_id_is_public(self):
        b = Base(12)
        b.id = 99
        self.assertEqual(99, b.id)
