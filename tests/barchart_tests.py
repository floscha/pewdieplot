import unittest
import sys
sys.path.append('../pewdieplot')

from pewdieplot.graph.barchart import BarChart


def _create_test_barchart():
    barchart = BarChart('Test Bar Chart')
    return barchart


class BarChartTest(unittest.TestCase):
    """Test suite for the BarChart class."""

    def test_type(self):
        """Assert that the created object is of type BarChart."""
        test_barchart = _create_test_barchart()
        self.assertIs(BarChart, type(test_barchart))


if __name__ == '__main__':
    unittest.main()
