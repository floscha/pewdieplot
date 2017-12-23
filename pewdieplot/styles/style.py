"""."""
import os
import yaml

import numpy as np

from ..util.color_wheel import ColorWheel


class Style(object):
    """Contains several style attributes for a graph."""

    def __init__(self):
        """Initialize the Style object."""
        self.line_colors = ColorWheel()

    @staticmethod
    def load_from_yaml(fpath):
        """Load a style defined in a YAML file."""
        styles_dir_path = os.path.dirname(os.path.realpath(__file__))
        style_file_path = os.path.join(styles_dir_path, fpath)
        with open(style_file_path, 'r') as f:
            try:
                style_dict = yaml.load(f)
            except yaml.YAMLError as e:
                print(e)

        style_obj = Style()
        return style_obj
