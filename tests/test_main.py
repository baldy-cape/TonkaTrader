# tests/test_main.py
"""Unit tests for the main module."""

import unittest
import os
from main import load_settings


class TestMain(unittest.TestCase):
    """Test cases for the main module."""

    def setUp(self):
        """
        Set up a temporary settings file before each test.
        """
        self.temp_cfg_file = 'temp_settings.cfg'
        with open(self.temp_cfg_file, 'w', encoding='utf-8') as file:
            file.write('[DEFAULT]\n')
            file.write('Setting1 = TestValue1\n')

    def tearDown(self):
        """
        Clean up and remove the temporary settings file after each test.
        """
        os.remove(self.temp_cfg_file)

    def test_load_settings(self):
        """
        Test loading of settings from a temporary configuration file.
        """
        settings = load_settings(self.temp_cfg_file)
        self.assertIn('Setting1', settings['DEFAULT'])
        self.assertEqual(settings['DEFAULT']['Setting1'], 'TestValue1')


if __name__ == '__main__':
    unittest.main()
