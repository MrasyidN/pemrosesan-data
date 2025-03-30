import unittest
 
class TestAssertions(unittest.TestCase):
    
    def test_assertEqual(self):
        a = 5
        b = 5
        self.assertEqual(a, b)  # Pass jika a == b
 
    def test_assertNotEqual(self):
        a = 5
        b = 3
        self.assertNotEqual(a, b)  # Pass jika a != b
 
    def test_assertTrue(self):
        x = True
        self.assertTrue(x)  # Passes jika bool(x) is True
 
    def test_assertFalse(self):
        x = False
        self.assertFalse(x)  # Passes jika bool(x) is False
 
    def test_assertIs(self):
        a = None
        b = None
        self.assertIs(a, b)  # Passes jika a is b
 
    def test_assertIsNot(self):
        a = []
        b = []
        self.assertIsNot(a, b)  # Passes jika a is not b
 
    def test_assertIsNone(self):
        x = None
        self.assertIsNone(x)  # Passes jika x is None
 
    def test_assertIsNotNone(self):
        x = "hello"
        self.assertIsNotNone(x)  # Passes jika x is not None
 
    def test_assertIn(self):
        a = 3
        b = [1, 2, 3]
        self.assertIn(a, b)  # Pass jika a in b
 
    def test_assertNotIn(self):
        a = 4
        b = [1, 2, 3]
        self.assertNotIn(a, b)  # Pass jika a not in b
 
    def test_assertIsInstance(self):
        a = "hello"
        b = str
        self.assertIsInstance(a, b)  # Pass jika isinstance(a, b)
 
    def test_assertNotIsInstance(self):
        a = "hello"
        b = int
        self.assertNotIsInstance(a, b)  # Pass jika not isinstance(a, b)
 
if __name__ == "__main__":
    unittest.main()