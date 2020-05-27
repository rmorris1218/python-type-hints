import unittest

from hint import *

class TestHint(unittest.TestCase):

    def test_tags_to_list(self):
        test_tags = {"key": "value"}
        tags_list = tags_to_list(test_tags)
        assert len(tags_list) == 1
        assert tags_list[0]['Key'] == "key"
        assert tags_list[0]['Value'] == "value"