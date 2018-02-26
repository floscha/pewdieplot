import numpy as np

from pewdieplot.graph.scatterplot import ScatterPlot

points_00 = np.random.multivariate_normal([0, 0], [[0.2, 0], [0, 0.2]], 200)
points_22 = np.random.multivariate_normal([2, 2], [[0.2, 0], [0, 0.2]], 200)
all_points = np.stack((points_00, points_22))

(ScatterPlot(title='Scatter Plot Example', size=(6, 3.5))
 .xlim(-2, 4.1)
 .ylim(-2, 4.1)
 .xticks(np.arange(-2, 4.5))
 .yticks(np.arange(-2, 4.5))
 .legends(['Mean (0, 0)', 'Mean (2, 2)'])
 .data(all_points)
 ).show()
pass  # Supress object output in notebook.
