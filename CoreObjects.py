from colorsys import rgb_to_hsv, hsv_to_rgb


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
        _hsv = tuple(map(int, values))
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
green = Color("green", RGB((0, 255, 0)))
blue = Color("blue", RGB((0, 0, 255)))
purple = Color("purple", RGB((127, 0, 255)))
pink = Color("pink", RGB((255, 51, 255)))
brown = Color("brown", RGB((102, 51, 0)))
black = Color("black", RGB((0, 0, 0)))
white = Color("white", RGB((255, 255, 255)))
grey = Color("grey", RGB((128, 128, 128)))

lime_green = SubColor("lime_green", RGB((128, 255, 0)), green)
sea_foam = SubColor("sea_foam", RGB((0, 255, 128)), green)
teal = SubColor("teal", RGB((0, 255, 255)), blue)


