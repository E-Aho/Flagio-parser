import cv2

class Shape:

    def __init__(self, name: str = None, prototype=None):
        self.prototype = self.set_prototype(prototype)
        self.name = name

    def set_prototype(self, file):
        base = cv2.imread(file, 0)
        edge = cv2.Canny(base, 0, 200, apertureSize=3)
        return edge

star = Shape(name="5 point star", prototype=cv2.imread("Five_Pointed_Star_Solid.png"))
