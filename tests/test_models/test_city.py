#!/usr/bin/python3
"""Unit test for class City"""
import models
from models.base_model import BaseModel
from models.city import City
import os
import pep8
import unittest
from time import sleep


class TestCity(unittest.TestCase):
    """
    Args:
            unittest ([type]): [description]
    """

    def setUp(self):
        """Reload object"""
        self.c1 = City()
        self.c1.name = "Julien"
        self.c1.state = "Antioquia"

    def tearDown(self):
        """delete instance"""
        del self.c1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """test doc in the file"""
        self.assertIsNotNone(City.__doc__)

    def test_instance(self):
        """Test instance"""
        self.assertIsInstance(self.c1, City)
        self.assertIsInstance(self.c1, BaseModel)

    def test_is_subclass(self):
        """Test is_subclass"""
        self.assertTrue(issubclass(self.c1.__class__, BaseModel), True)

    def test_has_attr(self):
        """Test has attr"""
        self.assertTrue('id' in self.c1.__dict__)
        self.assertTrue('created_at' in self.c1.__dict__)
        self.assertTrue('updated_at' in self.c1.__dict__)
        self.assertTrue('name' in self.c1.__dict__)
        self.assertTrue('state' in self.c1.__dict__)

    def test_attr_type(self):
        """Test attr_type"""
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.state, str)

    def test_save(self):
        """Test save"""
        self.c1.save()
        self.assertNotEqual(self.c1.created_at, self.c1.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual('to_dict' in dir(self.c1), True)


if __name__ == '__main__':
    unittest.main()
