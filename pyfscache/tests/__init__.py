from unittest import TestSuite

from . import test_fscache

def test_suite():
  suite = TestSuite()
  suite.addTest(test_fscache.test_suite())
  return suite
