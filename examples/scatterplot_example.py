"""Example for using a ScatterPlot."""
# TODO(SysPath) Get rid of hacky path magic.
import sys
sys.path.append('../pewdieplot')

import numpy as np

from pewdieplot.graph.scatterplot import ScatterPlot


# Build two point clouds from multivariate Gaussian distributions.
points_00 = np.random.multivariate_normal([0, 0], [[0.2, 0], [0, 0.2]], 200)
points_22 = np.random.multivariate_normal([2, 2], [[0.2, 0], [0, 0.2]], 200)
all_points = np.stack((points_00, points_22))

# Create and show the plot.
(ScatterPlot(title='Scatter Plot Example', size=(8, 5))
 .xlim(-2, 4)
 .ylim(-2, 4)
 .xticks(np.arange(-2, 4.5, 0.5))
 .yticks(np.arange(-2, 4.5, 0.5))
 .legends(['Mean (0, 0)', 'Mean (2, 2)'])
 .data(all_points)
 ).show()
