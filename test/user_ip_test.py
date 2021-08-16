"""
Test user_ip function
"""
import unittest
from unittest.mock import patch

from app.dict_def import get_user_ip


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_use_ip(self):
        user_input = [
            "bye"
        ]

        with patch('builtins.input', side_effect=user_input):
            with self.assertRaises(SystemExit) as sysEx:
                get_user_ip()

        self.assertEqual("BBye!", sysEx.exception.args[0])


if __name__ == '__main__':
    unittest.main()
