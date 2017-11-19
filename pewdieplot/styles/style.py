"""."""
import os
import yaml

import numpy as np


def _hex_to_float(hex_color):
    if len(hex_color) == 7:
        hex_color = hex_color[1:]
    colors = []
    for i in range(3):
        pos = i * 2
        hex_num = hex_color[pos:pos + 2]
        dec_num = int(hex_num, 16)
        colors.append(dec_num)

    colors = np.array(colors, dtype=np.float)
    # Normalize to range between 0 and 1.
    colors = colors / 255.

    return colors


class Style(object):
    """."""

    def __init__(self,
                 line_colors,
                 font):
        """Initialize the Style object."""
        self.line_colors = self._maybe_convert_color_format(line_colors)
        self.font = font

    def _maybe_convert_color_format(self, colors):
        if type(colors) is np.array:
            return colors

        converted_colors = [_hex_to_float(c) for c in colors]
        converted_colors = np.array(converted_colors)
        return converted_colors

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

        style_obj = Style(line_colors=style_dict['lineColors'],
                          font=None)
        return style_obj
