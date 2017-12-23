import colorsys


class ColorWheel(object):
    def __init__(self,
                 start_hue=240,
                 saturation=80,
                 lightness=60):
        """Init a new ColorWheel object.

        params:
            start_hue (int): A degree on the HSL color wheel between 0 and 359 (360 would be 0 again).
                Defaults to 240.
            saturation=100 (int): 0 to 100
                Defaults to 80.
            lightness (int): 0 = black, 50 = neutral, 100 = white.
                Defaults to 60.
        """

        if 0 <= start_hue < 360:
            self.start_hue = start_hue
        else:
            raise ValueError("'start_hue' can only take values from 0 to 359")

        if 0 <= saturation < 360:
            self.saturation = saturation
        else:
            raise ValueError("'saturation' can only take values from 0 to 359")

        if 0 <= lightness < 360:
            self.lightness = lightness
        else:
            raise ValueError("'lightness' can only take values from 0 to 359")

    def generate_colors(self, num):
        """Return 'num' colors from the HSL wheel in HLS format."""
        generated_colors = []

        for i in range(num):
            h = int((self.start_hue + (i * 360 / 3)) % 360)
            s = self.saturation
            l = self.lightness
            new_color = (h, s, l)
            generated_colors.append(new_color)

        return generated_colors

    def get_rgb_colors(self, num):
        """Return 'num' colors from the HSL wheel in RGB format."""
        generated_colors = self.generate_colors(num)

        rgb_colors = []
        for color in generated_colors:
            h, s, l = color
            new_rgb_color = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
            new_rgb_color = tuple(int(tone * 255) for tone in new_rgb_color)
            print(new_rgb_color)
            rgb_colors.append(new_rgb_color)

        return rgb_colors
