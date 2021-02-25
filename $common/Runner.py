#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import gettext
from unittest import TestSuite, TestLoader, TextTestRunner


language = sys.argv[1]
try:    
    trad = gettext.GNUTranslations(open("../../course/common/student/$i18n/" + language + ".mo", "rb"))
except FileNotFoundError:
    trad = gettext.NullTranslations()
trad.install()

test_names = [file[:file.rfind('.')] for file in os.listdir('.') if file.startswith("Test")]

suite = TestSuite()
for test in test_names:
    tests = TestLoader().loadTestsFromName(test)
    suite.addTests(tests)

runner = TextTestRunner(verbosity=0, descriptions=0)
try:
    result = runner.run(suite)
except AttributeError: pass
except TimeoutError: pass

if result.wasSuccessful():
    sys.exit(127)
