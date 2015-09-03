import unittest
from unittest import mock

from ..action import PrintAction

class PrintActionTest(unittest.TestCase):
    def test_executing_action_prints_message(self):
        patcher = mock.patch('builtins.print')
        mock_print = patcher.start()
        try:
            action = PrintAction()
            text = "GOOG > $10"
            action.execute(text)
            mock_print.assert_called_with(text)
        finally:
            patcher.stop()

            
