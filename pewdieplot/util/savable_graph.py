import matplotlib.pyplot as plt


class SavableGraph(object):
    """Intermediate graph object used for saving the graph to disk.

    Attributes:
        graph (Graph): The graph to be saved.
        file_path (str): The file to be created without extension.
    """

    def __init__(self, graph, file_path):
        """Initialize a new SavableGraph object."""
        self.graph = graph
        self.file_path = file_path

    def _save(self, file_path):
        """Save the graph to disk.

        Args:
            file_path (str): The file to be created including extension.
        """
        plt.savefig(file_path)

    def pdf(self):
        """Save the graph as a PDF file.

        Example:
            graph.save_as('bar_chart').pdf()
        """
        self._save(self.file_path + '.pdf')

    def png(self):
        """Save the graph as a PNG file.

        Example:
            graph.save_as('bar_chart').png()
        """
        self._save(self.file_path + '.png')
