"""Module for the BarChart class."""
import matplotlib.pyplot as plt
import numpy as np

from graph import Graph


class BarChart(Graph):
    """A basic bar chart implementation."""

    def __init__(self, *args, **kwargs):
        """Initialize the BarChart object."""
        # Pass dict of constructor arguments to super class.
        super(BarChart, self).__init__(*args, **kwargs)

        self._legend_labels = []

    def data(self, bar_data, overlapping=False):
        """Set the data for the line_data to be plotted."""
        # Check data format.
        if type(bar_data) is not np.array:
            bar_data = np.array(bar_data)
        assert len(bar_data.shape) in [1, 2]
        if len(bar_data.shape) == 1:
            bar_data = bar_data.reshape(1, -1)

        N = bar_data.shape[1]

        if overlapping:
            bar_width = 1/1.5
        else:
            bar_width = 0.8 / float(N)

        x_min, x_max = 0, N
        y_min, y_max = np.min(bar_data), np.max(bar_data)
        self._prepare_plot(x_min, x_max, y_min, y_max)

        # Load colors.
        colors = np.array(self.style.line_colors.get_rgb_colors(len(bar_data))) / 255

        fill_colors = colors * 1.3
        fill_colors = np.clip(fill_colors, 0.0, 1.0)
        darkened_line_colors = colors * 0.9

        # Has to be just before plot()?
        # plt.xticks(rotation=90)
        handles = []
        for i, bars in enumerate(bar_data):
            bar_offset = bar_width * i if not overlapping else 0
            x = np.arange(N)
            # Apply offset.
            bar_positions = x + bar_offset
            # Center bars around tick.
            bar_positions = bar_positions - 0.3
            h = plt.bar(bar_positions, bars,
                        bar_width,
                        color=fill_colors[i],
                        edgecolor=darkened_line_colors[i],
                        alpha=1.)
            handles.append(h)

        if self._legend_labels:
            plt.legend(handles, self._legend_labels)

        return self
