"""Module for the LineChart class."""
# FIXME(RelativeImports) Get rid of relative imports.
from .graph import Graph

import matplotlib.pyplot as plt
import numpy as np


class LineChart(Graph):
    """."""

    def __init__(self, *args, **kwargs):
        """Initialize the LineChart object."""
        # Pass dict of constructor arguments to super class.
        super(LineChart, self).__init__(*args, **kwargs)

    def data(self, lines):
        """Set the data for the lines to be plotted."""
        # Check data format.
        if type(lines) is not np.array:
            lines = np.array(lines)
        assert len(lines.shape) in [2, 3]
        if len(lines.shape) == 2:
            lines = lines.reshape(1, -1, 2)
        if len(lines.shape) == 3 and lines.shape[1] == 2:
            lines = lines.reshape(1, -1, 2)

        # Calculate boundries and prepare the plot using them
        # x_min = min(min(l[0]) for l in lines)
        # x_max = max(max(l[0]) for l in lines)
        # y_min = min(min(l[1]) for l in lines)
        # y_max = max(max(l[1]) for l in lines)
        # self._prepare_plot(x_min, x_max, y_min, y_max)

        self._prepare_plot(0, 2 * np.pi, -1, 1)

        for i, line in enumerate(lines):
            x, y = line[:, 0], line[:, 1]
            plt.plot(x, y,
                     c=self.style.line_colors[i],
                     lw=3,
                     alpha=0.7)

        return self

    def show(self):
        """Display the graph."""
        super(LineChart, self).show()
