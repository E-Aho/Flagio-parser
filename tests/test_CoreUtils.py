import pytest
import cv2

from tests.CoreFlags import trans_pride_flag, german_flag


class TestBasics:
    def test_can_show_image(self):
        flag = german_flag
        print(flag)

        cv2.imshow('image', flag)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

        assert True