"""Module for the Graph abstract class."""
from abc import ABC

import matplotlib.pyplot as plt
import numpy as np

from styles.style import Style


class Graph(ABC):
    """Abstract base class for all kind of graphs."""

    def __init__(self,
                 title=None,
                 size=(10.5, 6),
                 color_offset=0):
        """Initialize the Graph object."""
        self._figsize = size

        self._title = title

        # TODO(CustomColorOrder) Allow custom ordering of the color palette.
        self.style = Style.load_from_yaml('default_style.yaml')

        self._gridColor = '#AAAAAA'
        self._gridWidth = 1.0

        self._hide_labels = False

        self._xticks = None
        self._yticks = None

        self._spines = set(['bottom', 'left'])

        self._xlimit = None
        self._ylimit = None

        # Label
        self._xlabel_fn = None
        self._xlabel = ''
        self._ylabel = ''
        self._label_color = '#222222'

    def size(self, width, height):
        """Set the size of the figure."""
        self._figsize = (width, height)
        return self

    # def title(self, title):
    #     """Set the title of the graph."""
    #     self._title = title
    #     return self

    def hide_labels(self):
        """Hide the labels of the graph."""
        self._hide_labels = True
        return self

    def xticks(self, ticks):
        """Set the ticks for the x-axis."""
        self._xticks = ticks
        return self

    def yticks(self, ticks):
        """Set the ticks for the y-axis."""
        self._yticks = ticks
        return self

    def spines(self, spines):
        """Define what spines to show.

        Can be any number out of the following:
            'bottom', 'top', 'left', 'right'
        """
        self._spines = self._spines | set(spines)
        return self

    def xlim(self, xmin, xmax):
        """Set the limit for the x-axis."""
        self._xlimit = (xmin, xmax)
        return self

    def ylim(self, ymin, ymax):
        """Set the limit for the y-axis."""
        self._ylimit = (ymin, ymax)
        return self

    def xlabel(self, xlabel):
        """Set label for the x-axis."""
        self._xlabel = xlabel
        return self

    def ylabel(self, ylabel):
        """Set label for the y-axis."""
        self._ylabel = ylabel
        return self

    def labels(self, xlabel, ylabel):
        """Set labels for both x- and y-axis."""
        self.xlabel(xlabel)
        self.ylabel(ylabel)
        return self

    def xlabel_fn(self, fn):
        """Apply the given function to all labels on the x-axis.

        Can for example be used when labels should be mapped to a dictionary.
        """
        self._xlabel_fn = fn
        return self

    def label_color(self, color):
        """Set the color for the labels of both axes."""
        self._label_color = color
        return self

    def legends(self, legend_labels, position=None):
        """."""
        self._legend_labels = legend_labels

        return self

    def _prepare_plot(self, x_min, x_max, y_min, y_max):
        plt.close()  # ??

        fig, ax = plt.subplots(figsize=self._figsize,
                               facecolor='white',
                               edgecolor='white')

        ax.axes.tick_params(labelcolor=self._label_color, labelsize='10')

        #
        if self._xticks is not None:
            xticks = self._xticks
        else:
            step_size = (x_max - x_min) / 6.  # FIXME Round maybe?
            step_size = max(step_size, 0.1)  # Prevent 0 values.
            xticks = np.arange(x_min, x_max + step_size, step_size)

        if self._yticks is not None:
            yticks = self._yticks
        else:
            step_size = (y_max - y_min) / 6.  # FIXME Round maybe?
            step_size = max(step_size, 0.1)  # Prevent 0 values.
            yticks = np.arange(y_min, y_max + step_size, step_size)

        for axis, ticks in [(ax.get_xaxis(), xticks),
                            (ax.get_yaxis(), yticks)]:
            axis.set_ticks_position('none')
            axis.set_ticks(ticks)
            axis.label.set_color('#999999')
            if self._hide_labels:
                axis.set_ticklabels([])

        #
        if self._xlimit is not None:
            xlimit = self._xlimit
        else:
            margin = (x_max - x_min) / 10.
            xlimit = [x_min - margin, x_max + margin]

        if self._ylimit is not None:
            ylimit = self._ylimit
        else:
            margin = (y_max - y_min) / 10.
            ylimit = [y_min - margin, y_max + margin]

        axes = plt.gca()
        axes.set_xlim(xlimit)
        axes.set_ylim(ylimit)

        plt.grid(color=self._gridColor,
                 linewidth=self._gridWidth,
                 linestyle='-')

        for pos in (set(['bottom', 'top', 'left', 'right']) ^ self._spines):
            ax.spines[pos].set_visible(False)

        # FIXME Just for logaritmic x axes
        if self._xlabel_fn:
            plt.xticks(xticks,
                       [self._xlabel_fn(_x) for _x in xticks])
            # , rotation='vertical')

        if self._title:
            plt.title(self._title)

        # Set labels
        ax.set_xlabel(self._xlabel)
        ax.set_ylabel(self._ylabel)
        ax.xaxis.label.set_color(self._label_color)
        ax.yaxis.label.set_color(self._label_color)

    def pyplot(self, function_name, *args, **kwargs):
        """Call a function from the PyPlot library."""
        function = getattr(plt, function_name)
        function(*args, **kwargs)

        return self

    def save(self, path):
        """Save the graph under the specified file path."""
        plt.savefig(path)

        return self

    def show(self):
        """Display the graph."""
        plt.show()

        return self
