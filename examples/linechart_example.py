"""Example for using a LineChart."""
# TODO(SysPath) Get rid of hacky path magic.
import sys
sys.path.append('../pewdieplot')
from fractions import Fraction

import numpy as np

from pewdieplot.graph.linechart import LineChart


# Create Sine, Cosinus and Tan curves.
x = np.arange(0, 2 * np.pi, 0.15)
sin_y = np.sin(x)
sin_points = np.dstack((x, sin_y))
cos_y = np.cos(x)
cos_points = np.dstack((x, cos_y))
tan_y = np.tan(x)
tan_points = np.dstack((x, tan_y))
all_points = np.concatenate((sin_points, cos_points, tan_points))

# Build and show Line Chart.
(LineChart('Line Chart Example', size=(8, 5))
 .xlim(0, 2 * np.pi)
 .ylim(-4, 4)
 .xticks(np.arange(0, 2 * np.pi + 0.1, 0.5 * np.pi))
 .yticks(np.arange(-5, 5, 1))
 .xlabel_fn(lambda n: r'$%s\pi$' % Fraction(n / np.pi))
 .legends(['Sine', 'Cosine', 'Tangent'])
 .data(all_points)
 .pyplot('annotate', 'Sine Max', xy=(0.5 * np.pi, 1), xytext=(2.5, 2),
         arrowprops=dict(facecolor='black', shrink=0.05))
 ).show()
