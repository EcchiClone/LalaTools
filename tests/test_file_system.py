import unittest
from lalatools.manage_file_system import file_system

class TestFileSystem(unittest.TestCase):
    def test_del_head(self):
        self.assertEqual(file_system.del_head("C:/Users/User/Documents/test.txt"), "test.txt")
        self.assertEqual(file_system.del_head(["C:/Users/User/Documents/test.txt", "C:/Users/User/Documents/test2.txt"]), ["test.txt", "test2.txt"])

    def test_replace_split_mark(self):
        self.assertEqual(file_system.replace_split_mark("C:\\Users\\User\\Documents\\test.txt"), "C:/Users/User/Documents/test.txt")
        self.assertEqual(file_system.replace_split_mark(["C:\\Users\\User\\Documents\\test.txt", "C:\\Users\\User\\Documents\\test2.txt"]), ["C:/Users/User/Documents/test.txt", "C:/Users/User/Documents/test2.txt"])

    def test_get_file_list(self):
        self.assertIsInstance(file_system.get_file_list("."), list)

if __name__ == '__main__':
    unittest.main()
