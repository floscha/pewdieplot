import unittest

from pewdieplot.util.color_wheel import ColorWheel


class ColorWheelTest(unittest.TestCase):
    """Test suite for the ColorWheel class."""

    def test_correct_default_hls(self):
        """Simply assert wether the default values of an object are correct."""
        color_wheel = ColorWheel()

        self.assertEqual(240, color_wheel.start_hue)
        self.assertEqual(80, color_wheel.saturation)
        self.assertEqual(60, color_wheel.lightness)

    def _is_tuple_of_three_ints(self, var):
        """Helper method to assert type and size of a color tuple."""
        self.assertIs(tuple, type(var))
        self.assertEqual(3, len(var))
        for e in var:
            self.assertIs(int, type(e))

    def test_generating_three_hsl_colors_type(self):
        """Assert wether generated HSL colors are of the correct type."""
        color_wheel = ColorWheel()

        generated_colors = color_wheel.generate_colors(3)

        self.assertIs(list, type(generated_colors))
        for color in generated_colors:
            self._is_tuple_of_three_ints(color)

    def test_generating_three_hsl_colors_values(self):
        """Assert wether generated HSL colors contain the correct values."""
        color_wheel = ColorWheel()

        generated_colors = color_wheel.generate_colors(3)

        expected_saturation = 80
        expected_lightness = 60
        self.assertTupleEqual((240, expected_saturation, expected_lightness), generated_colors[0])
        self.assertTupleEqual((0, expected_saturation, expected_lightness), generated_colors[1])
        self.assertTupleEqual((120, expected_saturation, expected_lightness), generated_colors[2])

    def test_generating_three_rgb_colors_type(self):
        """Assert wether generated RGB colors are of the correct type."""
        color_wheel = ColorWheel()

        generated_colors = color_wheel.get_rgb_colors(3)

        self.assertIs(list, type(generated_colors))
        for color in generated_colors:
            self._is_tuple_of_three_ints(color)

    def test_getting_three_rgb_colors_values(self):
        """Assert wether generated RGB colors contain the correct values."""
        color_wheel = ColorWheel()

        generated_colors = color_wheel.get_rgb_colors(3)

        self.assertTupleEqual((71, 71, 234), generated_colors[0])
        self.assertTupleEqual((234, 71, 71), generated_colors[1])
        self.assertTupleEqual((71, 234, 71), generated_colors[2])


if __name__ == '__main__':
    unittest.main()
