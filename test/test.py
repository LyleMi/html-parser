#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

sys.path.append("..")

from htmlparser import HTML

class ParserTest(unittest.TestCase):

    def test_parse(self):
        with open("sample0.html", "rb") as fh:
            print(HTML.parse(fh.read()))

    def test_parse_tag(self):
        HTML.parseTag('<input type="radio" name="do" id="do_included" value="included" checked="checked" />')


if __name__ == '__main__':
    unittest.main()
