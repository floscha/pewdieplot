"""Module for the LineChart class."""
from graph import Graph

import matplotlib.pyplot as plt
import numpy as np


class LineChart(Graph):
    """A `Graph` displaying one more multiple lines."""

    def __init__(self, *args, **kwargs):
        """Initialize the LineChart object."""
        # Pass dict of constructor arguments to super class.
        super(LineChart, self).__init__(*args, **kwargs)

        self._legend_labels = []

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

        # Load colors.
        colors = np.array(self.style.line_colors.get_rgb_colors(len(lines))) / 255

        self._prepare_plot(0, 2 * np.pi, -1, 1)

        handles = []
        for i, line in enumerate(lines):
            x, y = line[:, 0], line[:, 1]
            h, = plt.plot(x, y,
                          c=colors[i],
                          lw=3,
                          alpha=0.7)
            handles.append(h)

        if self._legend_labels:
            plt.legend(handles, self._legend_labels)

        return self
