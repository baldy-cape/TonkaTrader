# tests/test_main.py
import unittest
import os
from main import load_settings

class TestMain(unittest.TestCase):

    def setUp(self):
        # Create a temporary settings file for testing
        self.temp_cfg_file = 'temp_settings.cfg'
        with open(self.temp_cfg_file, 'w') as file:
            file.write('[DEFAULT]\n')
            file.write('Setting1 = TestValue1\n')

    def tearDown(self):
        # Remove the temporary file after testing
        os.remove(self.temp_cfg_file)

    def test_load_settings(self):
        settings = load_settings(self.temp_cfg_file)
        self.assertIn('Setting1', settings['DEFAULT'])
        self.assertEqual(settings['DEFAULT']['Setting1'], 'TestValue1')

if __name__ == '__main__':
    unittest.main()

