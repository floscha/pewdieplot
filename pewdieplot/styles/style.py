"""."""
import os
import yaml


class Style(object):
    """."""

    def __init__(self,
                 line_colors,
                 fill_colors,
                 font):
        """Initialize the Style object."""
        self.line_colors = line_colors
        self.fill_colors = fill_colors
        self.font = font

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
                          fill_colors=style_dict['fillColors'],
                          font=None)
        return style_obj
