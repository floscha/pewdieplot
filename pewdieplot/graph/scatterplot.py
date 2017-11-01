"""Module for the ScatterPlot class."""
# FIXME(RelativeImports) Get rid of relative imports.
from .graph import Graph

import matplotlib.pyplot as plt
import numpy as np


class ScatterPlot(Graph):
    """."""

    def __init__(self, *args, **kwargs):
        """Initialize the ScatterPlot object."""
        # Pass dict of constructor arguments to super class.
        super(ScatterPlot, self).__init__(*args, **kwargs)

        self._area = 10 ** 2
        self._legend_labels = []
        # Initialize color function with identity.
        self._color_function = lambda x: x

    def area(self, area):
        """Set the area of the circles."""
        self._area = area

    def color_function(self, function):
        """Apply the given function to x and y, producing a color as output."""
        self._color_function = function

    def legends(self, legend_labels, position=None):
        """."""
        self._legend_labels = legend_labels

        return self

    def data(self, points):
        """Set the data for the points to be plotted."""
        if type(points) is not np.array:
            points = np.array(points)
        assert len(points.shape) in [2, 3]
        if len(points.shape) == 2:
            points = points.reshape(1, -1, 2)
        if len(points.shape) == 3 and points.shape[1] == 2:
            points = points.reshape(1, -1, 2)

        # Calculate boundries and prepare the plot using them
        x, y = zip(*points[0])
        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)
        self._prepare_plot(x_min, x_max, y_min, y_max)

        handles = []
        for i, ps in enumerate(points):
            x, y = zip(*ps)
            h = plt.scatter(x, y,
                            s=self._area,
                            c=self.style.fill_colors[i],  # Apply color function.
                            edgecolors=self.style.line_colors[i],
                            alpha=0.75)
            handles.append(h)

        if self._legend_labels:
            plt.legend(handles, self._legend_labels)

        return self

    def show(self):
        """Display the graph."""
        super(ScatterPlot, self).show()
