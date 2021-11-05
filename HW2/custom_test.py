import unittest
from exception import *
from custom_list import CustomList


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.my_list = CustomList([9, 1, 0, 7, 3, 0, 5])  # 25
        self.my_list1 = CustomList([1, 2, 3, 4])

    def test_sub(self):
        with self.assertRaises(NotListError):
            var = self.my_list1 - 1

        #оба CustomList
        my_list2 = CustomList([0, 1, 2, 3])
        result = self.my_list1 - my_list2
        self.assertEqual(result, [1, 1, 1, 1])
        self.assertIsInstance(result, CustomList)

        #один - List, второй - CustomList и наоборот
        list3 = [5, 2, 10, 1]
        result = self.my_list1 - list3
        self.assertEqual(result, [-4, 0, -7, 3])
        self.assertIsInstance(result, CustomList)

        result = list3 - self.my_list1
        self.assertEqual(result, [4, 0, 7, -3])
        self.assertIsInstance(result, CustomList)

        #дополнение нулями
        list3 = [5, 2, 10, 1, 10, 10]
        result = self.my_list1 - list3
        self.assertEqual(result, [-4, 0, -7, 3, -10, -10])
        self.assertEqual(self.my_list1, [1, 2, 3, 4])

        list3 = [5, 2]
        result = self.my_list1 - list3
        self.assertEqual(result, [-4, 0, 3, 4])
        self.assertEqual(self.my_list1, [1, 2, 3, 4])

    def test_add(self):
        # оба CustomList
        my_list2 = CustomList([0, 1, 2, 3])
        result = self.my_list1 + my_list2
        self.assertEqual(result, [1, 3, 5, 7])
        self.assertIsInstance(result, CustomList)

        # один - List, второй - CustomList и наоборот
        list3 = [5, 2, 10, 1]
        result = self.my_list1 + list3
        self.assertEqual(result, [6, 4, 13, 5])
        self.assertIsInstance(result, CustomList)

        result = list3 + self.my_list1
        self.assertEqual(result, [6, 4, 13, 5])
        self.assertIsInstance(result, CustomList)

        # дополнение нулями
        list3 = [5, 2, 10, 1, 10, 10]
        result = self.my_list1 + list3
        self.assertEqual(result, [6, 4, 13, 5, 10, 10])
        self.assertEqual(self.my_list1, [1, 2, 3, 4])

        list3 = [5, 2]
        result = self.my_list1 + list3
        self.assertEqual(result, [6, 4, 2, 3])
        self.assertEqual(list3, [1, 2, 3, 4])

        with self.assertRaises(NotListError):
            self.my_list1 + 1

    def test_compare(self):
        my_list2 = CustomList([5, 9, 1, 0, 10])
        self.assertTrue(self.my_list == my_list2)

        my_list2 = CustomList([5, 9, 0, 10])
        self.assertTrue(self.my_list != my_list2)

        my_list2 = CustomList([5, 9, 10, 10])
        self.assertTrue(self.my_list < my_list2)

        my_list2 = CustomList([24])
        self.assertTrue(self.my_list >= my_list2)

        my_list2 = CustomList([5, 3, 0,  1, 10])
        self.assertTrue(self.my_list > my_list2)
        my_list2 = CustomList([25])
        self.assertTrue(self.my_list <= my_list2)

        
        my_list3 = [0, 1]
        self.assertTrue(my_list3 < self.my_list)
        self.assertTrue(self.my_list >= my_list3)
        
        with self.assertRaises(NotListError):
            self.my_list1 < 1

if __name__ == '__main__':
    unittest.main()

