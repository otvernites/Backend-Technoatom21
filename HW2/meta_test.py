import unittest
from metaclass import CustomClass


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.inst = CustomClass()

    def test_meta_class(self):
        self.assertEqual(self.inst.custom_x, 50)
        self.assertEqual(hasattr(self.inst, 'custom_x'), True)
        self.assertEqual(hasattr(self.inst, 'x'), False)

        self.assertEqual(self.inst.custom_val, 99)
        self.assertEqual(hasattr(self.inst, 'custom_val'), True)
        self.assertEqual(hasattr(self.inst, 'val'), False)

        self.assertEqual(self.inst.custom_line(), 100)
        self.assertEqual(hasattr(self.inst, 'custom_line'), True)
        self.assertEqual(hasattr(self.inst, 'line'), False)

        self.assertEqual(self.inst.custom_item, 10)
        self.assertEqual(hasattr(self.inst, 'custom_item'), True)
        self.assertEqual(hasattr(self.inst, 'item'), False)

        self.assertEqual(self.inst.custom_str, "hello")
        self.assertEqual(hasattr(self.inst, 'custom_str'), True)
        self.assertEqual(hasattr(self.inst, 'str'), False)

        self.assertEqual(self.inst.custom_size(), (10, 1))
        self.assertEqual(hasattr(self.inst, 'custom_size'), True)
        self.assertEqual(hasattr(self.inst, 'size'), False)
