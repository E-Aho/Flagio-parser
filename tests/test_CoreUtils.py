import numpy as np
import pytest
import cv2

from src.ColorObjects import categorise_color, black, RGB, red, yellow
from src.CoreUtils import get_boundaries
from tests.CoreFlags import trans_pride_flag, german_flag, french_flag, belgian_flag, indian_flag, serbian_flag, \
    panama_flag


class TestBasics:
    german_flag = german_flag
    french_flag = french_flag
    belgian_flag = belgian_flag
    trans_pride_flag = trans_pride_flag

    def test_can_parse_image(self):
        top_pixel = RGB(german_flag[0, 0])
        mid_pixel = RGB(german_flag[int(german_flag.shape[0]/2), 0])
        bot_pixel = RGB(german_flag[-1, 0])

        print(type(german_flag))
        print(bot_pixel)

        assert categorise_color(top_pixel) == black
        assert categorise_color(mid_pixel) == red
        assert categorise_color(bot_pixel) == yellow

class TestGetBoundaries:
    german_flag = german_flag
    french_flag = french_flag
    belgian_flag = belgian_flag
    trans_pride_flag = trans_pride_flag
    indian_flag = indian_flag
    serbian_flag = serbian_flag
    panama_flag = panama_flag

    def test_works_for_germany(self):
        lines = get_boundaries(german_flag)
        assert len(lines) == 2

    def test_works_for_france(self):
        lines = get_boundaries(french_flag)
        assert len(lines) == 2

    def test_works_for_india(self):
        lines = get_boundaries(indian_flag)
        assert len(lines) == 2

    def test_works_for_trans(self):
        lines = get_boundaries(trans_pride_flag)
        assert len(lines) == 4

    def test_works_for_belgian(self):
        lines = get_boundaries(belgian_flag)
        assert len(lines) == 2

    def test_works_for_serbian(self):
        lines = get_boundaries(serbian_flag)
        print(len(lines))
        assert len(lines) == 2

    def test_works_for_panama(self):
        lines = get_boundaries(panama_flag)
        print(lines)
        assert len(lines) == 2

def

