import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add_integers(self):
        """Test addition of two integers."""
        self.assertEqual(add(1, 2), 3)

    def test_add_floats(self):
        """Test addition of two floats."""
        self.assertAlmostEqual(add(1.0, 2.5), 3.5)

    def test_add_mixed_types(self):
        """Test addition of an integer and a float."""
        self.assertAlmostEqual(add(1, 2.5), 3.5)

    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        self.assertEqual(add(-1, -1), -2)

    def test_add_with_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(5, 0), 5)

    def test_add_type_error(self):
        """Test that adding non-numbers raises a TypeError."""
        with self.assertRaises(TypeError):
            add("a", "b")
        with self.assertRaises(TypeError):
            add(1, "b")

if __name__ == '__main__':
    unittest.main()
