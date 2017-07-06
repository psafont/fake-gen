from doctest import testmod
import unittest

import testdata

class TestDocTest(unittest.TestCase):

    def test_doctest(self):
        testmod(testdata.base)
        testmod(testdata.dictionary)
        testmod(testdata.factories.datetimes)
        testmod(testdata.factories.fake)
        testmod(testdata.factories.generic)
        testmod(testdata.factories.numeric)
        testmod(testdata.factories.sequences)
        testmod(testdata.factories.statistical)
        testmod(testdata.factories.strings)

if __name__ == '__main__':
    unittest.main()
