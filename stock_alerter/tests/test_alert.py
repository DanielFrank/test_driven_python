import unittest
from datetime import datetime
from unittest import mock

from ..alert import Alert
from ..rule import PriceRule
from ..stock import Stock

class AlertTest(unittest.TestCase):
    def test_action_is_executed_when_rule_matches(self):
        exchange = {"GOOG": Stock("GOOG")}
        rule = PriceRule("GOOG",lambda stock: stock.price > 10)
        action = mock.MagicMock()
        alert_text = "sample alert"
        alert = Alert(alert_text, rule, action)
        alert.connect(exchange)
        exchange["GOOG"].update(datetime(2014,2,10), 11)
        action.execute.assert_called_with(alert_text)