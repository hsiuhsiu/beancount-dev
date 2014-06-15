import unittest

from beancount.core import data
from beancount.core import compare
from beancount.parser import parser


TEST_INPUT = """

2012-02-01 open Assets:US:Cash
2012-02-01 open Assets:US:Credit-Card
2012-02-01 open Expenses:Grocery
2012-02-01 open Expenses:Coffee
2012-02-01 open Expenses:Restaurant

2012-05-18 * "Buying food" #dinner
  Expenses:Restaurant         100 USD
  Expenses:Grocery            200 USD
  Assets:US:Cash

2013-06-20 * "Whole Foods Market" | "Buying books" #books #dinner ^ee89ada94a39
  Expenses:Restaurant         150 USD
  Assets:US:Credit-Card

2013-06-22 * "La Colombe" | "Buying coffee"  ^ee89ada94a39
  Expenses:Coffee         5 USD
  Assets:US:Cash

2014-02-01 close Assets:US:Cash
2014-02-01 close Assets:US:Credit-Card

"""

class TestCompare(unittest.TestCase):

    def test_hash_entries(self):
        previous_hashes = None
        for _ in range(64):
            entries, errors, options_map = parser.parse_string(TEST_INPUT)
            hashes = compare.hash_entries(entries)
            if previous_hashes is None:
                previous_hashes = hashes
            else:
                self.assertEqual(previous_hashes.keys(), hashes.keys())

    def test_compare_entries(self):
        entries1, _, __ = parser.parse_string(TEST_INPUT)
        entries2, _, __ = parser.parse_string(TEST_INPUT)

        # Check two equal sets.
        same, missing1, missing2 = compare.compare_entries(entries1, entries2)
        self.assertTrue(same)
        self.assertFalse(missing1)
        self.assertFalse(missing2)

        # First > Second.
        same, missing1, missing2 = compare.compare_entries(entries1, entries2[:-1])
        self.assertFalse(same)
        self.assertTrue(missing1)
        self.assertFalse(missing2)
        self.assertEqual(1, len(missing1))
        self.assertTrue(isinstance(missing1.pop(), data.Close))

        # First < Second.
        same, missing1, missing2 = compare.compare_entries(entries1[:-1], entries2)
        self.assertFalse(same)
        self.assertFalse(missing1)
        self.assertTrue(missing2)
        self.assertEqual(1, len(missing2))
        self.assertTrue(isinstance(missing2.pop(), data.Close))

        # Both have missing.
        same, missing1, missing2 = compare.compare_entries(entries1[1:], entries2[:-1])
        self.assertFalse(same)
        self.assertTrue(missing1)
        self.assertTrue(missing2)
        self.assertEqual(1, len(missing1))
        self.assertTrue(isinstance(missing1.pop(), data.Close))
        self.assertEqual(1, len(missing2))
        self.assertTrue(isinstance(missing2.pop(), data.Open))

    def test_includes_entries(self):
        entries1, _, __ = parser.parse_string(TEST_INPUT)
        entries2, _, __ = parser.parse_string(TEST_INPUT)

        includes, missing = compare.includes_entries(entries1[0:-3], entries2)
        self.assertTrue(includes)
        self.assertFalse(missing)

        includes, missing = compare.includes_entries(entries1, entries2[0:-3])
        self.assertFalse(includes)
        self.assertEqual(3, len(missing))