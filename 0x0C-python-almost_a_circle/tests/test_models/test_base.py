from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    """class to test the methods"""

    def init(self):
        Base.__nb_objects = 0

    def id_test(self):
        new_id = Base(5)
        self.assertEqual(new_id.id, 5)
    
    def test_id_none(self):
        new_id = Base()
        self.assertEqual(new_id.id, 1)
    