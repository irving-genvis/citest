'''

  Created by irving on 24/07/18

'''
from unittest import TestCase
from ci.calculator import calculator



class TestClaculator(TestCase):

    def setUp(self):
        self.c = calculator()

    def test_add(self):
        self.assertEqual(self.c.add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(self.c.subtract(1, 1), 0)


