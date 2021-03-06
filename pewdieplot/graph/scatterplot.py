"""Module for the ScatterPlot class."""
import matplotlib.pyplot as plt
import numpy as np

from graph import Graph


class ScatterPlot(Graph):
    """A basic scatter plot implementation."""

    def __init__(self, *args, **kwargs):
        """Initialize the ScatterPlot object."""
        # Pass dict of constructor arguments to super class.
        super(ScatterPlot, self).__init__(*args, **kwargs)

        self._area = 10 ** 2
        self._legend_labels = []
        # Initialize color function with identity.
        self._color_function = lambda c, ps: c

    def area(self, area):
        """Set the area of the circles."""
        self._area = area

    def color_function(self, function):
        """Apply the given function to x and y, producing a color as output."""
        self._color_function = function

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

        # Load colors.
        colors = np.array(self.style.line_colors.get_rgb_colors(len(points))) / 255

        handles = []
        for i, ps in enumerate(points):
            x, y = zip(*ps)

            fill_colors = self._color_function(colors[i], ps)
            # fill_colors = fill_colors * 1.3
            # fill_colors = np.clip(fill_colors, 0.0, 1.0)
            # Use darkened fill color for edges.
            edge_colors = fill_colors * 0.8

            h = plt.scatter(x, y,
                            s=self._area,
                            c=fill_colors,
                            edgecolors=edge_colors,
                            alpha=0.7)
            handles.append(h)

        if self._legend_labels:
            plt.legend(handles, self._legend_labels)

        return self
