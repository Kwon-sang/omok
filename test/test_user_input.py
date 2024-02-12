import unittest
from unittest.mock import patch

from src import user_input


class UserInputTest(unittest.TestCase):

    @patch('builtins.input')
    def test_board_size_pass(self, mock_get):
        data_list = [
            '0',
            '3',
            '99',
            '077',
        ]
        mock_get.side_effect = data_list
        for data in data_list:
            result = user_input.board_size()
            self.assertEqual(result, int(data))

    @patch('builtins.input')
    def test_board_size_fail(self, mock_get):
        data_list = [
            '-1',
            'a',
            'dsdf',
            '-10',
            '00d',
            'd34',
            ' 3',
            '4 4'
        ]
        mock_get.side_effect = data_list
        for data in data_list:
            with self.assertRaises(ValueError) as context:
                user_input.board_size()
            self.assertTrue(str(context.exception) == "Invalid input")

    @patch('builtins.input')
    def test_username_pass(self, mock_get):
        data = ('username1', 'username2')
        mock_get.side_effect = data
        result = user_input.username()
        self.assertEqual(result, data)

    @patch('builtins.input')
    def test_username_fail(self, mock_get):
        data = ('same username', 'same username')
        mock_get.side_effect = data
        with self.assertRaises(ValueError) as context:
            user_input.username()
        self.assertTrue(str(context.exception) == "Invalid input")

    @patch('builtins.input')
    def test_position_pass(self, mock_get):
        data_list = [
            '0 0',
            '3 5',
            '0 7',
            '16 16',
            '07 09'
        ]
        mock_get.side_effect = data_list
        for data in data_list:
            result = user_input.position()
            expected = tuple(map(int, data.split()))
            self.assertEqual(result, expected)

    @patch('builtins.input')
    def test_position_fail(self, mock_get):
        data_list = [
            '-5 0',
            'd 5',
            '9 d',
            '6o 3'
            '54'
            '5  4'
        ]
        mock_get.side_effect = data_list
        for data in data_list:
            with self.assertRaises(ValueError):
                user_input.position()

    @patch('builtins.input')
    def test_position_exit(self, mock_get):
        data = 'Q'
        mock_get.side_effect = data
        with self.assertRaises(SystemExit):
            user_input.position()
