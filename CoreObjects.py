from colorsys import rgb_to_hsv, hsv_to_rgb
from typing import Union


class RGB:
    def __init__(self, values: tuple):
        if len(values) != 3:
            raise Exception(f"Error: RGB value {values} does not have 3 values")
        _arr = []
        for i in range(3):
            try:
                v = int(values[i])
            except Exception:
                raise Exception(f"Error: RGB value {values} contains a value which can't be cast to type Int")
            else:
                if v < 0 or v > 255:
                    raise Exception(f"Error: RGB value {values} contains values out of range")
                _arr.append(v)

        self.r = int(_arr[0])
        self.g = int(_arr[1])
        self.b = int(_arr[2])

    def to_hsv(self):
        hsv_raw = rgb_to_hsv(self.r/255, self.g/255, self.b/255)
        return HSV((hsv_raw[0] * 360, hsv_raw[1], hsv_raw[2]))


class HSV:
    def __init__(self, values: tuple):
        if len(values) != 3:
            raise Exception(f"HSV Error: RGB value {values} does not have 3 values")
        _hsv = tuple(map(float, values))
        if _hsv[0] < 0 or _hsv[0] > 360:
            raise Exception(f"HSV Error: H value from HSV {values} is not between 0 and 360")
        elif _hsv[1] < 0 or _hsv[1] > 1:
            raise Exception(f"HSV Error: S value from HSV {values} is not between 0 and 1")
        elif _hsv[2] < 0 or _hsv[2] > 1:
            raise Exception(f"HSV Error: V value from HSV {values} is not between 0 and 1")

        self.h = _hsv[0]
        self.s = _hsv[1]
        self.v = _hsv[2]

    def to_rgb(self) -> RGB:
        rgb_raw = hsv_to_rgb(self.h, self.s, self.v)
        return RGB(tuple(x * 255 for x in rgb_raw))


class Color:
    def __init__(self, name: str, rgb: RGB):
        self.name = name
        self.rgb = rgb

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class SubColor(Color):
    def __init__(self, name: str, rgb: RGB, parent: Color):
        super().__init__(name, rgb)
        self.parent = parent

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


red = Color("red", RGB((255, 0, 0)))
orange = Color("orange", RGB((255, 128, 0)))
yellow = Color("yellow", RGB((255, 255, 0)))
green = Color("green", RGB((20, 255, 20)))
blue = Color("blue", RGB((10, 10, 255)))
purple = Color("purple", RGB((127, 0, 255)))
pink = Color("pink", RGB((255, 51, 255)))
brown = Color("brown", RGB((102, 51, 0)))
black = Color("black", RGB((0, 0, 0)))
white = Color("white", RGB((255, 255, 255)))
grey = Color("grey", RGB((128, 128, 128)))

gold = SubColor("gold", RGB((197, 179, 88)), yellow)


def categorise_color(value: Union[RGB, HSV]) -> Color:
    # Hard coded because for our use case, we have quite specific colors to pick out, and only care about broad cases
    # There is definitely a better way to do this but *shrug*

    c = None
    if isinstance(value, RGB):
        c = value.to_hsv()
    elif isinstance(value, HSV):
        c = value
    else:
        raise Exception("CategoriseColor Error: The given color is not in a valid format.")

    print(f"h: {c.h}, s: {c.s}, v: {c.v}")

    if c.v < 0.1 or (c.s < 0.2 and c.v < 0.15):
        return black
    elif c.s < 0.04 and c.v < 0.95 or (180 < c.h < 230 and c.s < 0.2 and c.v < 0.7):
        return grey
    elif c.s < 0.035 and c.v >= 0.95:
        return white

    else:  # not greyscale
        if 0 <= c.h < 15 or c.h >= 340:  # reds
            if c.s < 0.60 and (340 < c.h or 9 < c.h):
                return pink
            elif c.s < 0.75 and c.h > 10:
                return orange
            else:
                return red
        elif c.h < 43:  # oranges
            if c.v < 0.6 or (c.s < .6 and c.v < 0.9):
                return brown
            else:
                return orange
        elif c.h < 66:  # yellows
            return yellow
        elif c.h < 160:  # greens
            return green
        elif c.h < 259:  # blues
            return blue
        elif c.h < 309:  # purples
            return purple
        elif c.h < 340:  # pinks
            return pink
        else:
            raise Exception("CategoriseColor Error: Fallthrough.")

