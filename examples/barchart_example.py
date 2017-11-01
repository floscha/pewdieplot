"""Example for using a BarChart."""
# TODO(SysPath) Get rid of hacky path magic.
import sys
sys.path.append('../pewdieplot')

import numpy as np

from pewdieplot.graph.barchart import BarChart


data = [[3, 2, 1], [2, 1, 3], [1, 3, 2]]
x_tick_labels = ['January', 'February', 'March', 'April']

(BarChart(title='Bar Chart Example', size=(8, 5))
 .xlim(-0.5, 3.5)
 .xticks(np.arange(0, 4))
 .xlabel_fn(lambda n: x_tick_labels[n])
 .yticks(np.arange(0, 4, 0.5))
 .legends(['Blue', 'Purple', 'Green'])
 .data(data)
 ).show()
