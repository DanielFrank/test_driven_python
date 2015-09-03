import unittest
from unittest import mock

from ..action import PrintAction

class PrintActionTest(unittest.TestCase):
    @mock.patch("builtins.print")
    def test_executing_action_prints_message(self, mock_print):
        action = PrintAction()
        text = "GOOG > $10"
        action.execute(text)
        mock_print.assert_called_with(text)

            
