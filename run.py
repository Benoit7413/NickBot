import unittest
import sys
from tests.main import *
import nickbot

testLoader = unittest.defaultTestLoader
testRunner = unittest.TextTestRunner(verbosity=1)
test = testLoader.loadTestsFromName("tests.main")
result = testRunner.run(test)
if not result.wasSuccessful():
    sys.exit(not result.wasSuccessful())

nickbot.main()
