import pytest
import cv2

from src.ColorObjects import categorise_color, black, RGB, red, yellow
from tests.CoreFlags import trans_pride_flag, german_flag, french_flag, belgian_flag


class TestBasics:
    german_flag = german_flag
    french_flag = french_flag
    belgian_flag = belgian_flag
    trans_pride_flag = trans_pride_flag

    def test_can_show_image(self):
        top_pixel = RGB(german_flag[0, 0])
        mid_pixel = RGB(german_flag[int(german_flag.shape[0]/2), 0])
        bot_pixel = RGB(german_flag[-1, 0])
        print(bot_pixel)

        assert categorise_color(top_pixel) == black
        assert categorise_color(mid_pixel) == red
        assert categorise_color(bot_pixel) == yellow
