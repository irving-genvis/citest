'''

  Created by irving on 24/07/18

'''
from unittest import TestCase
from ci.calculator import calculator

c = calculator()


class TestClaculator(TestCase):
    def test_add(self):
        self.assertEqual(c.add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(c.subtract(1, 1), 0)


t = TestClaculator()
t.test_add()
t.test_subtract()
