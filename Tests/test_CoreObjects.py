import pytest

from CoreObjects import *

class TestCategoriseColor:

    class TestReds:

        def test_normal_red(self):
            assert categorise_color(RGB((255, 0, 0))) == red

        def test_dark_red(self):
            assert categorise_color(RGB((51, 0, 0))) == red

        def test_deep_red(self):
            assert categorise_color(RGB((218, 53, 21))) == red

    class TestOranges:

        def test_normal_orange(self):
            assert categorise_color(RGB((255, 100, 0))) == orange

        def test_pale_orange(self):
            assert categorise_color(RGB((255, 204, 153))) == orange

        def test_red_orange(self):
            assert categorise_color(RGB((255, 107, 43))) == orange

        def test_light_brown(self):
            assert categorise_color(RGB((210, 180, 140))) == brown

        def test_normal_brown(self):
            assert categorise_color(RGB((89, 60, 31))) == brown

        def test_chocolate(self):
            assert categorise_color(RGB((92, 51, 23))) == brown

    class TestYellow:
        def test_normal_yellow(self):
            assert categorise_color(RGB((255, 255, 0))) == yellow

        def test_dark_yellow(self):
            assert categorise_color(RGB((177, 176, 70))) == yellow

        def test_pale_gold(self):
            assert categorise_color(RGB((192, 170, 60))) == yellow

        def test_pale_yellow(self):
            assert categorise_color(RGB((249, 255, 177))) == yellow

    class TestGreens:
        def test_normal_green(self):
            assert categorise_color(RGB((10, 255, 10))) == green

        def test_forest_green(self):
            assert categorise_color(RGB((1, 68, 33))) == green

        def test_olive_green(self):
            assert categorise_color(RGB((33, 42, 18))) == green

        def test_light_green(self):
            assert categorise_color(RGB((56, 93, 56))) == green

        def test_lime_green(self):
            assert categorise_color(RGB((173, 255, 47))) == green

    class TestBlues:
        def test_normal_blue(self):
            assert categorise_color(RGB((0, 0, 200))) == blue

        def test_cyan(self):
            assert categorise_color(RGB((0, 255, 255))) == blue

        def test_turquoise(self):
            assert categorise_color(RGB((0, 206, 209))) == blue

        def test_dodger_blue(self):
            assert categorise_color(RGB((30, 144, 255))) == blue

        def test_cornflower_blue(self):
            assert categorise_color(RGB((100, 149, 237))) == blue

        def test_light_blue(self):
            assert categorise_color(RGB((173, 216, 230))) == blue

    class TestPurples:

        def test_normal_purple(self):
            assert categorise_color(RGB((128, 0, 128))) == purple

        def test_medium_purple(self):
            assert categorise_color(RGB((147, 112, 219))) == purple

        def test_rebeca_purple(self):
            assert categorise_color(RGB((102, 51, 153))) == purple

    class TestPinks:

        def test_normal_pink(self):
            assert categorise_color(RGB((255, 192, 203))) == pink

        def test_deep_pink(self):
            assert categorise_color(RGB((255, 20, 147))) == pink

        def test_hot_pink(self):
            assert categorise_color(RGB((255, 105, 180))) == pink

    class TestWhite:
        def test_pure_white(self):
            assert categorise_color(RGB((255, 255, 255))) == white

        def test_smoke_white(self):
            assert categorise_color(RGB((245, 245, 245))) == white

        def test_slightly_off_whites(self):
            assert categorise_color(RGB((248, 248, 245))) == white
            assert categorise_color(RGB((255, 255, 248))) == white
            assert categorise_color(RGB((245, 251, 253))) == white

    class TestGrey:
        def test_normal_grey(self):
            assert categorise_color(RGB((155, 155, 15))) == grey

        def test_light_grey(self):
            assert categorise_color(RGB((233, 239, 241))) == grey

        def test_dark_grey(self):
            assert categorise_color(RGB((65, 65, 65))) == grey

        def test_steel_greys(self):
            assert categorise_color(RGB((131, 150, 154))) == grey
            assert categorise_color(RGB((131, 136, 154))) == grey

        def test_off_greys(self):
            assert categorise_color(RGB((200, 205, 198))) == grey
            assert categorise_color(RGB((205, 199, 204))) == grey
            assert categorise_color(RGB((115, 113, 110))) == grey

    class TestBlack:
        def test_normal_black(self):
            assert categorise_color(RGB((0, 0, 0))) == black

        def test_off_black(self):
            assert categorise_color(RGB((32, 33, 36))) == black
            assert categorise_color(RGB((34, 36, 29))) == black
            assert categorise_color(RGB((29, 36, 36))) == black
