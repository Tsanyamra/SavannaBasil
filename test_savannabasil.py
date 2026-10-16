# test_savannabasil.py
"""
Tests for SavannaBasil module.
"""

import unittest
from savannabasil import SavannaBasil

class TestSavannaBasil(unittest.TestCase):
    """Test cases for SavannaBasil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SavannaBasil()
        self.assertIsInstance(instance, SavannaBasil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SavannaBasil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
