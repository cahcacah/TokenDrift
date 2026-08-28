# test_tokendrift.py
"""
Tests for TokenDrift module.
"""

import unittest
from tokendrift import TokenDrift

class TestTokenDrift(unittest.TestCase):
    """Test cases for TokenDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenDrift()
        self.assertIsInstance(instance, TokenDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
