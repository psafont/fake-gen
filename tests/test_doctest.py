import doctest
import unittest

import testdata

class TestDocTest(unittest.TestCase):

    def test_doctest(self):
        doctest.testmod(testdata.base)
        doctest.testmod(testdata.dictionary)
        doctest.testmod(testdata.factories.statistical)
        doctest.testmod(testdata.factories.datetimes)
        doctest.testmod(testdata.factories.generic)
        doctest.testmod(testdata.factories.sequences)
        doctest.testmod(testdata.factories.numbers)

if __name__ == '__main__':
    unittest.main()
