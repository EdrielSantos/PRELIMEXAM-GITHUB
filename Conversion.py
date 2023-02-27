import unittest

def conversion(temp):
    return (temp-32) * 5/9


class Testing(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(conversion(105), 37.77777777777778)

if __name__ == '__main__':
    unittest.main()
        